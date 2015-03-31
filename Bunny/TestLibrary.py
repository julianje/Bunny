from TestResult import *
import scipy.stats
import scipy.misc
import numpy as np

def Binomial(TestType="TT",alpha=0.05,Bias=0.5):
	# Binomial test
	if TestType=="TT":
		def F(Data):
			TestName="Two-tailed binomial test"
			Conditions=Data.shape[0]
			KeyStats = [Data[i].sum()*1.0/Data.shape[1] for i in range(Conditions)]
			pvals=[scipy.stats.binom_test(Data[i].sum(),Data.shape[1],Bias) for i in range(Conditions)]
			results = [i<alpha for i in pvals]
			final = 1 if sum(results)==Conditions else 0
			return TestResult(final,TestName,results,KeyStats,pvals)
	elif TestType=="OT":
		def F(Data):
			TestName="One-tailed binomial test"
			Conditions=Data.shape[0]
			KeyStats = [Data[i].sum()*1.0/Data.shape[1] for i in range(Conditions)]
			pvals=[scipy.stats.binom.sf(Data[i].sum()-1,Data.shape[1],Bias) for i in range(Conditions)]
			results = [i<alpha for i in pvals]
			final = 1 if sum(results)==Conditions else 0
			return TestResult(final,TestName,results,KeyStats,pvals)
	else:
		print "Error: Binomial test must be one-tailed (OT) or two-tailed (TT)."
		return None
	return F

def Majority():
	# Test for qualitative bias
	def F(Data):
		TestName="Testing if majority of data agrees with prediction"
		Conditions=Data.shape[0]
		results=[Data[i].sum()>Data.shape[1]*1.0/2 for i in range(Conditions)]
		final = 1 if sum(results)==Conditions else 0
		return TestResult(final,TestName,results)

def TTest(alpha=0.05):
	def F(Data):
		TestName="T-Test"
		if Data.shape[0]!=2:
			print "Error: T-test needs exactly two conditions"
			return None
		pval=scipy.stats.ttest_ind(Data[0],Data[1])[1]
		return TestResult(1,TestName) if pval<=alpha else TestResult(0,TestName)
	return F

def FisherExact(alpha=0.05):
	def F(Data):
		TestName="Fisher exact test"
		if Data.shape[0]!=2:
			print "Error: Fisher exact test needs exactly two conditions"
			return None
		V1=Data[0].sum(),Data.shape[1]-Data[0].sum()
		V2=Data[1].sum(),Data.shape[1]-Data[1].sum()
		pval=scipy.stats.fisher_exact([V1,V2])[1]
		return TestResult(1,TestName) if pval<=alpha else TestResult(0,TestName)
	return F

def MeanDifference(BootSamples=10000,inputalpha=0.05):
	"""
	Create function that bootstraps the mean difference across conditions
	"""
	def F(Data,Samples=BootSamples,alpha=inputalpha):
		TestName="Bootstrapped difference between means"
		Conditions=Data.shape[0]
		if Conditions<2:
			print "Error: MeanDifference test needs at least two conditions"
			return None
		#Comparisons = scipy.misc.comb(Conditions,2)
		Size=Data.shape[1]
		outcome = []
		for Condition1 in range(Conditions-1):
			for Condition2 in range(Condition1+1,Conditions):
				# Compare the two conditions.
				C1=Data[Condition1]
				C2=Data[Condition2]
				# Calculate their means
				#mean1=np.mean(C1)
				#mean2=np.mean(C2)
				# Generate resampling indexes for bootstrap
				indexes = np.random.randint(0,Size,(Samples, Size))
				# Get the difference in means for each sample.
				statistics = np.mean(C1[indexes],1)-np.mean(C2[indexes],1)
				# re-sort
				statistics = np.sort(statistics)
				# Get (1-alpha)% confidence interval
				lowerbound = statistics[int((alpha/2.0)*Samples)]
				upperbound = statistics[int((1-alpha/2.0)*Samples)]
				if (lowerbound<0 and upperbound<0) or (lowerbound>0 and upperbound>0):
					outcome.append(1)
				else:
					outcome.append(0)
		# Once done, check if all tests succeeded
		final = 1 if sum(outcome)==len(outcome) else 0
		return TestResult(final,TestName,outcome)
	return F

def BinomialWithControl(TestType="TT",alpha=0.05,Bias=0.5):
	print "Creating binomial with control. Make sure the test model is input before the control model in the experiment object."
	if TestType=="TT":
		TestName="First condition with two-tailed binomial test, and second condition as control."
		def F(Data):
			Conditions = Data.shape[0]
			if Conditions!=2:
				print "Error: BinomialWithControl needs exactly two conditions"
				return None
				pvals = [scipy.stats.binom_test(Data[i].sum(),Data.shape[1],Bias) for i in range(Conditions)]
				results = [i<alpha for i in pvals]
				final = 1 if (results[0]==1 and results[1]==0) else 0
				return TestResult(final,TestName,results,None,pvals)
	elif TestType=="OT":
		TestName="First condition with one-tailed binomial test, and second condition as control."
		def F(Data):
			Conditions = Data.shape[0]
			if Conditions!=2:
				print "Error: BinomialWithControl needs exactly two conditions"
				return None
				pvals = [scipy.stats.binom.sf(Data[i].sum()-1,Data.shape[1],Bias) for i in range(Conditions)]
				results = [i<alpha for i in pvals]
				final = 1 if (results[0]==1 and results[1]==0) else 0
				return TestResult(final,TestName,results,None,pvals)
	else:
		print "Error: Binomial test must be one-tailed (OT) or two-tailed (TT)."
		return None
	return F
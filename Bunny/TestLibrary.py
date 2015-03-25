import scipy.stats

def Binomial(TestType="TT",alpha=0.05,Bias=0.5):
	# Binomial test
	if TestType=="TT":
		def F(Data):
			pval=scipy.stats.binom_test(Data.sum(),Data.shape[1],Bias)
			return 1 if pval<=alpha else 0
	elif TestType=="OT":
		def F(Data):
			pval=scipy.stats.binom.sf(Data.sum()-1,Data.shape[1],Bias)
			return 1 if pval<=alpha else 0
	else:
		print "Error: Binomial test must be one-tailed (OT) or two-tailed (TT)."
		return None
	return F

def TTest(alpha=0.05):
	def F(Data):
		if Data.shape[0]!=2:
			print "Error: T-test needs exactly two conditions"
			return None
		pval=scipy.stats.ttest_ind(Data[0],Data[1])[1]
		return 1 if pval<=alpha else 0
	return F

def FisherExact(alpha=0.05):
	def F(Data):
		if Data.shape[0]!=2:
			print "Error: Fisher exact test needs exactly two conditions"
			return None
		V1=Data[0].sum(),Data.shape[1]-Data[0].sum()
		V2=Data[1].sum(),Data.shape[1]-Data[1].sum()
		pval=scipy.stats.fisher_exact([V1,V2])[1]
		return 1 if pval<=alpha else 0
	return F

#def BinomialWithControl(TestType="TT",alpha=0.05):
#	if TestType=="TT":
#		def F(Data):
#			if Data.shape[0]!=2:
#				print "Error: BinomialWithControl needs exactly two conditions"
#				return None

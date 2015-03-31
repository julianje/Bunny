from Experiment import *
from Participant import *
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import sys
import pickle
import time

def Explore(Exp,filename=None):
	if not Exp.Validate():
		print "Error: Experiment failed validation."
		return None
	print "Exploring sample sizes ... "
	res = ExploreSampleSize(Exp)
	PlotPowerSamples(res,filename)

def Hop(Exp,limit=100,power=None,samples=10000,Verbose=True):
	if power==None:
		if Exp.Power==None:
			if Verbose:
				print "Setting power to 0.95."
			power=0.95
		else:
			power=Exp.Power
	if (power>=1 or power<=0):
		if Verbose:
			print "Error: Power has to be between 0 and 1."
		return None
	if Verbose:
		sys.stdout.write("Power: "+str(power)+"\nLimit: "+str(limit)+"\nReplications per proposal: "+str(samples)+"\n")
	lower = 1
	upper = limit
	current = (upper-lower)/2+lower
	if Verbose:
		print "Searching for your sample size..."
	while True:
		sys.stdout.write("Simulating with "+str(current)+" participants per condition... ")
		sys.stdout.flush()
		Exp.SetSampleSize(current)
		p = Exp.GetPower(samples)
		if Verbose:
			sys.stdout.write("Power="+str(p)+"\n")
		if p < power:
			# If experiment is underpowered
			if (upper-lower)<=1:
				Exp.SetSampleSize(upper)
				Exp.UpdatePower()
				return [upper,Exp.Power]
			lower = current
			current = (upper-lower)/2+lower
		else:
			if (upper-lower)<=1:
				Exp.SetSampleSize(lower)
				Exp.UpdatePower()
				return [lower,Exp.Power]
			upper = current
			current = (upper-lower)/2+lower

def Inspect(Exp,RecomputePower=False):
	"""
	Print report of an experiment object.
	"""
	sys.stdout.write("\nValidating experiment...")
	if Exp.Validate():
		sys.stdout.write(" SUCCESS\n\n")
	sys.stdout.write("Experiment name: "+str(Exp.Name)+"\n")
	sys.stdout.write("Statistical test: "+str(Exp.StatTest.Name)+"\n\n")
	if not Exp.SampleSize==None:
		sys.stdout.write("Sample size: "+str(Exp.SampleSize)+"\n")
	else:
		sys.stdout.write("No sample size associated. Checking if I can estimate it... ")
		if not Exp.Power==None:
			sys.stdout.write("Yes.\nComputing smallest sample size needed... \n\n")
			Hop(Exp,limit=100,power=Exp.Power,samples=5000,Verbose=False)
			sys.stdout.write("Sample size: " + str(Exp.SampleSize)+"\n")
		else:
			sys.stdout.write("No.\nUse Bunny.Explore(Experiment) to see the relation between sampe size and power.\n")
	if not Exp.Power==None:
		if RecomputePower==True:
			Exp.UpdatePower()
			sys.stdout.write("Power: "+str(Exp.Power)+" (Freshly computed!)\n")
		else:
			sys.stdout.write("Power: "+str(Exp.Power)+" (Call Bunny.Inspect(True) to recompute power)\n")
	else:
		sys.stdout.write("No power. Checking if I can estimate it... ")
		if not Exp.SampleSize==None:
			sys.stdout.write("Yes.\n\n")
			Exp.UpdatePower()
			sys.stdout.write("Power: "+str(Exp.Power)+"\n")
		else:
			sys.stdout.write("No.\nUse Bunny.Explore(Experiment) to see the relation between sampe size and power.\n\n")

def Imagine(Exp,samples=10000):
	""" Plot key statistics """
	if Exp.SampleSize==None:
		print "ERROR: Need a sample size!"
		return None
	if len(Exp.Participants) == 1:
		Res = Exp.Replicate(samples)
		Stats = [Res[i].keystats[0] for i in range(samples)]
		Decisions = [Res[i].aggregatedecision for i in range(samples)]
		SuccessTrials_indices = [i for i, x in enumerate(Decisions) if x==1]
		FailedTrials_indices = [i for i, x in enumerate(Decisions) if x==0]
		SuccessTrials = [Stats[i] for i in SuccessTrials_indices]
		FailedTrials = [Stats[i] for i in FailedTrials_indices]
		Power = sum(Decisions)*1.0/len(Decisions)
		pylab.figure()
		n, bins, patches = pylab.hist([SuccessTrials, FailedTrials],10, histtype='bar', stacked=True, color=['green','red'], label=['Success','Fail'])
		pylab.legend()
		pylab.xlabel('Statistic value')
		pylab.ylabel('Number of observations')
		pylab.title(str(samples) + ' simulations with ' + str(Exp.SampleSize) + ' participants each. Power = ' + str(Power))
		pylab.show()
	else:
		print "Bunny.Imagine(Exp) only works for experiments with one condition"

def Save(Exp,Filename):
	Filename = Filename + ".p"
	pickle.dump(Exp,open(Filename, "wb"))

def Load(Filename):
	Experiment = pickle.load(open(Filename, "rb"))
	return Experiment

# Mid-level functions
def ExploreSampleSize(Exp,lower=1,limit=-1,samples=10000):
	if limit==-1:
		print "No limit specified. Testing samples between 15 and 35 ..."
		lower=15
		limit = 35
	Power=[]
	if lower>limit:
		print "Error: Lower limit is higher than upper limit"
		return None
	print "Estimating time ...."
	SampleSize=range(lower,limit+1)
	CurrSampleSize=Exp.SampleSize
	for i in SampleSize:
		if i==lower:
			start = time.time()
		Exp.SetSampleSize(i)
		Power.append(Exp.GetPower(samples))
		if i==lower:
			end = time.time()
			secs = (end-start)*len(SampleSize)
			sys.stdout.write("This will take at least ")
			if (secs<60):
				sys.stdout.write(str(round(secs,2))+ " seconds.\n")
			else:
				mins = secs*1.0/60
				if (mins<60):
					sys.stdout.write(str(round(mins,2))+ " minutes.\n")
				else:
					hours = mins*1.0/60
					sys.stdout.write(str(round(hours,2))+ " hours.\n")
	print "Done!"
	# Restore experiment object.
	if CurrSampleSize == None:
		Exp.ResetSampleSize()
		Exp.ResetPower()
	else:
		Exp.SetSampleSize(CurrSampleSize)
		Exp.UpdatePower(samples)
	return [SampleSize, Power]

def PlotPowerSamples(Samples,Filename=None):
	plt.clf()
	plt.plot(Samples[0],Samples[1],'bo',Samples[0],Samples[1],'k')
	plt.xlabel('Sample Size')
	plt.ylabel('Power')
	plt.title('Relation between sample size and power')
	plt.grid(True)
	if Filename==None:
		plt.show()
	else:
		plt.savefig(Filename)
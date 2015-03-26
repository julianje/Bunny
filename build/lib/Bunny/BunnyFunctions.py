from Experiment import *
from Participant import *
import matplotlib.pyplot as plt
import sys

def Explore(Exp,dimension="SampleSize"):
	if not Exp.Validate():
		print "Error: Experiment failed validation."
		return None
	if dimension=="SampleSize":
		print "Exploring sample sizes ... "
		res = ExploreSampleSize(Exp)
		PlotPowerSamples(res)

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
		print("Proposed Sample Size, Power")
	while True:
		Exp.SetSampleSize(current)
		p = Exp.GetPower(samples)
		if Verbose:
			sys.stdout.write(str(current)+","+str(p)+"\n")
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
			discard = Hop(Exp,limit=100,power=Exp.Power,samples=5000,Verbose=False)
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

# Mid-level functions
def ExploreSampleSize(Exp,lower=1,limit=-1,samples=50000):
	if limit==-1:
		print "No limit specified. Testing samples between 15 and 35 ..."
		lower=15
		limit = 35
	Power=[]
	if lower>limit:
		print "Error: Lower limit is higher than upper limit"
		return None
	SampleSize=range(lower,limit+1)
	CurrSampleSize=Exp.SampleSize
	for i in SampleSize:
		Exp.SetSampleSize(i)
		Power.append(Exp.GetPower(samples))
	Exp.SampleSize=CurrSampleSize # Restore experiment object.
	Exp.GetPower(samples)
	return [SampleSize, Power]

def PlotPowerSamples(Samples):
	plt.plot(Samples[0],Samples[1],'bo',Samples[0],Samples[1],'k')
	plt.show()
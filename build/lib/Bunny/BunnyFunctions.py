from Experiment import *
from Participant import *
import matplotlib.pyplot as plt

def Hop(Exp,dimension="SampleSize"):
	if not Exp.Validate():
		print "Error: Experiment failed validation."
		return None
	if dimension=="SampleSize":
		print "Exploring sample sizes ... "
		res = ExploreSampleSize(Exp)
		PlotPowersamples(res)

def ExploreSampleSize(Exp,lower=1,limit=-1,samples=1000):
	if limit==-1:
		print "No limit specified. Testing up to sample size of 40 ..."
		limit = 40
	Power=[]
	if lower>limit:
		print "Error: Lower limit is higher than upper limit"
		return None
	SampleSize=range(lower,limit+1)
	for i in SampleSize:
		Exp.SetSampleSize(i)
		Power.append(Exp.GetPower(samples))
	return [SampleSize, Power]

def PlotPowersamples(Samples):
	plt.plot(Samples[0],Samples[1],'bo',Samples[0],Samples[1],'k')
	plt.show()
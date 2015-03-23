from Experiment import *
from Participant import *
import matplotlib.pyplot as plt

def Hop(Exp):
	if not Exp.Validate():
		print "Error. Can't hop without a participant model and a statistical test."
		return None
	dimensions=Exp.GetMissing()
	if dimensions=="SampleSize":
		res = IncrementalSampleSize(Exp)
	plt.plot(res[0],res[1],'bo',res[0],res[1],'k')
	plt.show()

def IncrementalSampleSize(Exp,lower=1,limit=-1,Samples=1000):
	# Test sample size
	if limit==-1:
		print "No limit. Hopping up to 30."
		limit=30
	Power=[]
	SampleSize=range(1,limit+1)
	for i in SampleSize:
		Res=[Exp.Test(Exp.Participant.Recruit(i)) for _ in range(Samples)]
		Power.append(sum(Res)*1.0/Samples)
	return [SampleSize,Power]
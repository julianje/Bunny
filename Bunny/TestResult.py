### Class to contain results from statistical tests.

class TestResult(object):

	def __init__(self,aggregatedecision=None,TestName=None,decisions=None,keystats=None,pvals=None):
		self.aggregatedecision=aggregatedecision
		self.decisions=decisions
		self.keystats=keystats
		self.pvals=pvals
		self.testname=TestName

	def HasPvals(self):
		return 0 if self.pvals==None else 0

	def HasKeyStats(self):
		return 0 if self.keystats==None else 0

	def Display(self, Full=True):
		# Print class properties
		if Full:
			for (property, value) in vars(self).iteritems():
				print property, ': ', value
		else:
			for (property, value) in vars(self).iteritems():
				print property

class Participant(object):
	"""
	Participant class.
	Contains a model of a participant
	"""

	def __init__(self):
		self.Name="Skeleton Participant"
		self.Generator=None

	def Execute(self):
		if self.Generator == None:
			print "Missing generator!"
			return None
		return self.Generator()

	def Recruit(self,Samples):
		if self.Generator == None:
			print "Missing generator!"
			return None
		Outcome = [self.Execute() for _ in range(Samples)]
		return Outcome

	def SetBehavior(self, Generator):
		self.Generator = Generator

	def Validate(self):
		if self.Generator==None:
			print "Error. No generator in Participant object."
			return 0
		else:
			return 1
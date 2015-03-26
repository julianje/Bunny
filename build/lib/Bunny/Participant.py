
class Participant(object):
	"""
	Participant class.
	Contains a model of a participant.

	Execute()  generates one sample
	Sample(n) generates n samples
	SetBehavior(f) sets function f as the behavior model
	Validate() ensures the object has a function stored
	AddName(N) set object name to N
	Display(B) prints properties, B is boolean value indicating verbosity
	"""

	def __init__(self,Behavior=None,Name="Participant_Object"):
		self.Name=Name
		self.Behavior=Behavior

	def Execute(self):
		if self.Validate():
			return self.Behavior()
		else:
			return None

	def Sample(self,Samples):
		if self.Validate():
			Outcome = [self.Execute() for _ in range(Samples)]
			return Outcome
		else:
			return None

	def SetBehavior(self, Behavior):
		self.Behavior = Behavior

	def AddName(self, Name):
		self.Name = Name

	def Validate(self):
		if self.Behavior==None:
			print "ERROR: Participant object doesn't have a model of behavior.\nUse Participant.SetBehavior()"
			return 0
		else:
			return 1

	def Display(self, Full=True):
		# Print class properties
		if Full:
			for (property, value) in vars(self).iteritems():
				print property, ': ', value
		else:
			for (property, value) in vars(self).iteritems():
				print property
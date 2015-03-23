from Participant import *
from DataTest import *

class Experiment(object):
	"""
	Experiment class.
	Contains information about an experiment
	"""

	def __init__(self,Participant=None,StatTest=None,Name="Experiment skeleton"):
		self.Youngest=None
		self.Oldest=None
		self.SampleSize=None
		self.Participant=Participant
		self.StatTest=StatTest
		self.Name=Name

	def AddParticipants(self,Participant):
		self.Participant = Participant

	def AddTest(self,Test):
		self.StatTest = Test

	def Test(self,Data):
		return self.StatTest.RunTest(Data)

	def GetMissing(self):
		return "SampleSize"

	def Validate(self):
		if self.Participant==None or self.StatTest==None:
			return 0
		else:
			if not self.StatTest.Validate():
				return 0
			if not self.Participant.Validate():
				return 0
			return 1
from Participant import *
from DataTest import *
import numpy as np

class Experiment(object):
	"""
	Experiment class.
	Contains information about an experiment

	SetParticipant(P) adds participant p to experiment
	SetTest(T)        adds test t to experiment
	Test(D)           runs test T on data D (calling datatest method)
	Validate()		  checks if Experiment object is ready to go
	Display(B) prints properties, B is boolean value indicating verbosity
	"""

	def __init__(self,Participants=None,StatTest=None,Name="Experiment_Skeleton_Object"):
		self.SampleSize = None
		if Participants==None:
			self.Participants=[]
		else:
			if not isinstance(Participants,list):
				Participants = [Participants]
			self.Participants = Participants
		self.StatTest = StatTest
		self.Name = Name

	def SetParticipants(self,Participants):
		"""
		Set a list of participant models to the experiment.
		"""
		if (self.Participants != []):
			print "WARNING: You've replaced the participant models.\nDid you mean to use Experiment.AddParticipants()?"
		self.Participants = [Participants]

	def GetPower(self, N=1000):
		results = self.Replicate(N)
		return sum(results)*1.0/len(results)

	def Replicate(self, N=1000):
		"""
		Simulate experiment N times
		"""
		return [self.RunExperiment() for _ in range(N)]

	def RunExperiment(self):
		"""
		Simulate experiment and run test
		"""
		return self.TestData(self.CollectData())

	def TestData(self,Data):
		"""
		Run test on dataset
		"""
		return self.StatTest.RunTest(Data)

	def CollectData(self):
		"""
		Get data from each participant model according to specified sample size.
		"""
		# Check how many conditions you have (as participant models)
		Conditions = len(self.Participants)
		# Initialize an empty array
		Data = np.zeros((Conditions,self.SampleSize))
		# Fill each row by drawing samples from each participant model
		for i in range(Conditions):
			Data[i] = self.Participants[i].Sample(self.SampleSize)
		return Data

	def AddParticipants(self,Participants):
		"""
		Add one or more participant models to an existing list of models
		"""
		# If they only sent one participant make sure its a list
		if not isinstance(Participants,list):
			Participants = [Participants]
		self.Participants.extend(Participants)

	def SetSampleSize(self, SampleSize):
		self.SampleSize=SampleSize

	def SetTest(self,Test):
		self.StatTest = Test

	def Validate(self):
		"""
		Check if the experiment object is ready to run.
		"""
		V1=self.ValidateParticipants()
		V2=self.ValidateTest()
		if ((V1==1) and (V2==1)):
			return 1
		else:
			return 0

	def ValidateParticipants(self):
		"""
		Call validation method for all participant models.
		"""
		if self.Participants == None or self.Participants == []:
			print "ERROR: No participants associated with experiment"
			return 0
		ParticipantValidations = [i.Validate() for i in self.Participants]
		if (sum(ParticipantValidations)!=len(ParticipantValidations)):
			print "ERROR: At least one participant model in the experiment failed to validate itself."
			return 0
		return 1

	def ValidateTest(self):
		"""
		Call validation method for test object.
		"""
		if not self.StatTest.Validate():
			print "ERROR: DataTest object failed to validate itself.\nExperiment needs a validated DataTest object\n(run self.Validate() on your data test before attaching it to an experiment)."
			return 0
		return 1

	def Display(self, Full=True):
		# Print class properties
		if Full:
			for (property, value) in vars(self).iteritems():
				print property, ': ', value
		else:
			for (property, value) in vars(self).iteritems():
				print property
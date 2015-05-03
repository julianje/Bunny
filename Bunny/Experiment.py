# -*- coding: utf-8 -*-

"""
Experiment objects bind Participant and DataTest object together with supporting functions.
"""

__license__ = "MIT"

from Participant import *
from DataTest import *
from TestResult import *
import numpy as np
import warnings


class Experiment(object):

    def __init__(self, Participants=None, StatTest=None, Name="Experiment_Object"):
        """
        Create a new experiment object.

        Args:
            Participants (Participant OR list): A participant object or a list of Participant objects

            StatTest (DataTest): A DataTest object

            Name (str) : Experiment's name

        Returns:
            Experiment object

        >> Experiment(MyParticipant,MyTest,"Experiment")

        >> Experiment([MyParticipantTest,MyParticipantControl],MyTest,"Experiment") # Test must know how to handle two conditions

        >> Experiment([MyParticipant]*2,MyTest,"Experiment") # Equivalent to above
        """
        self.SampleSize = None
        if Participants is None:
            self.Participants = []
        else:
            if not isinstance(Participants, list):
                Participants = [Participants]
            self.Participants = Participants
        self.StatTest = StatTest
        self.Name = Name
        self.Power = None

    def SetParticipants(self, Participants):
        """
        Insert one or more participant models into the experiment

        Args:
            Participants (Participant OR list): A participant object or a list of Participant objects

        Returns:
            None

        >> MyExperiment.SetParticipants(MyParticipant)

        >> MyExperiment.SetParticipants([MyParticipantTest,MyParticipantControl]) # Test must know how to handle two conditions
        """
        if (self.Participants != []):
            print "WARNING: You've replaced the participant models.\nDid you mean to use Experiment.AddParticipants()?"
        self.Participants = [Participants]

    def SetPower(self, Power):
        """
        Set an experiment's power. Some functions can fill this in automatically (e.g., Inspect). But you can also use it to find a sample size.

        Args:
            Power (float): Experiment's power

        Returns:
            None

        >> MyExperiment.SetPower(0.95)
        """
        self.Power = Power

    def UpdatePower(self, samples=1000):
        """
        Recompute and save experiment's new power. Needs Experiment object to have a sample size.

        Args:
            samples (int): Number of samples to use

        Returns:
            None

        >> MyExperiment.UpdatePower()
        """
        self.Power = self.GetPower(samples)

    def ResetPower(self):
        """
        Remove experiment's power

        Args:
            None

        Returns:
            None

        >> MyExperiment.ResetPower()
        """
        self.Power = None

    def GetPower(self, samples=1000):
        """
        Recompute an experiment's power without storing it. This is function supports search over sample sizes and requires the experiment to have a set sample size.

        Args:
            samples (int): Number of samples to use

        Returns:
            power (int): Experiment's power

        >> MyExperiment.UpdatePower()
        """
        results = self.ExtractDecision(self.Replicate(samples))
        return sum(results) * 1.0 / len(results)

    def ExtractDecision(self, Data):
        """
        Extract a DataTest's final decision to calculate it's power

        .. Internal function::

           This function is for internal use only.

        Args:
            Data (TestResult): TestResult object.

        Returns:
            power (bool): Indicator about whether simulation fulfilled DataTest's final criteria.
        """
        return [Data[i].aggregatedecision for i in range(len(Data))]

    def Replicate(self, N=1000):
        """
        Simulate data collection and analysis N times

        .. Internal function::

           This function is for internal use only.

        Args:
            N (int): Number of experiment simulations.

        Returns:
            Results (list): List of N TestResult objects
        """
        if self.SampleSize is None:
            print "ERROR: Need a sample size! (Use Exp.SetSampleSize())"
            return None
        return [self.RunExperiment() for _ in range(N)]

    def RunExperiment(self):
        """
        Simulate data collection and analysis once

        .. Internal function::

           This function is for internal use only.

        Args:
            None

        Returns:
            TestResult object
        """
        D = self.CollectData()
        warnings.filterwarnings('ignore', category=FutureWarning)
        if D is None:
            print "Failed to get data."
            return None
        else:
            return self.TestData(D)

    def TestData(self, Data):
        """
        Run experiment's data test on the result from a simulation

        .. Internal function::

           This function is for internal use only.

        Args:
            Data (array): An array produced by Experiment.CollectData()

        Returns:
            TestResult object
        """
        return self.StatTest.RunTest(Data)

    def CollectData(self):
        """
        Simulate data collection once

        .. Internal function::

           This function is for internal use only.

        Args:
            None

        Returns:
            NxM Array where N is the number of participant models and M is the number of conditions.
        """
        if self.SampleSize is None:
            print "Error: No sample size!"
            return None
        # Check how many conditions you have (as participant models)
        Conditions = len(self.Participants)
        # Initialize an empty array
        Data = np.zeros((Conditions, self.SampleSize))
        # Fill each row by drawing samples from each participant model
        for i in range(Conditions):
            Data[i] = self.Participants[i].Sample(self.SampleSize)
        return Data

    def AddParticipants(self, Participants):
        """
        Add a participant model to experiment. In contrast to SetParticipants(), this function leaves past participant models instead of replacing them.

        Args:
            Participants (list or Participant object): A participant object or a list of participant objects

        Returns:
            None
        """
        # If they only sent one participant make sure its a list
        if not isinstance(Participants, list):
            Participants = [Participants]
        self.Participants.extend(Participants)

    def SetSampleSize(self, SampleSize):
        """
        Add a sample size to Experiment.

        Args:
            SampleSize (int): Experiment's sample size

        Returns:
            None

        >> MyExperiment.SetSampleSize(16)
        >> Inspect(MyExperiment) # Will use sample size to set power.
        """
        if SampleSize is None:
            self.SampleSize = None
        elif int(SampleSize) <= 0:
            print "Error: Sample size must be positive integer."
        else:
            self.SampleSize = int(SampleSize)

    def ResetSampleSize(self):
        """
        Remove experiment's sample size

        Args:
            None

        Returns:
            None
        """
        self.SampleSize = None

    def SetTest(self, Test):
        """
        Insert DataTest object to experiment

        Args:
            Test (DataTest object)

        Returns:
            None
        """
        self.StatTest = Test

    def Validate(self):
        """
        Check that experiment object has all information necessary to run simulations.

        .. Internal function::

           This function is for internal use only.

        Args:
            None

        Returns:
            bool
        """
        V1 = self.ValidateParticipants()
        V2 = self.ValidateTest()
        if (V1 and V2):
            # Check if you can run an experiment through the whole process
            try:
                TestData = np.zeros((len(self.Participants), 1))
                for i in range(len(self.Participants)):
                    TestData[i] = self.Participants[i].Sample(1)
                self.StatTest.RunTest(TestData)
            except:
                print "Behavior and test validated, but failed to connect!"
                raise
                return 0
        else:
            return 0
        return 1

    def ValidateParticipants(self):
        """
        Check that Participant objects have all information necessary to run simulations.

        .. Internal function::

           This function is for internal use only.

        Args:
            None

        Returns:
            bool
        """
        if self.Participants is None or self.Participants == []:
            print "ERROR: No participants associated with experiment"
            return 0
        ParticipantValidations = [i.Validate() for i in self.Participants]
        if (sum(ParticipantValidations) != len(ParticipantValidations)):
            print "ERROR: At least one participant model in the experiment failed to validate itself."
            return 0
        return 1

    def ValidateTest(self):
        """
        Check that DataTest objects have all information necessary to run simulations.

        .. Internal function::

           This function is for internal use only.

        Args:
            None

        Returns:
            bool
        """
        if not self.StatTest.Validate():
            print "ERROR: DataTest object failed to validate itself.\nExperiment needs a validated DataTest object\n(run self.Validate() on your data test before attaching it to an experiment)."
            return 0
        return 1

    def Display(self, Full=True):
        """
        Print object attributes.

        .. Internal function::

           This function is for internal use only.

        Args:
            Full (bool): When set to False, function only prints attribute names. Otherwise, it also prints its values.

        Returns:
            standard output summary
        """
        if Full:
            for (property, value) in vars(self).iteritems():
                print property, ': ', value
        else:
            for (property, value) in vars(self).iteritems():
                print property

# -*- coding: utf-8 -*-

"""
Participant objects wrap a behavior model with supporting functions.
"""

__license__ = "MIT"

import inspect


class Participant(object):

    def __init__(self, Behavior=None, Name="Participant_Object"):
        """
        Participant class.

        Contains a model of a participant.

        Args:
            Behavior (function): Function that returns a single number and can be called
                                 without suppling additional parameters
            Name (str): Object's name.
        """
        if isinstance(Behavior, list):
            # If the behavior is a list, then extract it's name
            # and information about variation.
            self.Behavior = Behavior[0]
            if Name == "Participant_Object":
                self.Name = Behavior[1]
            else:
                self.Name = Name
        else:
            # Otherwise the input is likely just a function
            self.Behavior = Behavior
            self.Name = Name

    def Execute(self):
        """
        Collect a single data point.

        .. warning::

           This function is for internal use only.

        Args:
            None

        Returns:
            Call from Behavior function

        >> MyParticipant.Execute()
        """
        return self.Behavior()

    def Sample(self, Samples):
        """
        Collect n samples.

        .. warning::

           This function is for internal use only.

        Args:
            Samples (int) : Number of samples.

        Returns:
            Outcomes (list) : List of function calls

        >> MyParticipant.Sample(5)
        """
        Outcome = [self.Execute() for _ in range(Samples)]
        return Outcome

    def SetBehavior(self, Behavior, Name="Participant_Object"):
        """
        Set behavior model

        Args:
            Behavior (function) : Behavior function (Found in Behaviors library; see wiki).
            Name (str) : Function's name.

        Returns:
            None

        >> MyParticipant.SetBehavior(Behaviors.BernoulliAgent(0.5))
        """
        if isinstance(Behavior, list):
            # If the behavior is a list, then extract it's name
            # and information about variation.
            self.Behavior = Behavior[0]
            if Name == "Participant_Object":
                self.Name = Behavior[1]
            else:
                self.Name = Name
        else:
            # Otherwise the input is likely just a function
            self.Behavior = Behavior
            # Replace name.
            self.Name = Name

    def AddName(self, Name):
        """
        Associate name with object

        Args:
            Name (str) : Function's name.

        Returns:
            None

        >> MyParticipant.AddName("Bernoulli model")
        """
        self.Name = Name

    def Validate(self):
        """
        Check that object has all information necessary to run simulations.

        .. warning::

           This function is for internal use only.

        Args:
            None

        Returns:
            bool
        """
        if self.Behavior is None:
            print "ERROR: Participant object doesn't have a model of behavior.\nUse Participant.SetBehavior()"
        elif not hasattr(self.Behavior, '__call__'):
            print "ERROR: Cannot call behavior function."
        else:
            res = inspect.getargspec(self.Behavior)
            if len(res.args) > 0 and (res.defaults is None):
                print "ERROR: Function requires arguments. Cannot use!"
                return 0
            if len(res.args) > 0 and (res.defaults is not None):
                if len(res.args) != len(res.defaults):
                    print "ERROR: Function requires arguments. Cannot use!"
                    return 0
            try:
                self.Behavior()
            except:
                print "Unexpected error in participant model!"
                return 0
        return 1

    def Display(self, Full=True):
        """
        Print object attributes.

        .. warning::

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

# -*- coding: utf-8 -*-

"""
Participant objects wrap a behavior model with supporting functions.
"""

__license__ = "MIT"


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

    def __init__(self, Behavior=None, Name="Participant_Object"):
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
        if isinstance(Behavior, list):
            # If the behavior is a list, then extract it's name
            # and information about variation.
            self.Behavior = Behavior[0]
            if Name == "Participant_Object":
                self.Name = Behavior[1]
            else:
                self.Name = Name
            self.InputVariation = Behavior[2]
        else:
            # Otherwise the input is likely just a function
            self.Behavior = Behavior
            self.Name = Name
            # No information about whether function takes arguments
            self.InputVariation = "Unknown"

    def Execute(self):
        return self.Behavior()

    def Sample(self, Samples):
        Outcome = [self.Execute() for _ in range(Samples)]
        return Outcome

    def SetBehavior(self, Behavior, Name="Participant_Object"):
        if isinstance(Behavior, list):
            # If the behavior is a list, then extract it's name
            # and information about variation.
            self.Behavior = Behavior[0]
            if Name == "Participant_Object":
                self.Name = Behavior[1]
            else:
                self.Name = Name
            self.InputVariation = Behavior[2]
        else:
            # Otherwise the input is likely just a function
            self.Behavior = Behavior
            # No information about whether function takes arguments
            self.InputVariation = "Unknown"
            # Replace name.
            self.Name = Name

    def AddName(self, Name):
        self.Name = Name

    def Validate(self):
        if self.Behavior is None:
            print "ERROR: Participant object doesn't have a model of behavior.\nUse Participant.SetBehavior()"
        elif not hasattr(self.Behavior, '__call__'):
            print "ERROR: Cannot call behavior function."
        else:
            try:
                self.Sample(1)
            except:
                print "Unexpected error in participant model!"
                raise
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

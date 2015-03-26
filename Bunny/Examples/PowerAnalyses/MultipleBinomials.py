# You are running many binomial experiments and want to check the probability that they all work
import Bunny

# To see detailed code version see SimpleBinomial.py example
Child = Bunny.Participant(Bunny.ParticipantLibrary.Binomial(0.9))
StatTest = Bunny.DataTest(Bunny.TestLibrary.Binomial("OT"))

# Give five child models to the experiment
Experiment = Bunny.Experiment([Child]*5,StatTest,"2-AFC task")

Bunny.Inspect(Experiment) # Will now work on the assumption that you want all five experiments to succeed.

# If you think some tasks are more difficult than others..
# Model where 90% gets answer correct
ChildEasy = Bunny.Participant(Bunny.ParticipantLibrary.Binomial(0.9))
# Model where 75% gets answer correct
ChildDifficult = Bunny.Participant(Bunny.ParticipantLibrary.Binomial(0.75))
StatTest = Bunny.DataTest(Bunny.TestLibrary.Binomial("OT"))

# 3 Experiments. You think 2 are easy and 1 is more challenging
Experiment = Bunny.Experiment([ChildEasy,ChildEasy,ChildDifficult],StatTest,"2-AFC task")

Bunny.Inspect(Experiment) # Will now work on the assumption that you want all five experiments to succeed.

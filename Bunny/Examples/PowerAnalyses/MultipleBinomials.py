# You are running many binomial experiments and want to check the
# probability that they all work
import Bunny

# To see detailed code version see SimpleBinomial.py example
Child = Bunny.Participant(Bunny.ParticipantLibrary.Binomial(0.9))
StatTest = Bunny.DataTest(Bunny.TestLibrary.Binomial("OT"))

# Give five child models to the experiment
# In python [Child]*5 is a short way of writing [Child,Child,Child,Child,Child]
Experiment = Bunny.Experiment([Child] * 5, StatTest, "2-AFC task")

# Will now work on the assumption that you want all five experiments to
# succeed.
Bunny.Inspect(Experiment)
# See SimpleBinomial.py experiment on how to play around with experiment
# objects

# If you think some tasks are more difficult than others..
# Model where 90% gets answer correct
ChildEasy = Bunny.Participant(Bunny.ParticipantLibrary.Binomial(0.9))
# Model where 75% gets answer correct
ChildDifficult = Bunny.Participant(Bunny.ParticipantLibrary.Binomial(0.75))
StatTest = Bunny.DataTest(Bunny.TestLibrary.Binomial("OT"))

# 3 Experiments. You think 2 are easy and 1 is more challenging
Experiment = Bunny.Experiment(
    [ChildEasy, ChildEasy, ChildDifficult], StatTest, "2-AFC task")

# Will now work on the assumption that you want all five experiments to
# succeed.
Bunny.Inspect(Experiment)

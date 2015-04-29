# Model a set of 2-alternative forced choice tasks.
# Analysis: two-tailed binomial tests.

# This model builds upon 2AFC_task.py

from Bunny import *

#############
# EXAMPLE 1 #
#############

# You expect participant to have the same behavior in all conditions

# Create a binomial agent with probability of success = 0.8
Behavior = Participant(Behaviors.BinomialAgent(0.8))
# Create a DataTest that runs a binomial test
Test = DataTest(Tests.BinomialTest("OT"))
# Create an experiment object with three conditions.
# You can also replace [Behavior, Behavior, Behavior] for [Behavior]*3
MyExperiment = Experiment([Behavior, Behavior, Behavior], Test, "2-AFC task")
# Now, your experiment assumes that you will run three conditions and use the same test on all conditions.
# Remember: Sample size now indicates sample size per condition.
Explore(MyExperiment)
# Find a sample size given your power
MyExperiment.SetPower(0.95)
Hop(MyExperiment)
# Visualize your experiment's power given a sample size
# Success now means that *all* three experiments were significant
MyExperiment.SetSampleSize(16)
Imagine(MyExperiment)

#############
# EXAMPLE 2 #
#############

# You expect participants to behave differently in different conditions

# You expect 90% of participants to succeed in the first condition, but only 75% to succeed in the second condition.
BehaviorModelA = Participant(Behaviors.BinomialAgent(0.9))
BehaviorModelB = Participant(Behaviors.BinomialAgent(0.75))

# Create a DataTest that runs a binomial test
Test = DataTest(Tests.BinomialTest("OT"))
# Create an experiment object with three conditions.
MyExperiment = Experiment([BehaviorModelA, BehaviorModelB], Test, "2-AFC task")
# See section above for how to use the experiment object. All functions will now assume you want both conditions to succeed.

#############
# EXAMPLE 3 #
#############

# A test and a control condition

# You expect 75% of participants to succeed in the first condition, but onlye 50% to succeed in the second condition.
# However you are now expecting for the first test to be significant and the second one to be non-significant.
BehaviorTestModel = Participant(Behaviors.BinomialAgent(0.75))
BehaviorControlModel = Participant(Behaviors.BinomialAgent(0.5))

# The lest library comes with a test that does this:
Test = DataTest(Tests.BinomialWithControlTest("OT"))
# You will see a message letting you know that Bunny is assuming that the first condition is test and the second one is control.
MyExperiment = Experiment([BehaviorTestModel, BehaviorControlModel], Test, "2-AFC task")
# See section above for how to use the experiment object.

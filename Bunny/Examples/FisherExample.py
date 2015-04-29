# Model an experiment with two conditions
# that you expect to appear significantly
# different as given by Fisher's exact test.

# This file shows the simplest implementation.
# To get more insight into the code please see 2AFC_task.py first.

# See 2AFC_task.py for other things you can do with Exp.

from Bunny import *

ConditionA = Participant(Behaviors.BinomialAgent(0.8))
ConditionB = Participant(Behaviors.BinomialAgent(0.2))

StatTest = DataTest(Tests.FisherExactTest())

Exp = Bunny.Experiment(
    [ConditionA, ConditionB], StatTest, "Contrastive conditions")

# Look at power vs sample size graph.
Explore(Exp)

# Model an experiment where the behavior is sampled
# from an empirical distribution

from Bunny import *

P1 = Participant(Behaviors.EmpiricalAgent([1, 2, 3, 3, 3, 3, 5]))
# Equivalent to:
# P1 = Participant(Behaviors.EmpiricalAgent([[1,1],[2,1],[3,4],[5,1]]))

P2 = Participant(Behaviors.EmpiricalAgent([1, 2, 5, 5, 9, 10]))

Test = Bunny.DataTest(Bunny.TestLibrary.TTest())

MyExp = Experiment([P1, P2], Test)

# See 2AFC_task for examples on what to do with the experiment object.

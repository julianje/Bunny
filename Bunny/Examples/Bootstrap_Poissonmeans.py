# Model an experiment where participants perform
# a discrete number of actions.

from Bunny import *

# Create a model of a participant where their behavior is Poisson-distributed
# with mean 9
P1 = Participant(Behaviors.PoissonAgent(9), "High Condition")
# Create a model of a participant where their behavior is Poisson-distributed
# with mean 6
P2 = Participant(Behaviors.PoissonAgent(6), "Baseline condition")
# Create a model of a participant where their behavior is Poisson-distributed
# with mean 3
P3 = Participant(Behaviors.PoissonAgent(3), "Low condition")

# Create a test where you want the mean difference
# to be reliably different from 0 across all conditions
# through a basic non-parametric bootstrap
Test = DataTest(Tests.MeanDifferenceTest(BootSamples=1000))

# Create an experiment with all child models and the bootstrap test
MyExp = Experiment([P1, P2, P3], Test)

# See 2AFC_task for examples on what to do with the experiment object.

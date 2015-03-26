# Model a discrete measure of play time.
import Bunny

# Create a model of a child where their behavior is Poisson-distributed with mean 6
Child1 = Bunny.Participant(Bunny.ParticipantLibrary.Poisson(6),"Condition 1 child")
# Create a model of a child where their behavior is Poisson-distributed with mean 9
Child2 = Bunny.Participant(Bunny.ParticipantLibrary.Poisson(9),"Condition 2 child")
# Create a model of a child where their behavior is Poisson-distributed with mean 14
Child3 = Bunny.Participant(Bunny.ParticipantLibrary.Poisson(14),"Condition 3 child")

# Create a test where you want the mean difference
# to be reliably different from 0 across all conditions
# through a bootstrap
Test = Bunny.DataTest(Bunny.TestLibrary.MeanDifference(BootSamples=1000),"Bootstrap mean performance")

# Create an experiment with all child models and the bootstrap test
Experiment = Bunny.Experiment([Child1,Child2,Child3],Test,"Play experiment")

# Simulate experiments to find minimum sample size
Bunny.Hop(Experiment,limit=50,power=0.95,samples=5000,Verbose=True)
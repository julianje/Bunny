# Model a 2-alternative forced choice task.
# Expectation: 80% of participants will succeed.
# Analysis: a one-tailed binomial test.

# This file contains three sections:
# quick version shows the most efficient way to implement the experiment.
# argument version shows how to use arguments to tweak the parameters.
# detailed version shows a very inefficient way to implement the
# experiment, but it gives more insight into how Bunny works.

from Bunny import *

#################
# QUICK VERSION #
#################

# Create a binomial agent with probability of success = 0.8
Behavior = Participant(ParticipantLibrary.BinomialAgent(0.8))
# Create a DataTest that runs a binomial test
Test = DataTest(TestLibrary.Binomial("OT"))
# Create an experiment object
MyExperiment = Experiment(Behavior, Test, "2-AFC task")
# Explore relation between sample size and power
Explore(MyExperiment)
# Find a sample size given your power
MyExperiment.SetPower(0.95)
Hop(MyExperiment)
# Visualize your experiment's power given a sample size
MyExperiment.SetSampleSize(16)
Imagine(MyExperiment)

####################
# ARGUMENT VERSION #
####################

# Create a binomial agent with probability of success = 0.8
Behavior = Participant(ParticipantLibrary.BinomialAgent(0.8))
# Create a DataTest that runs a binomial test. However, mark the test as
# successfull if p<0.1, and set chance behavior to 0.25.
Test = DataTest(TestLibrary.Binomial(TestType="TT", alpha=0.1, Bias=0.25))
# Create an experiment object
MyExperiment = Experiment(Behavior, Test, "2-AFC task")
# Explore relation between sample size and power. Test sample sizes
# between 1 and 100
Explore(MyExperiment, lower=1, limit=100)
# Do the same as above, but save the image instead of displaying it
Explore(MyExperiment, lower=1, limit=100, filename="MyResults.pdf")
# Find a sample size given your power
MyExperiment.SetPower(0.95)
# Search for my appropriate sample size with a limit up to 200 participants.
# Ignore the experiment's power and instead use 0.85
# Run 500 simulations for each proposed sample size
# set Verbose to false, meaning that you will only see the final answer
# and not the search process.
Hop(MyExperiment, limit=200, power=0.85, samples=500, Verbose=False)
# Visualize your experiment's power given a sample size
MyExperiment.SetSampleSize(16)
# Visualize experiment's power using 100,000 simulations
Imagine(MyExperiment, samples=100000)

####################
# DETAILED VERSION #
####################

# Create a function that returns success with probabiliy = 0.8
BehaviorModel = ParticipantLibrary.BinomialAgent(0.8)
# Option 1: Create a participant object and send the behavior model as an
# argument
Behavior = Participant(BehaviorModel)
# Option 2: Create an empty participant object and add the behavior model later
Behavior = Participant()
Behavior.SetBehavior(BehaviorModel)

# Load a function that runs a binomial test
MyTest = TestLibrary.Binomial("OT")
# Option 1: Create a datatest object and send the DataTest as an argument
Test = DataTest(MyTest)
# Option 2: Create an empty DataTest object and add the binomial test later
Test = DataTest()
Test.SetTest(MyTest)

# Create an experiment object
MyExperiment = Experiment(Behavior, Test, "2-AFC task")
# See quick version section above for how examples on what you can do with
# the experiment object.

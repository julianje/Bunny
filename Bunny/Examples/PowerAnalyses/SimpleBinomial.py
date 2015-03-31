import Bunny

# LONG VERSION
# Create a participant object
Child = Bunny.Participant()
# Create a behavior model with 90% chance of success
Behavior = Bunny.ParticipantLibrary.Binomial(0.9)
# Attach the behavior model to the participant object
Child.SetBehavior(Behavior)

# Create a data test object
StatTest = Bunny.DataTest()
# Create a one-tailed binomial test
BinomialTest = Bunny.TestLibrary.Binomial("OT")
# Attach the test to the datatest file
StatTest.SetTest(BinomialTest)

# SHORT VERSION: You can do all of the above in two lines
Child = Bunny.Participant(Bunny.ParticipantLibrary.Binomial(0.9))
StatTest = Bunny.DataTest(Bunny.TestLibrary.Binomial("OT"))

# Now that you have a behavior model and a test, you can build an experiment

Experiment = Bunny.Experiment(Child, StatTest, "2-AFC task")

# Now you can explore your experiment
# Inspection will tell you you have no sample size or power
Bunny.Inspect(Experiment)

# You can look at the relation between these two through explore
Bunny.Explore(Experiment)

# If you want to know the power of a sample size
Experiment.AddSampleSize(16)
Bunny.Inspect(Experiment)  # Inspection will now calculate the power for you
# Take a closer look at the distribution you'll expect
Bunny.Imagine(Experiment)

# If you want to find the right sample size given power
Experiment.SetPower(0.99)  # I want a 99% change of experiment succeeding
Bunny.Hop(Experiment)

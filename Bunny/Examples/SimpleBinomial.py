import Bunny

# Run a simple binomial test
P = Bunny.Participant()
P.SetBehavior(Bunny.ParticipantLibrary.Binomial(0.8))
StatTest = Bunny.DataTest()
StatTest.SetTest(Bunny.Tests.BinomialTest("OT"))

# OR
P = Bunny.Participant(Bunny.ParticipantLibrary.Binomial(0.9))
StatTest = Bunny.DataTest(Bunny.TestLibrary.Binomial("OT"))
Exp = Bunny.Experiment(P,StatTest,"2AFC")

# Look at object
Bunny.Inspect(Exp) # Missing both sample size and power
Bunny.Hop(Exp) # Explore their relation

Exp.SetSampleSize(16)
Bunny.Inspect(Exp) # Bunny adds the power

Exp.ResetSampleSize()
Exp.SetPower(0.95)



Exp.RunExperiment()
import Bunny

# Run a simple binomial test
P = Bunny.Participant()
StatTest = Bunny.DataTest()
StatTest.SetTest(Bunny.Tests.BinomialTest("TT"))
P.SetBehavior(Bunny.Participants.Binomial(0.8))
Exp = Bunny.Experiment(P,StatTest,"Confused Participants")
Exp.SetSampleSize(16)
Exp.RunExperiment()
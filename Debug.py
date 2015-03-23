import Bunny

P = Bunny.Participant()
StatTest = Bunny.DataTest()
StatTest.SetTest(Bunny.Tests.BinomialTest("OT"))
P.SetBehavior(Bunny.Participants.Binomial(0.9))
Exp = Bunny.Experiment(P,StatTest,"SmartKids")
Bunny.Hop(Exp)


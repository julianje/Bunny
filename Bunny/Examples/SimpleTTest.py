import Bunny


# Run a t-test on two binomial sets (which you shouldn't really)
# Place holder until I add the gaussian participant model

# Option 1: Add both participants at once.
P = Bunny.Participant()
P.SetBehavior(Bunny.ParticipantLibrary.Binomial(0.8))
P2 = Bunny.Participant()
P2.SetBehavior(Bunny.ParticipantLibrary.Binomial(0.1))
StatTest = Bunny.DataTest()
StatTest.SetTest(Bunny.Tests.TTest())
Exp = Bunny.Experiment([P,P2],StatTest,"Confused Participants")
Exp.SetSampleSize(16)
Exp.RunExperiment()

# Option 2: Add participants one at a time
P = Bunny.Participant()
P.SetBehavior(Bunny.ParticipantLibrary.Binomial(0.8))
StatTest = Bunny.DataTest()
StatTest.SetTest(Bunny.Tests.TTest())
Exp = Bunny.Experiment(P,StatTest,"Confused Participants")
Exp.SetSampleSize(16)
# Add second participant
P2 = Bunny.Participant()
P2.SetBehavior(Bunny.ParticipantLibrary.Binomial(0.1))
Exp.AddParticipants(P2)
Exp.RunExperiment()
#Bunny.Hop(Exp)


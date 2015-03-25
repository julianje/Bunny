import Bunny


# Run an exact test on two binomial populations

# Option 1: Compressed way
P1 = Bunny.Participant(Bunny.ParticipantLibrary.Binomial(0.8))
P2 = Bunny.Participant(Bunny.ParticipantLibrary.Binomial(0.2))
StatTest = Bunny.DataTest(Bunny.TestLibrary.FisherExact())
Exp = Bunny.Experiment([P1,P2],StatTest)

# Option 2: Detailed way
P1 = Bunny.Participant()
P1.SetBehavior(Bunny.ParticipantLibrary.Binomial(0.8))
StatTest = Bunny.DataTest()
StatTest.SetTest(Bunny.Tests.FisherExact())
Exp = Bunny.Experiment(P1,StatTest,"Contrastive conditions")
P2 = Bunny.Participant()
P2.SetBehavior(Bunny.ParticipantLibrary.Binomial(0.2))
Exp.AddParticipants(P2)

# Things you can do with the experiment object:
Exp.SetSampleSize(16) # Add a sample size
Exp.GetPower() # Calculate experiment's sample size
Exp.CollectData() # Simulate one run of the experiment
Exp.Replicate(100) # Replicate experiment 100 times

# Things Bunny can do for you
Bunny.Hop(Exp) # Currently only supports sample-size exploration
Bunny.ExploreSampleSize(Exp,lower=10,limit=50,samples=1000) # Replicate 1000 times each experiment with sample sizes between lower and limit
Bunny.CalculateSampleSize(Exp,limit=40) # Find the sample size with the experiment's power.
Bunny.CalculateSampleSize(Exp,limit=40,power=0.99,samples=1000) # Find sample size for power=0.99; replicate each experiment one thousand times
# Run an exact test on two conditions
import Bunny

ConditionA = Bunny.Participant(Bunny.ParticipantLibrary.Binomial(0.8))
ConditionB = Bunny.Participant(Bunny.ParticipantLibrary.Binomial(0.2))

StatTest = Bunny.DataTest(Bunny.TestLibrary.FisherExact())
Exp = Bunny.Experiment(
    [ConditionA, ConditionB], StatTest, "Contrastive conditions")

# Low at power vs sample size graph
Bunny.Explore(Exp)

# Get sample size given power
Exp.SetPower(0.99)
Bunny.Hop(Exp)

# Get power given sample size
Exp.SetSampleSize(24)
Bunny.Inspect(Exp)  # Computes power

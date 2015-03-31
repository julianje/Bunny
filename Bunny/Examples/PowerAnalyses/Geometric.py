import Bunny

Effort = Bunny.Participant(
    Bunny.ParticipantLibrary.Poisson(20), "Effort condition")
NoEffort = Bunny.Participant(
    Bunny.ParticipantLibrary.Poisson(10), "No effort condition")

Effort = Bunny.Participant(Bunny.ParticipantLibrary.Empirical(
    [18, 30, 61, 23, 7, 6, 23, 11, 5, 9, 10, 11, 33, 28, 3, 50, 22]), "Effort condition")
NoEffort = Bunny.Participant(Bunny.ParticipantLibrary.Empirical(
    [12, 8, 3, 4, 2, 1, 9, 29, 11, 14, 24, 22, 1, 27, 12, 0]), "No effort condition")

Test = Bunny.DataTest(Bunny.TestLibrary.MeanDifference(BootSamples=1000))

Test = Bunny.DataTest(Bunny.TestLibrary.TTest())

Experiment = Bunny.Experiment(
    [Effort, NoEffort], Test, "Baby effort experiment")


Effort = Bunny.Participant(
    Bunny.ParticipantLibrary.Geometric(1.0 / 20), "Effort condition")
NoEffort = Bunny.Participant(
    Bunny.ParticipantLibrary.Geometric(1.0 / 10), "No effort condition")
Test = Bunny.DataTest(Bunny.TestLibrary.MeanDifference(BootSamples=1000))
Experiment = Bunny.Experiment(
    [Effort, NoEffort], Test, "Baby effort experiment")

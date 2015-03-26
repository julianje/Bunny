![Bunny](../Logos/bunny_longform.png)

# Using the libraries

### Behavior library

The participant library can be accesses in Bunny.ParticipantLibrary

##### Random agent

You can generate an agent that gives random numbers between 0 and 1 by calling

    Bunny.ParticipantLibrary.RandomAgent()

##### Binomial agent

Generate a binomial agent that returns correct or incorrect through

    Bunny.ParticipantLibrary.Binomial()

The function defaults to a bias of 0.5 (random guessing). Add a new bias through arguments

    Bunny.ParticipantLibrary.Binomial(0.8)

creates an agent that gets things right 80% of the time.

### TestLibrary

The test library can be accessed through Bunny.TestLibrary

##### Binomial test

The binomial test takes three parameters, whether it's one-tailed (OT) or two-tailed (TT), the significance level, and the bias you're testing again.

By default

	Bunny.TestLibrary.Binomial()

returns a two-tailed binomial function with significance at 0.05, testing against a bias of 0.5. You can change these parameters through

	Bunny.TestLibrary.Binomial(TestType,alpha,bias)

where TestType is one of the strings "OT" or "TT"

For example

	F=Bunny.TestLibrary.Binomial("OT",0.1,0.25)

creates a function F that runs a one-tailed binomial test which is significant if p<0.1, and is testing against a bias of 0.25

Calling the function

	F(Data)

returns a list. The first value is a boolean indicator whether the test succeeded, the second value is a list of the subtests (useful when the binomial test is running many separate conditions), and the third value is a list containing the p-values

The function will run a binomial test on each row of the Data array. The first indicator is only true when all tests succeeded, the second list is a detailed list of what happened in each condition.

##### Majority test

This function is a qualitative version of the binomial test, that only checks if the majority of participants are responding in accordance with your hypothesis. It's constructor doesn't take any arguments

	Bunny.TestLibrary.Majority()

##### T-test

T-tests are built through

    Bunny.TestLibrary.TTest()

and default to a significance level of 0.05. You send a new significant level as an argument:

    Bunny.TestLibrary.TTest(0.1)

The resulting function only works for Datasets with two rows. If the input has more than two rows the test will print an error message and fail.

##### Fisher exact test

Fisher exact tests are built through

    Bunny.TestLibrary.FisherExact()

Like the T-test function. Fisher exact only works for datasets with two conditions.

# Adding new functions to libraries

### Pariticipant library

### Test library
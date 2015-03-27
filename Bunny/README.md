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

##### Poisson agent

Input is lambda

    F=Bunny.ParticipantLibrar.Poisson(L=5)

you can manually override it later

    F(Lambda=1)

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

##### Mean Difference

Mean difference checks that the mean in each condition is different from the mean of all other conditions. This is done by bootstrapping the mean differnce between each pair of conditions. You can input the number of bootstrap samples as an argument (Defaulted to 10,000)

    F=Bunny.TestLibrary.MeanDifference(BootSamples=5000,inputalpha=0.05)

You can modify the number of bootstrap samples and the significance level through arguments:

    F(Data,Samples=5000,alpha=0.1)

##### Binomial with Control

Succeeds when first test is significant under a binomial test but second condition is not.

    Bunny.TestLibrary.BinomialWithControl(TestType="TT",alpha=0.05,Bias=0.5)

Where TestType can be two-tailed ("TT") or one-tailed ("OT")

# Adding new functions to libraries

### Pariticipant library

A model in the participant library should be a function that returns a new function. This function can take input arguments but they must have a default value. The output should be a single number. Support for participant models that return more than one number is easy to implement, but it's not clear whether it is useful

### Test library

Bunny's procedures pack simulation results into numpy arrays. A new test in the test library should be a function that returns a new test function. The test function's first argument is always the data: a numpy array where each row is a different condition and each entry is a simulation of a participant. The function can take more input arguments after the Data, but they should all have preset values. A statistical should always return a list with the first object being a boolean indicator of whether the test was satisfied or not (this is necessary for computing power). More details about the test can follow after that.

Preferably, the test function should know how to adapt to multiple conditions. For example, the library's binomial test will run the test on any condition it finds. If the data has five conditions, the function's output is a list where the first object is True only when all conditions were significant, and 0 otherwise. The second item in the list is a sublist marking which conditions succeeded and which didn't. The last item in the list is a sublist with the p-values.

This kind of support should also be added to test that compare between conditions. For example, when the MeanDifference test finds more than two conditions it computes the test on all possible pairs of conditions.
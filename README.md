![Bunny](Logos/bunny_longform.png)

# About

Bunny is a monte carlo power analyses (MCPA) package for python. Bunny takes a theory of how you think humans will behave (called a Participant) and the analysis you plan to use on the data (called a DataTest) and helps you understand your experiment by simulating the process of collecting and analyzing your data thousands of times. Bunny can help you determine your experiment's power, the sample size you need, or simply to understand how different tests affect your study.

Bunny is simple. Here is a complete working example showing how to calculate the power for a two-alternative forced choice task:

	from Bunny import *
	ChildModel = Participant(Behaviors.BernoulliAgent(0.8))
	MyTest = DataTest(Tests.BinomialTest())
	MyExperiment = Experiment(ChildModel, MyTest)
	Hop(MyExperiment)

# Usage

Bunny's main objects are Experiments, a combination of a formal theory of how you think participants will behave and a statistical procedure you plan to use on your data. If you use Bunny's libraries, you can build an Experiment in as little as three lines of code. Implementing your own is also simple. Once you have an experiment, Bunny can ...

Calculate its power, given the sample size

	Inspect(Experiment)

Help you visualize the experiment's power

	Imagine(Experiment)

Find the sample size you need given a power

	Experiment.SetPower(0.95)
	Hop(Experiment)

Or explore the relationship between sample size and power

	Explore(Experiment)

# Get started

To get started visit the [wiki](https://github.com/julianje/Bunny/wiki) or look at the examples.

# Installation

To install download the source code and on a terminal run

	python setup.py install
	pip uninstall Bunny

# License

Bunny is available through an MIT license.

# TODO

* Support finding parameters in behavior models given a desired power and sample size

* Allow model objects to be saved.
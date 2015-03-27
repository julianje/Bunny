![Bunny](Logos/BunnyLogo.png)

# About

Bunny is a python package that does simulation-based power analyses. Meta-analyses pre-registrations coming soon.

# Installation

To install download the source code and on a terminal run

	python setup.py install
	pip uninstall Bunny

# Main usage

### Power analysis

Given an experiment (See example folder on how to build experiments), Bunny can ...

Calculate its power, given the sample size

	Experiment.SetSampleSize(30)
	Bunny.Inspect(Experiment)

Search for the smallest sample size with the desired power

	Experiment.SetPower(0.95)
	Bunny.Hop(Experiment)

Or explore the relationship between sample size and power

	Bunny.Explore(Experiment)

# Experiment objects

Experiment objects are a combination of one (or many) models of behavior (e.g., binomial behavior with 90% chance of giving right answer) and some processing you'll do with the data (e.g., a two-tailed binomial test).

Bunny comes with two libraries with many common models of participants (in Bunny.ParticipantLibrary) and with common statistical tests and procedures (Bunny.TestLibrary).

The easiest way to understand how this works is by looking at the examples.
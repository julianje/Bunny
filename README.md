![Bunny](Logos/BunnyLogo.png)

# About

Bunny is a python package that does simulation-based power analyses. The ability to do meta-analyses and to pre-register designs is being implemented.

# Installation

To install download the source code and on a terminal run

	python setup.py install
	pip uninstall Bunny

# Main usage

### Power analysis

Given an experiment object (See below on how to build experiments), Bunny can ...

Calculate its power, given the sample size

	Experiment.SetSampleSize(30)
	Bunny.Inspect(Experiment)

Search for the smallest sample size with the desired power

	Experiment.SetPower(0.95)
	Bunny.Hop(Experiment)

Or help you explore the relationship between sample size and power

	Bunny.Explore(Experiment)

### Meta analysis

Coming soon

### Pre-registration

Coming soon

# Creating experiment objects

### Experiment descriptions

Coming soon

### Through Bunny libraries

Bunny comes with two libraries with common statistical tests (Bunny.TestLibrary) and models of participants (Bunny.ParticipantLibrary)

### Manually

Coming soon

# Known issues:

Bunny's pre-registration uses openssl. If you're using anaconda. You might get the warning:

WARNING: can't open config file: /opt/anaconda1anaconda2anaconda3/ssl/openssl.cnf

This is a known issue: https://github.com/ContinuumIO/anaconda-issues/issues/137
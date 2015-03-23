#Bunny
______

## About

Bunny is a python package that lets you "hop" around different dimensions experiments to find the best design.

## How it works

Bunny has three kinds of objects: Participants, experiments, and statistical tests.

Experiments contain meta-data about the experiment: Sample size, age range, measure type, number of conditions, etc.

Participant objects contain a model of how participants behave. Thus, hypotheses are formalized as participants.

Test objects contain analysis methods for participants in the experiment.

## Vision

Bunny's main functions will be Hop and Inspect.

Inspect will take a full experiment, participant model, and test and compute different properties of the experiment through simulation (e.g., power).

Hop will take an experiment, participant model, and test, and search for missing values. It will then simulate runs using different values to help find the best design. For example, if an experiment object doesn't have a sample size. Bunny will simulate the experiment for different sample sizes.


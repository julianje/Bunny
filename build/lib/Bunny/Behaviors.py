# -*- coding: utf-8 -*-

"""
Behaviors library contains a set of common models of behavior.
"""

__license__ = "MIT"

import random
import numpy as np


def RandomAgent():
    """
    Create a function that returns floats between 0 and 1.

    Args:
        None

    Returns:
        Function

    >> MyFunction = Behaviors.RandomAgent()
    """
    def F():
        return random.random()
    return F


def BernoulliAgent(Bias=0.5):
    """
    Create a function that returns 1 with a certain probability and 0 otherwise.

    Args:
        Bias (float): Probability of success

    Returns:
        Function

    >> MyFunction = Behaviors.BernoulliAgent(0.5)
    """
    def F(B=Bias):
        return 1 if random.random() < B else 0
    return [F, "Bernoulli behavior"]


def BernoulliInclusionAgent(Bias=0.5, Pinc=0.5):
    """
    Create a function that returns 1 with a certain probability and 0 otherwise.
    However, if function returns 0 it has to pass an inclusion with probability Pinc

    Intuitively, this models a population where a proportion of participants master the task (they respond correctly and pass inclusion).
    Participants who don't understand the task, will likely be stopped by the inclusion question, however, there is a chance that they wil pass it by chance.

    Args:
        Bias (float): Probability of success
        Pinc (float): Probability of passing inclusion

    Returns:
        Function

    >> MyFunction = Behaviors.BernoulliInclusionAgent(0.8,0.5)
    """
    def F(B=Bias):
        return 1 if random.random() < (B + (1-B)*Pinc/2.0) else 0
    return [F, "Bernoulli with inclusion"]


def BinomialAgent(N, Bias):
    """
    Create a function that returns the sum of n independent bernoulli samples

    Args:
        N (int): number of samples
        Bias (float or list of floats): Probability of success. Or a list of length N indicating each probability of success

    Returns:
        Function

    >> MyFunction = Behaviors.BinomialAgent(2,0.8) # Two questions, each with 0.8 probability of success
    >> MyFunction = Behaviors.BinomialAgent(2,[0.6,0.8]) # Questions have 0.6 and 0.8 probabilities of success, respectively.
    """
    if isinstance(Bias, list):
        if len(Bias) != N:
            print "ERROR: List of biases does not match number of questions."
            return None

        def F():
            Responses = [1 if random.random < Bias[i] else 0 for i in range(N)]
            return sum(Responses)

    else:
        def F(B=Bias):
            Responses = [1 if random.random < B else 0 for i in range(N)]
            return sum(Responses)
    return [F, "Binomial behavior"]


def PoissonAgent(L=1):
    """
    Create a function that returns a sample from a poisson distribution.

    Args:
        L (float): Mean of the distribution

    Returns:
        Function

    >> MyFunction = Behaviors.PoissonAgent(4)
    """
    def F(Lambda=L):
        # Last zero is because np returns an array.
        return np.random.poisson(Lambda, 1)[0]
    return [F, "Poisson behavior"]


def EmpiricalAgent(List):
    """
    Create a function defined from an empirical sample.

    Args:
        List (list): List can be either a list of numbers, or a list of lists.
        when the List only contains numbers, the function randomly samples from that list.
        If the List is a lists of lists, the function interprets the first value of each list
        as an outcome and the second value as the number of observations of that value.

    Returns:
        Function

    >> MyFunction = Behaviors.EmpiricalAgent([1,3,3,4,5]) # Randomly sample from these numbers

    >> MyFunction = Behaviors.EmpiricalAgent([0,1,1,1]) # Randomly sample from these numbers

    >> MyFunction = Behaviors.EmpiricalAgent([[1,3],[0,1]]) # Equivalent to above
    """
    Lists = [isinstance(i, list) for i in List]
    # If you got a list of lists
    if sum(Lists) == len(Lists):
        # Repeat each item by the number of observations
        NewList = [[i[0]] * i[1] for i in List]
        # Flatten list
        List = [item for sublist in NewList for item in sublist]

    def F():
        return random.choice((List))
    return [F, "Empirically set behavior"]


def GeometricAgent(param):
    """
    Create a function that returns a sample from a geometric distribution.

    Args:
        param (float): Geometric distributions' parameter. The mean of the distribution is 1/param

    Returns:
        Function

    >> MyFunction = Behaviors.GeometricAgent(4)
    """
    def F(p=param):
        return np.random.geometric(p)
    return [F, "Geometric distribution"]


def NormalAgent(mean, sd=1):
    """
    Create a function that returns a sample from a normal distribution.

    Args:
        mean (float): Distribution's mean
        sd (float): Distribution's standard deviation

    Returns:
        Function

    >> MyFunction = Behaviors.NormalAgent(5,1)
    """
    def F(mean=mean, sd=sd):
        return np.random.normal(mean, sd)
    return [F, "Normal distribution"]

# -*- coding: utf-8 -*-

"""
ParticipantLibrary contains a set of common models of behavior.
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

    >> MyFunction = ParticipantLibrary.RandomAgent()
    """
    def F():
        return random.random()
    return F


def BinomialAgent(Bias=0.5):
    """
    Create a function that returns 1 with a certain probability and 0 otherwise.

    Args:
        Bias (float): Probability of success

    Returns:
        Function

    >> MyFunction = ParticipantLibrary.BinomialAgent(0.5)
    """
    def F(B=Bias):
        return 1 if random.random() < B else 0
    return [F, "Binomial behavior", "Unit"]


def PoissonAgent(L=1):
    """
    Create a function that returns a sample from a poisson distribution.

    Args:
        L (float): Mean of the distribution

    Returns:
        Function

    >> MyFunction = ParticipantLibrary.PoissonAgent(4)
    """
    def F(Lambda=L):
        # Last zero is because np returns an array.
        return np.random.poisson(Lambda, 1)[0]
    return [F, "Poisson behavior", "Real"]


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

    >> MyFunction = ParticipantLibrary.EmpiricalAgent([1,3,3,4,5]) # Randomly sample from these numbers

    >> MyFunction = ParticipantLibrary.EmpiricalAgent([0,1,1,1]) # Randomly sample from these numbers

    >> MyFunction = ParticipantLibrary.EmpiricalAgent([[1,3],[0,1]]) # Equivalent to above
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
    return [F, "Empirically set behavior", "None"]


def GeometricAgent(param):
    """
    Create a function that returns a sample from a geometric distribution.

    Args:
        param (float): Geometric distributions' parameter. The mean of the distribution is 1/param

    Returns:
        Function

    >> MyFunction = ParticipantLibrary.PoissonAgent(4)
    """
    def F(p=param):
        return np.random.geometric(p)
    return [F, "Geometric distribution", "Real"]
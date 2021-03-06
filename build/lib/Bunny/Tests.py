# -*- coding: utf-8 -*-

"""
Tests library contains a set of common statistical procedures.
"""

__license__ = "MIT"

from TestResult import *
import scipy.stats
import scipy.misc
import numpy as np


def BinomialTest(TestType="TT", alpha=0.05, Bias=0.5):
    """
    Create a binomial test.

    Args:
        TestType (str): Must be 'OT' or 'TT' for one-tailed and two-tailed respectively
        alpha (float): threshold at which the test succeeds
        Bias (float): Weight of null hypothesis.

    Returns:
        Function

    >> MyFunction = Tests.BinomialTest("OT",0.05,0.5)
    """
    if TestType == "TT":
        def F(Data):
            TestName = "Two-tailed binomial test"
            Conditions = Data.shape[0]
            KeyStats = [Data[i].sum() * 1.0 / Data.shape[1]
                        for i in range(Conditions)]
            pvals = [scipy.stats.binom_test(
                Data[i].sum(), Data.shape[1], Bias) for i in range(Conditions)]
            results = [i < alpha for i in pvals]
            final = 1 if sum(results) == Conditions else 0
            return TestResult(final, TestName, results, KeyStats, pvals)
    elif TestType == "OT":
        def F(Data):
            TestName = "One-tailed binomial test"
            Conditions = Data.shape[0]
            KeyStats = [Data[i].sum() * 1.0 / Data.shape[1]
                        for i in range(Conditions)]
            pvals = [scipy.stats.binom.sf(
                Data[i].sum() - 1, Data.shape[1], Bias) for i in range(Conditions)]
            results = [i < alpha for i in pvals]
            final = 1 if sum(results) == Conditions else 0
            return TestResult(final, TestName, results, KeyStats, pvals)
    else:
        print "Error: Binomial test must be one-tailed (OT) or two-tailed (TT)."
        return None
    return F


def MajorityTest():
    """
    Create a qualitative majority test. The test succeeds if the majority of participants respond correctly and fails otherwise.

    Args:
        None

    Returns:
        Function

    >> MyFunction = Tests.MajorityTest()
    """
    def F(Data):
        TestName = "Testing if majority of data agrees with prediction"
        Conditions = Data.shape[0]
        results = [
            Data[i].sum() > Data.shape[1] * 1.0 / 2 for i in range(Conditions)]
        final = 1 if sum(results) == Conditions else 0
        return TestResult(final, TestName, results)


def TTest(alpha=0.05):
    """
    Create a T-Test

    Args:
        alpha (float): Threshold at which test succeeds

    Returns:
        Function

    >> MyFunction = Tests.TTest()
    """
    def F(Data):
        TestName = "T-Test"
        if Data.shape[0] != 2:
            print "Error: T-test needs exactly two conditions"
            return None
        pval = scipy.stats.ttest_ind(Data[0], Data[1])[1]
        return TestResult(1, TestName) if pval <= alpha else TestResult(0, TestName)
    return F


def FisherExactTest(alpha=0.05):
    """
    Create a Fisher exact test. Function automatically checks if it can analyze input data.

    Args:
        alpha (float): Threshold at which test succeeds

    Returns:
        Function

    >> MyFunction = Tests.FisherExactTest()
    """
    def F(Data):
        TestName = "Fisher exact test"
        if Data.shape[0] != 2:
            print "Error: Fisher exact test needs exactly two conditions"
            return None
        V1 = Data[0].sum(), Data.shape[1] - Data[0].sum()
        V2 = Data[1].sum(), Data.shape[1] - Data[1].sum()
        pval = scipy.stats.fisher_exact([V1, V2])[1]
        return TestResult(1, TestName) if pval <= alpha else TestResult(0, TestName)
    return F


def BootstrapMeanTest(BootSamples=10000, criticalvalue=0.5, inputalpha=0.05):
    """
    Create a function that bootstraps the average value of each condition
    Function succeeds if 95 confidence interval does not value provided.

    Args:
        BootSamples (int): Number of samples for bootstrap
        criticalvalue (float): value that bootstrapped CI should avoid.
        intputalpha (float): percentage outside confidence interval

    Returns:
        Function

    >> MyFunction = Tests.BootstrapMeanTest()
    """
    def F(Data, Samples=BootSamples, criticalvalue=criticalvalue, inputalpha=intputalpha):
        TestName = "Bootstrap mean value"
        Conditions = Data.shape[0]
        Size = Data.shape[1]
        outcome = []
        for Condition in range(Conditions):
            C = Data[Condition]
            indices = np.random.randint(0, Size, (Samples, Size))
            statistics = np.mean(C[indices], 1)
            statistics = np.sort(statistics)
            lowerbound = statistics[int((alpha / 2.0) * Samples)]
            upperbound = statistics[int((1 - alpha / 2.0) * Samples)]
            if (lowerbound < criticalvalue and upperbound < criticalvalue) or (lowerbound > criticalvalue and upperbound > criticalvalue):
                outcome.append(1)
            else:
                outcome.append(0)
        final = 1 if sum(outcome) == len(outcome) else 0
        return TestResults(final, TestName, outcome)
    return F


def MeanDifferenceTest(BootSamples=10000, criticalvalue=0, inputalpha=0.05):
    """
    Create a function that bootstraps the difference in the means of two conditions.
    Function succeeds if 95 confidence interval does not cross the critical value.

    Args:
        BootSamples (int): Number of samples for bootstrap
        criticalvalue (float): Value that confidence interval should not contain
        inputalpha (float): Threshold at which test succeeds

    Returns:
        Function

    >> MyFunction = Tests.MeanDifferenceTest()
    """
    def F(Data, Samples=BootSamples, criticalvalue=criticalvalue, alpha=inputalpha):
        TestName = "Bootstrapped difference between means"
        Conditions = Data.shape[0]
        if Conditions < 2:
            print "Error: MeanDifference test needs at least two conditions"
            return None
        Size = Data.shape[1]
        outcome = []
        for Condition1 in range(Conditions - 1):
            for Condition2 in range(Condition1 + 1, Conditions):
                # Compare the two conditions.
                C1 = Data[Condition1]
                C2 = Data[Condition2]
                # Generate resampling indexes for bootstrap
                indexes = np.random.randint(0, Size, (Samples, Size))
                # Get the difference in means for each sample.
                statistics = np.mean(C1[indexes], 1) - np.mean(C2[indexes], 1)
                # re-sort
                statistics = np.sort(statistics)
                # Get (1-alpha)% confidence interval
                lowerbound = statistics[int((alpha / 2.0) * Samples)]
                upperbound = statistics[int((1 - alpha / 2.0) * Samples)]
                if (lowerbound < criticalvalue and upperbound < criticalvalue) or (lowerbound > criticalvalue and upperbound > criticalvalue):
                    outcome.append(1)
                else:
                    outcome.append(0)
        # Once done, check if all tests succeeded
        final = 1 if sum(outcome) == len(outcome) else 0
        return TestResult(final, TestName, outcome)
    return F


def BinomialWithControlTest(TestType="TT", alpha=0.05, Bias=0.5):
    """
    Create a function that runs a binomial test on two conditions. Test succeeds only when first condition succeeds under a binomial and the second test fails.

    Args:
        TestType (str): Must be 'OT' or 'TT' for one-tailed and two-tailed respectively
        alpha (float): threshold at which the test succeeds
        Bias (float): Weight of null hypothesis.

    Returns:
        Function

    >> MyFunction = Tests.BinomialWithControlTest()
    """
    print "Creating binomial with control. Make sure the test model is input before the control model in the experiment object."
    if TestType == "TT":
        TestName = "First condition with two-tailed binomial test, and second condition as control."

        def F(Data):
            Conditions = Data.shape[0]
            if Conditions != 2:
                print "Error: BinomialWithControl needs exactly two conditions"
                return None
            KeyStats = [Data[i].sum() * 1.0 / Data.shape[1]
                        for i in range(Conditions)]
            pvals = [scipy.stats.binom_test(
                Data[i].sum(), Data.shape[1], Bias) for i in range(Conditions)]
            results = [i < alpha for i in pvals]
            final = 1 if (results[0] == 1 and results[1] == 0) else 0
            return TestResult(final, TestName, results, KeyStats, pvals)
    elif TestType == "OT":
        TestName = "First condition with one-tailed binomial test, and second condition as control."

        def F(Data):
            Conditions = Data.shape[0]
            if Conditions != 2:
                print "Error: BinomialWithControl needs exactly two conditions"
                return None
            KeyStats = [Data[i].sum() * 1.0 / Data.shape[1]
                        for i in range(Conditions)]
            pvals = [scipy.stats.binom.sf(
                Data[i].sum() - 1, Data.shape[1], Bias) for i in range(Conditions)]
            results = [i < alpha for i in pvals]
            final = 1 if (results[0] == 1 and results[1] == 0) else 0
            return TestResult(final, TestName, results, KeyStats, pvals)
    else:
        print "Error: Binomial test must be one-tailed (OT) or two-tailed (TT)."
        return None
    return F

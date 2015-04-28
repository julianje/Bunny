# -*- coding: utf-8 -*-

"""
BunnyFunctions contains a set of high level functions to manipulate experiment objects.
"""

__license__ = "MIT"

from Experiment import *
from Participant import *
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import sys
import time


def Explore(Exp, lower=15, limit=35, filename=None):
    """
    Plot an experiment's power as a function of the sample size.

    Args:
        Exp (Experiment): Experiment object to use (see Experiment class)

        lower (int) : Smallest sample size to consider.

        limit (int) : Highest sample size to consider.

        filename (str) : Filename. If provided, the plot is saved instead of printed.

    Returns:
        None

    >> Explore(MyExperiment)

    >> Explore(MyExperiment,10,50,"Results.png")

    """
    if not Exp.Validate():
        print "Error: Experiment failed validation."
        return None
    print "Exploring sample sizes ... "
    res = ExploreSampleSize(Exp, lower, limit)
    PlotPowerSamples(res, filename)


def Hop(Exp, limit=100, power=None, samples=10000, Verbose=True):
    """
    Determine an experiment's sample size through binary search.

    Args:
        Exp (Experiment): Experiment object to use (see Experiment class)

        limit (int) : Highest sample size to consider.

        power (float) : Experiment's power. If none is provided then the experiment object's power is used. If neither are determined, power is set to 0.95

        samples (int) : Number of simulations for each sample size proposal.

        Verbose (bool) : Run function silently or not.

    Returns:
        [Sample size, Power] (list) : First item shows smallest sample size and second item shows the corresponding power.

    >> Hop(MyExperiment)

    >> Hop(MyExperiment, limit=30, power=0.99, samples=100, Verbose=False)

    """
    if power is None:
        if Exp.Power is None:
            if Verbose:
                print "Setting power to 0.95."
            power = 0.95
        else:
            power = Exp.Power
    if (power >= 1 or power <= 0):
        if Verbose:
            print "Error: Power has to be between 0 and 1."
        return None
    if Verbose:
        sys.stdout.write("Power: " + str(power) + "\nLimit: " +
                         str(limit) + "\nReplications per proposal: " + str(samples) + "\n")
    lower = 1
    upper = limit
    current = (upper - lower) / 2 + lower
    if Verbose:
        print "Searching for your sample size..."
    underpowered = True
    while True:
        sys.stdout.write(
            "Simulating with " + str(current) + " participants per condition... ")
        sys.stdout.flush()
        Exp.SetSampleSize(current)
        p = Exp.GetPower(samples)
        if Verbose:
            sys.stdout.write("Power=" + str(p) + "\n")
        if p < power:
            # If experiment is underpowered
            if (upper - lower) <= 1:
                Exp.SetSampleSize(upper)
                Exp.UpdatePower()
                # Check if Hopping worked
                if underpowered:
                    print "Warning: Failed to converge. Bunny.Hop() assumes that the pattern your DataTest searches for exists.\nIf you're using a null model consider using Bunny.Explore() instead.\nIf you're using a non-random model then increase the search limit by sending a number greater than 100 as the second paramter of Bunny.Hop()"
                return [upper, Exp.Power]
            lower = current
            current = (upper - lower) / 2 + lower
        else:
            underpowered = False
            if (upper - lower) <= 1:
                Exp.SetSampleSize(lower)
                Exp.UpdatePower()
                # If you're here then at least one instance was over
                return [lower, Exp.Power]
            upper = current
            current = (upper - lower) / 2 + lower


def Inspect(Exp, RecomputePower=False):
    """
    Print experiment details. Automatically computes sample size or power if possible.

    Args:
        Exp (Experiment): Experiment object to use (see Experiment class)

        RecomputePower (bool) : If the experiment object has a power stored RecomputePower determines if it should be recomputed.

    Returns:
        None

    >> Inspect(MyExperiment)

    >> Inspect(MyExperiment,True)

    """
    sys.stdout.write("\nValidating experiment...")
    if Exp.Validate():
        sys.stdout.write(" SUCCESS\n\n")
    sys.stdout.write("Experiment name: " + str(Exp.Name) + "\n")
    sys.stdout.write("Statistical test: " + str(Exp.StatTest.Name) + "\n\n")
    if not Exp.SampleSize is None:
        sys.stdout.write("Sample size: " + str(Exp.SampleSize) + "\n")
    else:
        sys.stdout.write(
            "No sample size associated. Checking if I can estimate it... ")
        if not Exp.Power is None:
            sys.stdout.write(
                "Yes.\nComputing smallest sample size needed... \n\n")
            Hop(Exp, limit=100, power=Exp.Power, samples=5000, Verbose=False)
            sys.stdout.write("Sample size: " + str(Exp.SampleSize) + "\n")
        else:
            sys.stdout.write(
                "No.\nUse Bunny.Explore(Experiment) to see the relation between sampe size and power.\n")
    if not Exp.Power is None:
        if RecomputePower is True:
            Exp.UpdatePower()
            sys.stdout.write(
                "Power: " + str(Exp.Power) + " (Freshly computed!)\n")
        else:
            sys.stdout.write(
                "Power: " + str(Exp.Power) + " (Call Bunny.Inspect(True) to recompute power)\n")
    else:
        sys.stdout.write("No power. Checking if I can estimate it... ")
        if not Exp.SampleSize is None:
            sys.stdout.write("Yes.\n\n")
            Exp.UpdatePower()
            sys.stdout.write("Power: " + str(Exp.Power) + "\n")
        else:
            sys.stdout.write(
                "No.\nUse Bunny.Explore(Experiment) to see the relation between sampe size and power.\n\n")


def Imagine(Exp, samples=10000):
    """
    Plot the key statistics of a simulation along with the decision.

    Args:
        Exp (Experiment): Experiment object to use (see Experiment class)

        samples (int) : Number of simulations to run

    Returns:
        None

    >> Imagine(MyExperiment)

    >> Imagine(MyExperiment,samples=10000)

    """
    if Exp.SampleSize is None:
        print "ERROR: Need a sample size!"
        return None
    if len(Exp.Participants) == 1:
        Res = Exp.Replicate(samples)
        Stats = [Res[i].keystats[0] for i in range(samples)]
        Decisions = [Res[i].aggregatedecision for i in range(samples)]
        SuccessTrials_indices = [i for i, x in enumerate(Decisions) if x == 1]
        FailedTrials_indices = [i for i, x in enumerate(Decisions) if x == 0]
        SuccessTrials = [Stats[i] for i in SuccessTrials_indices]
        FailedTrials = [Stats[i] for i in FailedTrials_indices]
        Power = sum(Decisions) * 1.0 / len(Decisions)
        pylab.figure()
        n, bins, patches = pylab.hist([SuccessTrials, FailedTrials], 10, histtype='bar', stacked=True, color=[
                                      'green', 'red'], label=['Success', 'Fail'])
        pylab.legend()
        pylab.xlabel('Statistic value')
        pylab.ylabel('Number of observations')
        pylab.title(str(samples) + ' simulations with ' +
                    str(Exp.SampleSize) + ' participants each. Power = ' + str(Power))
        pylab.show()
    else:
        print "Bunny.Imagine(Exp) only works for experiments with one condition"

# Mid-level functions


def ExploreSampleSize(Exp, lower=1, limit=-1, samples=10000):
    """
    Calculate an experiment's power for a range of sample sizes

    This is the main function that Explore() uses to generate the data.

        .. warning::

           This function is for internal use only.

    Args:
        Exp (Experiment): Experiment object to use (see Experiment class)

        lower (int) : Smallest sample size to consider.

        limit (int) : Highest sample size to consider. If limit=-1 then samples sizes between 15 and 35 are tested

        samples (int) : Number of simulations per proposal.

    Returns:
        [[Sample sizes], [Power]] (list) : [Sample sizes] is a list of sample sizes and [Power] is has the power associated with each sample size.

    >> ExploreSampleSize(MyExperiment)

    >> ExploreSampleSize(MyExperiment,10,50,10000)

    """
    if limit == -1:
        print "No limit specified. Testing samples between 15 and 35 ..."
        lower = 15
        limit = 35
    Power = []
    if lower > limit:
        print "Error: Lower limit is higher than upper limit"
        return None
    print "Estimating time ...."
    SampleSize = range(lower, limit + 1)
    CurrSampleSize = Exp.SampleSize
    for i in SampleSize:
        if i == lower:
            start = time.time()
        Exp.SetSampleSize(i)
        Power.append(Exp.GetPower(samples))
        if i == lower:
            end = time.time()
            secs = (end - start) * len(SampleSize)
            sys.stdout.write("This will take at least ")
            if (secs < 60):
                sys.stdout.write(str(round(secs, 2)) + " seconds.\n")
            else:
                mins = secs * 1.0 / 60
                if (mins < 60):
                    sys.stdout.write(str(round(mins, 2)) + " minutes.\n")
                else:
                    hours = mins * 1.0 / 60
                    sys.stdout.write(str(round(hours, 2)) + " hours.\n")
    print "Done!"
    # Restore experiment object.
    if CurrSampleSize is None:
        Exp.ResetSampleSize()
        Exp.ResetPower()
    else:
        Exp.SetSampleSize(CurrSampleSize)
        Exp.UpdatePower(samples)
    return [SampleSize, Power]


def PlotPowerSamples(Samples, Filename=None):
    """
    Plot sample size and power relation

    This is the function Explore() uses to produce its plots.

        .. warning::

           This function is for internal use only.

    Args:
        Samples (list): Samples should contain two lists. The first list contains sample sizes and second list contains the power associated with each sample size. ExploreSampleSize produces the output that can be sent directly to this function.

        Filename (str) : When the function receives a filename, it saves the resulting plot instead of displaying it.

    Returns:
        None

    >> res = ExploreSampleSize(Exp, 15, 20)
    >> PlotPowerSamples(res)

    """
    plt.clf()
    plt.plot(Samples[0], Samples[1], 'bo', Samples[0], Samples[1], 'k')
    plt.xlabel('Sample Size')
    plt.ylabel('Power')
    plt.title('Relation between sample size and power')
    plt.grid(True)
    if Filename is None:
        plt.show()
    else:
        plt.savefig(Filename)

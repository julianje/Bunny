# -*- coding: utf-8 -*-

"""
TestResult objects store DataTest results and makes them easier to manipulate.

This class is designed for internal code usage only.
"""

__license__ = "MIT"


class TestResult(object):

    def __init__(self, aggregatedecision=None, TestName=None, decisions=None, keystats=None, pvals=None):
        """
        Create a TestResult object object.

        .. warning::

           This function is for internal use only.

        Args:
            aggregatedecision (bool): Indicates if on aggregate the Test succeeded.

            TestName (str): Name of test that was used.

            TestName (str): Name of test that was used.

            decisions (list): List of individual decisions for each condition in the experiment.

            keystats (list): List of key statistical values given by the DataTest object

            pvals (list): List of p-values for each condition (if using NHST)

        Returns:
            TestResult object
        """
        self.aggregatedecision = aggregatedecision
        self.decisions = decisions
        self.keystats = keystats
        self.pvals = pvals
        self.testname = TestName

    def HasPvals(self):
        """
        Check if TestResult object has p-values associated with it

        .. warning::

           This function is for internal use only.

        Args:
            None

        Returns:
            Bool
        """
        return 0 if self.pvals is None else 0

    def HasKeyStats(self):
        """
        Check if TestResult object has key statistics associated with it

        .. warning::

           This function is for internal use only.

        Args:
            None

        Returns:
            Bool
        """
        return 0 if self.keystats is None else 1

    def Display(self, Full=True):
        """
        Print object attributes.

        .. warning::

           This function is for internal use only.

        Args:
            Full (bool): When set to False, function only prints attribute names. Otherwise, it also prints its values.

        Returns:
            standard output summary
        """
        if Full:
            for (property, value) in vars(self).iteritems():
                print property, ': ', value
        else:
            for (property, value) in vars(self).iteritems():
                print property

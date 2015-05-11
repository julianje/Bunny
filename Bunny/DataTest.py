# -*- coding: utf-8 -*-

"""
DataTest objects wrap a statistical procedure with supporting functions.
"""

__license__ = "MIT"


class DataTest(object):

    def __init__(self, Test=None, Name="DataTest_Object"):
        """
        Create a DataTest object.

        Args:
            Test (function): A statistical procedure

            Name (str): Name of test.

        Returns:
            DataTest object
        """
        self.Test = Test
        self.Name = Name

    def SetTest(self, Test):
        """
        Insert a test function to DataTest.

        Args:
           Test (function): A statistical procedure

        Returns:
            None

        >> MyAnalysis.SetTest(Tests.BinomialTest())
        """
        self.Test = Test

    def RunTest(self, Data):
        """
        Check that DataTest object is usable and execute the test on a dataset.

        .. warning::

           This function is for internal use only.

        """
        if not self.Validate():
            return None
        return self.Test(Data)

    def Validate(self):
        """
        Check that DataTest object works.

        .. warning::

           This function is for internal use only.

        Args:
            None

        Returns:
            bool
        """
        if self.Test is None:
            print "ERROR. DataTest object doesn't have a statistical test.\nUse DataTest.SetTest()"
            return 0
        elif not hasattr(self.Test, '__call__'):
            print "ERROR. Cannot call data function"
        else:
            return 1

    def SetName(self, Name):
        """
        Add name to DataTest object

        Args:
            Name (str): Name to assign

        Returns:
            None

        >> MyAnalysis.SetName("My Analysis")
        """
        self.Name = Name

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

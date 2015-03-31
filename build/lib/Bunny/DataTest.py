class DataTest(object):
	"""
	Data tests.
	Contains a statistical procedure to process data.

	SetTest(f)  sets function f as the statistical tests
	RunTest(D)  runs test self.Test on data D
	Validate()  ensures there is a test stored.
	Display(B)  prints properties, B is boolean value indicating verbosity
	"""

	def __init__(self,Test=None,Name="DataTest_Object"):
		self.Test=Test
		self.Name=Name

	def SetTest(self, Test):
		self.Test = Test

	def RunTest(self, Data):
		if not self.Validate():
			return None
		return self.Test(Data)

	def Validate(self):
		if self.Test == None:
			print "ERROR. DataTest object doesn't have a statistical test.\nUse DataTest.SetTest()"
			return 0
		elif not hasattr(self.Test, '__call__'):
			print "ERROR. Cannot call data function"
		else:
			return 1

	def AddName(self, Name):
		self.Name = Name

	def Display(self, Full=True):
		# Print class properties
		if Full:
			for (property, value) in vars(self).iteritems():
				print property, ': ', value
		else:
			for (property, value) in vars(self).iteritems():
				print property
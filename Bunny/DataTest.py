class DataTest(object):
	"""
	Data tests.
	"""

	def __init__(self,Name="DataTest skeleton"):
		self.Test=None
		self.Name=Name

	def SetTest(self, Test):
		self.Test = Test

	def RunTest(self, Data):
		if not self.Validate():
			return None
		return self.Test(Data)

	def Validate(self):
		if self.Test == None:
			print "Error. No test in DataTest object."
			return 0
		else:
			return 1
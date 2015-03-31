import random
import numpy as np

def RandomAgent():
	# Generate a random agent
	def F():
		return random.random()
	return F

def Binomial(Bias=0.5):
	# Generate an agent with a binomial bias
	def F(B=Bias):
		return 1 if random.random() < B else 0
	return [F,"Binomial behavior","Unit"]

def Poisson(L=1):
	# Generate an agent with a poisson distribution
	def F(Lambda=L):
		# Last zero is because np returns an array.
		return np.random.poisson(Lambda,1)[0]
	return [F,"Poisson behavior","Real"]

def Empirical(List):
	# If list is a list of items it will randomly select one,
	# if it's a list of lists, it will take the first value as the
	# outcome, and the second value as the number of counts.
	# Generate an agent that responds as given by the empirical distribution
	Lists = [isinstance(i,list) for i in List]
	# If you got a list of lists
	if sum(Lists)==len(Lists):
		# Repeat each item by the number of observations
		NewList = [[i[0]]*i[1] for i in List]
		# Flatten list
		List = [item for sublist in NewList for item in sublist]
	def F():
		return random.choice((List))
	return [F,"Empirically set behavior","None"]

def Geometric(param):
	"""
	Generate a geometric distribution with parameter p (mean = 1/p)
	"""
	def F(p=param):
		return np.random.geometric(p)
	return [F,"Geometric distribution","Real"]


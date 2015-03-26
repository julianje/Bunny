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
	return F

def Poisson(L=1):
	# Generate an agent with a poisson distribution
	def F(Lambda=L):
		# Last zero is because np returns an array.
		return np.random.poisson(Lambda,1)[0]
	return F
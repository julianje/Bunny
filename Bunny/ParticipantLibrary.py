import random

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
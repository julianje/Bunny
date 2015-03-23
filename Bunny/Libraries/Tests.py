import scipy.stats

def BinomialTest(TestType="TT",Bias=0.5,pval=0.05):
	# Binomial test
	if TestType=="TT":
		def F(Data):
			res=scipy.stats.binom_test(sum(Data),len(Data),Bias)
			return 1 if res<=pval else 0
	elif TestType=="OT":
		def F(Data):
			res=scipy.stats.binom.sf(sum(Data),len(Data),Bias)
			return 1 if res<=pval else 0
	else:
		print "Error: Binomial test must be one-tailed (OT) or two-tailed (TT)."
		return None	
	return F

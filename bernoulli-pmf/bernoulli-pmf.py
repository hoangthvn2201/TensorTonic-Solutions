import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    pmf = [p if element == 1 else 1-p for element in x]
    pmf = np.array(pmf)
    mean = p 
    var = p * (1-p)
    return (pmf, mean, var)
    
    
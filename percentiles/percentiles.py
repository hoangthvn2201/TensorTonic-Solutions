import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.array(x)
    percentiles = []
    for element in q:
        percentiles.append(np.percentile(x, element, method='linear'))
    percentiles = np.array(percentiles)
    return percentiles
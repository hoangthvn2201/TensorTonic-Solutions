import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    array_x = np.array(x)

    return (np.exp(array_x) - np.exp(-array_x)) / (np.exp(array_x) + np.exp(-array_x))
        
        
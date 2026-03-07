import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    v = np.asarray(v)
    if v.ndim == 1:
        return np.sqrt(np.sum(v**2))
    norm = []
    for i in range(len(v)):
        norm.append(np.sqrt(np.sum(v[i]**2)))
    norm = np.asarray(norm)
    return norm
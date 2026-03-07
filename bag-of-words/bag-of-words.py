import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    dct = {}
    for i in vocab:
        dct[i] = 0 
    for token in tokens:
        if token in vocab: 
            dct[token] += 1
    returned = list(dct.values())
    returned = np.array(returned, dtype=int)
    return returned
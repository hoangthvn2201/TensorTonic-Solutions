import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    labels = set(rater1)
    if len(labels) == 1:
        return 1
    count_of_label_1 = []
    count_of_label_2 = []
    n = len(rater1)
    p_e = 0 
    for label in labels: 
        count_of_label_1.append(np.sum([1 if i == label else 0 for i in rater1 ]))
        count_of_label_2.append(np.sum([1 if i == label else 0 for i in rater2 ]))
    p_o = np.sum([1 if rater1[i] == rater2[i] else 0 for i in range(len(rater1))]) / n
    for i in range(len(labels)): 
        p_e += count_of_label_1[i] * count_of_label_2[i] / (n**2)
    if p_e != 1:
        k = (p_o - p_e) / (1 - p_e)
    else:
        k = 0
    return k 
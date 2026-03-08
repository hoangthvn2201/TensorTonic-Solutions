def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    k = len(weights)
    w_sum = sum(weights)
    returned_lst = []
    for i in range(len(values) - k + 1):
        weight_sum = 0
        for j in range(k):
            weight_sum += weights[j]*values[i+j]
        returned_lst.append(weight_sum/w_sum)
    return returned_lst
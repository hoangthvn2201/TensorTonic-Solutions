def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    # Write code here
    norm_ratings = []
    for user in matrix:
        total_rate = 0
        num_rate = 0
        for i in range(len(user)):
          if user[i] != 0:
            total_rate += user[i]
            num_rate += 1
        if num_rate == 0:
            norm_rate = [0 for i in range(len(user))]
        else:
            mean = total_rate / num_rate      
            norm_rate = [user[i] - mean if user[i] != 0 else 0 for i in range(len(user))]
        norm_ratings.append(norm_rate)
    return norm_ratings
            
        
def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    wr = []
    for element in items: 
        weighted_rating = element[1]*element[0]/(element[1]+min_votes) + min_votes*global_mean/(element[1]+min_votes)
        wr.append(weighted_rating)

    return wr 
    
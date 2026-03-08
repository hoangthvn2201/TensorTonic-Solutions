def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    unrated_items = [(scores[i], i) for i in range(len(scores)) if i not in rated_indices]
    sorted_unrated_items = sorted(unrated_items, reverse=True, key=lambda x: x[0])
    sorted_unrated_items = sorted_unrated_items[:k]
    return_lst = []
    for i in range(len(sorted_unrated_items)):
        return_lst.append(sorted_unrated_items[i][1])

    return return_lst
    
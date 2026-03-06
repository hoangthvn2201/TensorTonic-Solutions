def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    precision = 0
    recall = 0 
    top_k_recommended = recommended[:k]
    relevant_top_k = list(set(top_k_recommended) & set(relevant))
    precision = float(len(set(relevant_top_k)) / k)
    recall = float(len(set(relevant_top_k)) / len(relevant))

    return [precision, recall]
    
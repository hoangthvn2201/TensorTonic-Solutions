def priority_replay_sample(priorities, alpha, beta):
    """
    Compute sampling probabilities and importance sampling weights for PER.
    """
    # Write code here    
    powered_priorities = [i ** alpha for i in priorities]

    total = sum(powered_priorities)

    probs = [i / total for i in powered_priorities]

    n = len(priorities)
    
    raw = [(n*probs[i]) ** (-beta) for i in range(len(probs))]

    max_raw = max(raw)

    weighted = [raw[i] / (max_raw) for i in range(len(raw))]
    

    return [probs, weighted]
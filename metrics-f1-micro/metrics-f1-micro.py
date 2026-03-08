def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    classes = set(y_true+y_pred)
    
    total_tp = 0
    total_fp = 0
    total_fn = 0
    for cl in classes:
        fp = 0
        fn = 0
        tp = 0
        for i in range(len(y_pred)):
            if y_pred[i] != y_true[i]:
                if y_pred[i] == cl:
                    fp += 1
                else:
                    if y_true[i] == cl:
                        fn += 1
            else:
                if y_true[i] == cl:
                    tp += 1
        total_fn += fn 
        total_fp += fp 
        total_tp += tp 

    # precision = total_tp / (total_tp + total_fp)
    # recall = total_tp / (total_tp + total_fn)
    return 2 * total_tp / (2 * total_tp + total_fp + total_fn)
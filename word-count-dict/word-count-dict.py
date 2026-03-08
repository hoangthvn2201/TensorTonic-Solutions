def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    dct = {}
    for sentence in sentences:
        for word in sentence:
            if word not in dct.keys():
                dct[word] = 1
            else:
                dct[word] += 1
    return dct 
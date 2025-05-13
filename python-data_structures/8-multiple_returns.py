def multiple_returns(sentence):
    # if thr sentence is not empty
    if sentence:
        # we tuple over a list since tuple accepts only  argument
        return tuple([len(sentence), sentence[0]])
    return

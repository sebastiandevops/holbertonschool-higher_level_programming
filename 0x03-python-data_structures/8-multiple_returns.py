#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        result = (len(sentence), None)
    else:
        result = (len(sentence), sentence[0])
    return result

#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary.values() == 0:
        return None
    else:
        return max(a_dictionary.keys())

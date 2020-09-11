#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    else:
        result = max(a_dictionary.values())
        for key in list(a_dictionary.keys()):
            if a_dictionary[key] == result:
                return key

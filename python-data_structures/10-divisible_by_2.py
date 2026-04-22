#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if not my_list:
        return []

    results = []
    for num in my_list:
        if num % 2 == 0:
            results.append(True)
        else:
            results.append(False)
    # This return must align with the 'for' and 'if not'
    return results

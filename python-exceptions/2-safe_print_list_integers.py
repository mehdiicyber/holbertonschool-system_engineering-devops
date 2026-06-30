#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers.

    Args:
        my_list (list): The list containing various types of elements.
        x (int): The number of elements to access from my_list.

    Returns:
        int: The real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count

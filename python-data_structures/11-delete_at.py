#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.
    """
    # Check if index is within valid range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Delete the element at the index
    del my_list[idx]

    return my_list

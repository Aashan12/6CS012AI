def reverse_skip(lst):
    """
    Return every second element starting from the second-to-last element in reverse order.

    Parameters:
    lst (list): Input list.

    Returns:
    list: Elements in reverse order skipping one element.
    """
    return lst[-2::-2]


# Example
print(reverse_skip([1, 2, 3, 4, 5, 6]))
def remove_first_last(lst):
    """
    Remove the first and last elements from a list.

    Parameters:
    lst (list): Input list.

    Returns:
    list: List without the first and last elements.
    """
    return lst[1:-1]


# Example
print(remove_first_last([1, 2, 3, 4, 5]))
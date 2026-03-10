def get_last_n(lst, n):
    """
    Return the last n elements of a list.

    Parameters:
    lst (list): Input list.
    n (int): Number of elements to extract.

    Returns:
    list: Last n elements.
    """
    return lst[-n:]


# Example
print(get_last_n([1, 2, 3, 4, 5], 2))
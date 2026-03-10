def get_first_n(lst, n):
    """
    Return the first n elements of a list.

    Parameters:
    lst (list): Input list.
    n (int): Number of elements to extract.

    Returns:
    list: First n elements.
    """
    return lst[:n]


# Example
print(get_first_n([1, 2, 3, 4, 5], 3))
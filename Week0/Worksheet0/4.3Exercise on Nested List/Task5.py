def find_max(lst):
    """
    Find the maximum value in a nested list.
    """
    maximum = float('-inf')

    for item in lst:
        if isinstance(item, list):
            maximum = max(maximum, find_max(item))
        else:
            maximum = max(maximum, item)

    return maximum


# Example
print(find_max([[1,2],[3,[4,5]],6]))
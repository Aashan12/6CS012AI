def average_nested(lst):
    """
    Calculate average of all numbers in a nested list.
    """
    flat = deep_flatten(lst)
    return sum(flat) / len(flat)


# Example
print(average_nested([[1,2],[3,4],[5,6]]))
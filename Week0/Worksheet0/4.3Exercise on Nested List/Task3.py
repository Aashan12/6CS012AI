def sum_nested(lst):
    """
    Calculate the sum of all numbers in a nested list.
    """
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    return total


# Example
print(sum_nested([[1,2],[3,[4,5]],6]))
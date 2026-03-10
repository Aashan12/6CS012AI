def flatten(lst):
    """
    Flatten a nested list into a single list.
    """
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


# Example
print(flatten([[1, 2], [3, 4], [5]]))
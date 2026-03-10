def remove_element(lst, elem):
    """
    Remove all occurrences of elem from a nested list.
    """
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(remove_element(item, elem))
        elif item != elem:
            result.append(item)
    return result


# Example
lst = [[1,2],[3,2],[4,5]]
print(remove_element(lst,2))
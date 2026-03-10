def access_nested_element(lst, indices):
    """
    Access an element in a nested list using indices.
    """
    element = lst
    for i in indices:
        element = element[i]
    return element


# Example
lst = [[1,2,3],[4,5,6],[7,8,9]]
print(access_nested_element(lst, [1,2]))
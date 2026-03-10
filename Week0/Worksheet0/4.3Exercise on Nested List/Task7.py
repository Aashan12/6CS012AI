def deep_flatten(lst):
    """
    Flatten a deeply nested list into a single list.
    """
    result = []

    for item in lst:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)

    return result


# Example
print(deep_flatten([[[1,2],[3,4]],[[5,6],[7,8]]]))
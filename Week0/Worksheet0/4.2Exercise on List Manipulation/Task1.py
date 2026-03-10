def extract_every_other(lst):
    """
    Extract every other element from a list starting from the first element.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list containing every other element.
    """
    return lst[::2]


# Example
numbers = [1, 2, 3, 4, 5, 6]
result = extract_every_other(numbers)

print("Original list:", numbers)
print("Every other element:", result)
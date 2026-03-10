def get_sublist(lst, start, end):
    """
    Return a sublist from the list from index 'start' to 'end' (inclusive).

    Parameters:
    lst (list): The original list.
    start (int): Starting index.
    end (int): Ending index.

    Returns:
    list: A new list containing elements from start to end.
    """
    return lst[start:end+1]


# Example
numbers = [1, 2, 3, 4, 5, 6]
result = get_sublist(numbers, 2, 4)

print("Original list:", numbers)
print("Sublist:", result)
def count_occurrences(lst, elem):
    """
    Count how many times elem appears in a nested list.
    """
    count = 0

    for item in lst:
        if isinstance(item, list):
            count += count_occurrences(item, elem)
        elif item == elem:
            count += 1

    return count


# Example
lst = [[1,2],[2,3],[2,4]]
print(count_occurrences(lst,2))
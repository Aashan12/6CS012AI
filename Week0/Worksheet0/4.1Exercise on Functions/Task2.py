def find_sum(numbers):
    """
    Calculate the sum of a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The sum of all numbers in the list.
    """
    return sum(numbers)


def find_average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The average of the numbers.
    """
    return sum(numbers) / len(numbers)


def find_max(numbers):
    """
    Find the maximum value in a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The largest number in the list.
    """
    return max(numbers)


def find_min(numbers):
    """
    Find the minimum value in a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The smallest number in the list.
    """
    return min(numbers)


print("Choose an operation:")
print("1. Sum")
print("2. Average")
print("3. Maximum")
print("4. Minimum")

try:
    choice = int(input("Enter your choice (1-4): "))
    user_input = input("Enter numbers separated by spaces: ")

    # Convert input string to list of floats
    numbers = [float(x) for x in user_input.split()]

    if len(numbers) == 0:
        print("Error: The list is empty.")
    else:
        if choice == 1:
            print("Sum =", find_sum(numbers))
        elif choice == 2:
            print("Average =", find_average(numbers))
        elif choice == 3:
            print("Maximum =", find_max(numbers))
        elif choice == 4:
            print("Minimum =", find_min(numbers))
        else:
            print("Invalid choice.")

except ValueError:
    print("Error: Please enter valid numbers.")
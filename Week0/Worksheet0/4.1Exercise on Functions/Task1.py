def convert_units(conversion_type, value):
    """
    Convert measurement units based on the selected conversion type.

    Parameters:
    conversion_type (int): The type of conversion selected by the user.
                           1 = meters to feet
                           2 = feet to meters
                           3 = kilograms to pounds
                           4 = pounds to kilograms
                           5 = liters to gallons
                           6 = gallons to liters
    value (float): The numeric value to convert.

    Returns:
    float: The converted value.
    """

    if conversion_type == 1:
        return value * 3.28084   # meters → feet
    elif conversion_type == 2:
        return value / 3.28084   # feet → meters
    elif conversion_type == 3:
        return value * 2.20462   # kg → pounds
    elif conversion_type == 4:
        return value / 2.20462   # pounds → kg
    elif conversion_type == 5:
        return value * 0.264172  # liters → gallons
    elif conversion_type == 6:
        return value / 0.264172  # gallons → liters
    else:
        return None


print("Unit Converter")
print("1. Length: meters → feet")
print("2. Length: feet → meters")
print("3. Weight: kilograms → pounds")
print("4. Weight: pounds → kilograms")
print("5. Volume: liters → gallons")
print("6. Volume: gallons → liters")

try:
    choice = int(input("Choose conversion type (1-6): "))
    value = float(input("Enter value to convert: "))

    result = convert_units(choice, value)

    if result is None:
        print("Unsupported conversion type.")
    else:
        print("Converted value:", result)

except ValueError:
    print("Invalid input! Please enter numeric values.")
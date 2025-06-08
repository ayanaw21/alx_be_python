# temp_conversion_tool.py

# Define Global Conversion Factors
# FAHRENHEIT_TO_CELSIUS_FACTOR is for converting Fahrenheit to Celsius
# Formula: (F - 32) * 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.
    """
    # Accessing global variable (no 'global' keyword needed as we are only reading)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.
    """
    # Accessing global variable (no 'global' keyword needed as we are only reading)
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to interact with the user for temperature conversion.
    """
    while True:
        try:
            temp_input = input("Enter the temperature to convert: ")
            # Try to convert input to a float
            temperature = float(temp_input)
            break # Exit loop if conversion is successful
        except ValueError:
            # If conversion fails, raise the specified error
            print("Invalid temperature. Please enter a numeric value.")
            continue # Continue the loop to prompt again

    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            break # Exit loop if unit is valid
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()
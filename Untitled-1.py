def convert_length(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "inches": 0.0254,
        "feet": 0.3048,
        "yards": 0.9144
    }
    
    # Convert the value to meters
    value_in_meters = value * length_units[from_unit]
    
    # Convert from meters to the desired unit
    return value_in_meters / length_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value  # If the units are the same

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "grams": 1,
        "kilograms": 1000,
        "milligrams": 0.001,
        "pounds": 453.592,
        "ounces": 28.3495
    }
    
    # Convert the value to grams
    value_in_grams = value * weight_units[from_unit]
    
    # Convert from grams to the desired unit
    return value_in_grams / weight_units[to_unit]

def convert_volume(value, from_unit, to_unit):
    volume_units = {
        "liters": 1,
        "milliliters": 0.001,
        "cubic meters": 1000,
        "gallons": 3.78541,
        "cups": 0.236588
    }
    
    # Convert the value to liters
    value_in_liters = value * volume_units[from_unit]
    
    # Convert from liters to the desired unit
    return value_in_liters / volume_units[to_unit]

def unit_converter():
    print("Unit Converter")
    print("1. Length")
    print("2. Temperature")
    print("3. Weight")
    print("4. Volume")
    choice = input("Choose the type of conversion (1-4): ")

    value = float(input("Enter the value to convert: "))
    
    if choice == "1":
        from_unit = input("Enter the current length unit (meters, kilometers, centimeters, millimeters, inches, feet, yards): ").lower()
        to_unit = input("Enter the target length unit (meters, kilometers, centimeters, millimeters, inches, feet, yards): ").lower()
        result = convert_length(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")
    
    elif choice == "2":
        from_unit = input("Enter the current temperature unit (Celsius, Fahrenheit, Kelvin): ").capitalize()
        to_unit = input("Enter the target temperature unit (Celsius, Fahrenheit, Kelvin): ").capitalize()
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")
    
    elif choice == "3":
        from_unit = input("Enter the current weight unit (grams, kilograms, milligrams, pounds, ounces): ").lower()
        to_unit = input("Enter the target weight unit (grams, kilograms, milligrams, pounds, ounces): ").lower()
        result = convert_weight(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")
    
    elif choice == "4":
        from_unit = input("Enter the current volume unit (liters, milliliters, cubic meters, gallons, cups): ").lower()
        to_unit = input("Enter the target volume unit (liters, milliliters, cubic meters, gallons, cups): ").lower()
        result = convert_volume(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")
    
    else:
        print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    unit_converter()

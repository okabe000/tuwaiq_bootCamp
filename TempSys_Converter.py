def convert_temp_c_to_f(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
def convert_temp_f_to_c(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

input_unit = input("Enter the input temperature unit (C/F): ").strip().upper()
if input_unit == 'F':
    temp_f = float(input("Enter temperature in Fahrenheit: "))
    temp_c = convert_temp_f_to_c(temp_f)
    print(f"{temp_f}°F is {temp_c:.2f}°C")
elif input_unit == 'C':
    temp_c = float(input("Enter temperature in Celsius: "))
    temp_f = convert_temp_c_to_f(temp_c)
    print(f"{temp_c}°C is {temp_f:.2f}°F")
else:
    print("Invalid input unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
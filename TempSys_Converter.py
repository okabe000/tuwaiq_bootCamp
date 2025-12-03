def convert_temp_c_to_f(celsius : float) -> float:  # giving type hints, and specifying return type
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def convert_temp_f_to_c(fahrenheit: float) -> float: # giving type hints, and specifying return type
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def main():
    input_unit = input("Enter the input temperature unit (C/F): ").strip().upper() # extracting one letter as the input unit 


    if input_unit == 'F':
        try:
            temp_f = float(input("Enter temperature in Fahrenheit: "))
        except ValueError:
            print("Invalid temperature value. Please enter a numeric value.")
            exit(1)

        temp_c = convert_temp_f_to_c(temp_f)
        print(f"{temp_f:.2f}°F is {temp_c:.2f}°C")
    elif input_unit == 'C':
        try:
            temp_c = float(input("Enter temperature in Celsius: "))
        except ValueError:
            print("Invalid temperature value. Please enter a numeric value.")
            exit(1)
        temp_f = convert_temp_c_to_f(temp_c)
        print(f"{temp_c:.2f}°C is {temp_f:.2f}°F")
    else:
        print("Invalid input unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
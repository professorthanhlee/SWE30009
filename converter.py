# Temperature Conversion Program
# Developer: [Le Nam Cong Thanh]
# Student ID: [103410217]


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5/9 + 273.15


def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32


def main():
    print("Temperature Conversion Program")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choice = int(input("Enter your choice (1/2/3/4/5/6): "))

    if choice == 1:
        celsius_temperature = float(
            input("Enter the temperature in Celsius: "))
        fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
        print(f"{celsius_temperature:.2f} degrees Celsius is equal to {fahrenheit_temperature:.2f} degrees Fahrenheit.")
    elif choice == 2:
        fahrenheit_temperature = float(
            input("Enter the temperature in Fahrenheit: "))
        celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
        print(f"{fahrenheit_temperature:.2f} degrees Fahrenheit is equal to {celsius_temperature:.2f} degrees Celsius.")
    elif choice == 3:
        celsius_temperature = float(
            input("Enter the temperature in Celsius: "))
        kelvin_temperature = celsius_to_kelvin(celsius_temperature)
        print(
            f"{celsius_temperature:.2f} degrees Celsius is equal to {kelvin_temperature:.2f} Kelvin.")
    elif choice == 4:
        kelvin_temperature = float(input("Enter the temperature in Kelvin: "))
        celsius_temperature = kelvin_to_celsius(kelvin_temperature)
        print(
            f"{kelvin_temperature:.2f} Kelvin is equal to {celsius_temperature:.2f} degrees Celsius.")
    elif choice == 5:
        fahrenheit_temperature = float(
            input("Enter the temperature in Fahrenheit: "))
        kelvin_temperature = fahrenheit_to_kelvin(fahrenheit_temperature)
        print(f"{fahrenheit_temperature:.2f} degrees Fahrenheit is equal to {kelvin_temperature:.2f} Kelvin.")
    elif choice == 6:
        kelvin_temperature = float(
            input("Enter the temperature in Fahrenheit: "))
        fahrenheit_temperature = kelvin_to_fahrenheit(kelvin_temperature)
        print(
            f"{kelvin_temperature:.2f} Kelvin is equal to {fahrenheit_temperature:.2f} degrees Fahrenheit.")
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")


if __name__ == "__main__":
    main()

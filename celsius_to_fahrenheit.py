#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program converts temperatures in Celsius to Fahrenheit


def fahrenheit():
    # This function calculates the temperature in Fahrenheit

    # Input
    print("This program converts temperatures in Celsius to Fahrenheit.")
    print("")
    celsius_string = input("Enter a temperature (°C): ")

    # Process
    while True:
        try:
            celsius_integer = int(celsius_string)

            print("")
            break
        except Exception:
            celsius_string = input("{} is not a valid input. Enter a "
                                   "temperature (°C): ".format(celsius_string))
    fahrenheit_temperature = (9 / 5) * celsius_integer + 32

    # Output
    print("{0}°C is {1}°F.".format(celsius_integer, fahrenheit_temperature))
    print("\nDone.")


def main():
    # This function calls other functions

    # Call functions
    fahrenheit()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 05, 12, 2025
# This program calculates area of triangle.


# Defines the first function needed for calculations.
def calc_area(height, base):
    # Calculates area
    area = 0.5 * height * base
    #Rounds the output till one decimal at the end
    area = round(area, 1)
    # Displays the area
    print(f"The area of triangle is {area} in cm")


def main():
    # Gets the input from the user
    height = input("Enter height of triangle.")
    base = input("Enter the base of triangle.")
    try:
        # Checks if the input inputted by the user is correct
        height = float(height)
        base = float(base)
        #Checks if input is positive
        if height < 0 or base < 0:
            print("You can't have negative input.")
        else:
            # Calls the function
            calc_area(height, base)
        # Prints out the specific statement if input is wrong
    except Exception:
        print("Your input should be float.")


if __name__ == "__main__":
    main()

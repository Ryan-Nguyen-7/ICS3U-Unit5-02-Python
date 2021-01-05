#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on January 2021
# This program uses a function to calculate
#   the area of a triangle


def calculate_area(base, height):
    # This function calculates area of a triangle

    # process
    area = (base*height) / 2

    # output
    print("The area is {}cm²".format(area))


def main():
    # input
    base_as_string = input("Enter base: ")
    height_as_string = input("Enter height: ")
    print("")

    try:
        base_as_number = int(base_as_string)
        height_as_number = int(height_as_string)

        if base_as_number > 0 and height_as_number > 0:
            # call function
            calculate_area(base_as_number, height_as_number)
        else:
            print("Integers must be positive")
    except Exception:
        print("Invalid integer")


if __name__ == "__main__":
    main()

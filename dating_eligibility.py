#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program determines if you are of the right age to date a grandmothers
# granddaughter


def main():

    # process
    try:

        # input
        age = int(input("Enter your age:"))
        print("")

    # Output
        if age > 25 and age < 40:
            print("You are a suitable fit for my granddaughter!!")
        else:
            print("You are not good enough for my granddaughter!!")
    except Exception:
        print("Please input a proper age")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Created by: Lucas DeBruyn
# Created on: October 2022
# This program uses if statements to guess a random number
#    with user input

import random


def main():
    # this uses if statements to guess a random number
    random_number_to_guess = random.randint(0, 9)  # a number between 0 and 9

    # input
    some_variable = int(input("Enter a number between 0 and 9: "))

    # process and output
    if some_variable == random_number_to_guess:
        print("You guessed correctly!")
    if some_variable != random_number_to_guess:
        print(
            "You guessed incorrectly. The correct number is : {0}".format(
                random_number_to_guess
            )
        )

    print("\nDone.")


if __name__ == "__main__":

    main()

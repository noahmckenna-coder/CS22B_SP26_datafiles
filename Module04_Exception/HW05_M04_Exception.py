### CS 22B Module 03 - Homework 5
### Name: Noah McKenna

##### Homework to practice writing Exceptions #####

##### Problem 1: Math Function with Exception Handling #####
## Write a Python function calculate_square_root(number) that takes a single argument number. The function should:
## Raise a ValueError with the message "Input must be a non-negative number" if the input is negative.
## Use a try-except block to catch the ValueError when you call the function and print the error message. If no exception occurs, return the square root of the number (you can use number ** 0.5 for simplicity).
def calculate_square_root(number):
    if number < 0:
        raise ValueError("Input must be a non-negative number")
    return number ** 0.5

try:
    result = calculate_square_root(-9)
    print("Square root:", result)
except ValueError as e:
    print(e)

##### Problem 2: Re-write Exception Handling #####
## A Python programmer has written a piece of code below, that reads a DNA sequence from a file and splits it up into a set number of equal-sized pieces (ignoring any incomplete pieces at the end of the sequence). It asks the user to enter the name of the file and the number of pieces, calculates the length of each piece (by dividing the total length by the number of pieces), then uses a range() to print out each piece.
## Re-write the python program in the empty cell below. Use try/except blocks to handle all the potential exceptions that may arise such as giving it the name of a non-existent file, or entering zero when asked for the number of pieces – or indeed, entering something that isn't a number at all when asked for the number of pieces. The input file dna_test.txt can be used to test your program.

## This is the original python program
import os
import sys

DNA="CTAGCTAGGCGAGCTACGAGAGCTAGCGAGACATCGATCAGTACGATCGACTCGACTAGCTACGACTACGATCAGCTACGATC"
f = open("dna_test.txt", 'w')
f.write(DNA)
f.close()

# check for valid filename
try:
    input_file = input('enter filename:\n')
    if not os.path.isfile(input_file):
        raise FileNotFoundError('not a valid filename')

    f = open(input_file)
    dna = f.read().rstrip("\n")
    f.close()

# check for valid number
    pieces = input('enter number of pieces:\n')
    if not pieces.isdigit():
        raise ValueError('not a valid number')

# check that number is not zero or negative
    pieces = int(pieces)
    if pieces <= 0:
        raise ValueError('number of pieces must be greater than zero')
# do the processing
    piece_length = int(len(dna) / pieces)
    print('piece length is ' + str(piece_length))
    for start in range(0, len(dna)-piece_length+1, piece_length):
        print(dna[start:start+piece_length])
except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print("Unexpected error:", e)

##### Problem 3: Writing a python class with exception handling #####
### Write a Python class TemperatureConverter with the following functionality:

## Constructor (init):
## Accepts two parameters: a numeric temperature and a scale ("C" for Celsius or "F" for Fahrenheit).
## Validates that: temperature is a number. Raise a TypeError if not. scale is either "C" or "F" (case-insensitive). Raise a ValueError if invalid.

## Methods:
## to_fahrenheit(): Converts the temperature to Fahrenheit: -> If the scale is "C", check if the input is above absolute zero (-273.15°C). If not, raise a ValueError. -> If the scale is "F", return the temperature as-is.
## to_celsius(): Converts the temperature to Celsius: -> If the scale is "F", check if the input is above absolute zero (-459.67°F). If not, raise a ValueError. -> If the scale is "C", return the temperature as-is.

## Requirements:
## Implement exception handling (try-except) for invalid inputs when creating an instance of the class or calling its methods.
## Demonstrate the following cases:
## - Converting 100°C to Fahrenheit.
## - Converting 32°F to Celsius.
## - Passing an invalid scale (e.g., "K") to the constructor.
## - Providing a temperature below absolute zero for either scale.
class TemperatureConverter:
    def __init__(self, temperature, scale):
        if not isinstance(temperature, (int, float)):
            raise TypeError("Temperature must be a number")

        if scale.upper() not in ["C", "F"]:
            raise ValueError("Scale must be 'C' or 'F'")

        self.temperature = temperature
        self.scale = scale.upper()

    def to_fahrenheit(self):
        if self.scale == "C":
            if self.temperature < -273.15:
                raise ValueError("Temperature below absolute zero in Celsius")
            return (self.temperature * 9/5) + 32
        return self.temperature

    def to_celsius(self):
        if self.scale == "F":
            if self.temperature < -459.67:
                raise ValueError("Temperature below absolute zero in Fahrenheit")
            return (self.temperature - 32) * 5/9
        return self.temperature
#Demonstration
try:
    t1 = TemperatureConverter(100, "C")
    print("100°C ->", t1.to_fahrenheit(), "°F")

    t2 = TemperatureConverter(32, "F")
    print("32°F ->", t2.to_celsius(), "°C")
except Exception as e:
    print(e)

try:
    t3 = TemperatureConverter(50, "K")
except Exception as e:
    print("Error:", e)

try:
    t4 = TemperatureConverter(-500, "F")
    print(t4.to_celsius())
except Exception as e:
    print("Error:", e)

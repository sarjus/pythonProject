"""
Program: binarytodecimal.py
Author: Sarju S
Last date modified: 28/02/23
Converts a string of bits to a decimal integer.
"""
binaryNumber = input("Enter the Binary Number:")
decimalNumber=0
exponent = len(binaryNumber)-1
for digit in binaryNumber:
    decimalNumber = decimalNumber + int(digit) * 2**exponent
    exponent-=1
print("The decimal equivalent is: ",decimalNumber)
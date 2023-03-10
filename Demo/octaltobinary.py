"""
Program: octaltobinary.py
Author: Sarju S
Last date modified: 28/02/23
Converts a octal to a string of bits.
"""
octalNumber = input("Enter the Octal Number:")
length = len(octalNumber)
binaryNumber=""
for digit in octalNumber:
    number = int(digit)
    if number==7:
        binaryNumber = binaryNumber+"111"
    elif number==6:
        binaryNumber = binaryNumber + "110"
    elif number == 5:
        binaryNumber = binaryNumber + "101"
    elif number == 4:
        binaryNumber = binaryNumber + "100"
    elif number == 3:
        binaryNumber = binaryNumber + "011"
    elif number == 2:
        binaryNumber = binaryNumber + "010"
    elif number == 1:
        binaryNumber = binaryNumber + "001"
    elif number == 0:
        binaryNumber = binaryNumber + "000"
print(binaryNumber)




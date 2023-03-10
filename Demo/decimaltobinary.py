"""
Program: decimaltobinary.py
Author: Sarju S
Last date modified: 28/02/23
Converts a decimal integer to a string of bits.
"""
decimalNumber=int(input("Enter a decimal number:"))
if decimalNumber==0:
    print(0)
else:
    binaryNumber=""
    print("Quotient Remainder Binary")
    while decimalNumber>0:
        remainder = decimalNumber%2
        decimalNumber = decimalNumber//2
        binaryNumber = str(remainder)+binaryNumber
        print("%5d%8d%12s" % (decimalNumber, remainder,
                              binaryNumber))
    print("The binary equivalent is",binaryNumber)

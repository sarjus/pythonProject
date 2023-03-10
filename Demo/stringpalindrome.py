"""
Program: stringpalindrome.py
Author: Sarju S
Last date modified: 07/0/23
Description: Program to check Whether a String is Palindrome or Not
"""
inputString=input("Enter the string to check whether it is palindrome or not:")
inputString=inputString.upper()
if inputString==inputString[::-1]:
    print("The String is palindrome")
else:
    print("The String is not palindrome")
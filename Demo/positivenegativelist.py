"""
Program: positivenegativelist.py
Author: Sarju S
Last date modified: 10/03/23
Description : program to read a list of n integers (positive as well as negative).
Create two new lists, one having all positive numbers and the other having all
negative numbers from the given list. Print all three lists.
"""
maxNumbers = int(input("How many numbers do you want to add in the list? (Number can be both positive and negative)"))
# initialize empty lists
inputList=list()
positiveNumbersList=list()
negativeNumbersList=list()
for i in range(maxNumbers):
    inputNumber=int(input("Enter a number:"))
    inputList.append(inputNumber)
print("All Numbers List :", inputList)
for number in inputList:
    if number>0:
        # if number is positive
        positiveNumbersList.append(number)
    else:
        # if number is positive
        negativeNumbersList.append(number)
print("Positive Numbers List: ",positiveNumbersList)
print("Negative Numbers List: ",negativeNumbersList)


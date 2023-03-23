"""
Program: removeduplicatelist.py
Author: Sarju S
Last date modified: 10/03/23
Description : Remove Duplicate numbers from a List
"""
duplicateList=[10,20,15,10,25,15,70,20]
finalList=[]
for number in duplicateList:
    if number not in finalList:
        finalList.append(number)
print("The List with duplicate numbers: ", duplicateList)
print("The final list:", finalList)
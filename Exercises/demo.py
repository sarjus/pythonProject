duplicateList=[10,20,30,10,30,40,20]
finalList=[]
for number in duplicateList:
    if number not in finalList:
        finalList.append(number)
print("The list with duplicate values:",duplicateList)
print("The final list:", finalList)
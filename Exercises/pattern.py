"""
Author: Sarju S
Last date modified: 23/02/23
1
1 2
1 2 3
1 2 3 4
"""
for inputNumber in range(1,5):
    i=0
    for i in range(2,inputNumber+1):
        if inputNumber%i==0:
            break
    #print(inputNumber,inputNumber,i)
    if i<(inputNumber):
        continue
    print(inputNumber)



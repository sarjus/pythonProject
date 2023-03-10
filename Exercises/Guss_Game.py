"""
Author: Sarju S
Last date modified: 22/02/23
At start-up, the user enters the smallest
number and the largest number in the range.
The computer then selects a number from this
range. On each pass through the loop, the
user enters a number to attempt to guess
the number selected by the computer.
The program responds by saying
“You’ve got it,” “Too large, try again,”
or “Too small, try again.” When the user
 finally guesses the correct number,
 the program congratulates him and tells
 him the total number of guesses.

"""
import random
low=int(input("Enter the lower range:"))
high=int(input("Enter the high range:"))
myNumber=random.randint(low,high)
count=0
while(1):
    count+=1
    userNumber=int(input("Enter a number with in the limit:"))
    if userNumber>myNumber:
        print("Too big!!")
    elif userNumber<myNumber:
        print("Too small!!")
    else:
        print("Congratulations!!! You got it in ",count, " tries")
        break
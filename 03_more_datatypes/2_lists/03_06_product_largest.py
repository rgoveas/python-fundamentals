'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

import math

input1 = int(input("Enter number1:"))
input2 = int(input("Enter number2:"))
input3 = int(input("Enter number3:"))
input4 = int(input("Enter number4:"))
input5 = int(input("Enter number5:"))
input6 = int(input("Enter number6:"))
input7 = int(input("Enter number7:"))
input8 = int(input("Enter number8:"))
input9 = int(input("Enter number9:"))
input10 = int(input("Enter number10:"))

Input_list = []
Input_list.extend([input1, input2, input3, input4, input5, input6, input7, input8, input9, input10])

print(Input_list)

## Print the largest number in the list
print("The largest number in the list is:", max(Input_list))

## Print the result of the product of all the numbers in the list  
result1 = math.prod(Input_list) 

print(result1) 


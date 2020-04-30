'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
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

order = [1, 3, 5, 7, 9, 8, 6, 4, 2, 0]

Input_list = [Input_list[i] for i in order]

print(Input_list)

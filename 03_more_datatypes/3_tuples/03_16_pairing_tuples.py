'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''


##list = [2, 3, 4, 5]

##tuple_list = tuple(list)


##Output of the tuple = [(2,3) , (4,5)]

## (1,6), (7,0)

Input = input("Please enter a set of numbers: ")

lst = Input.split()

lst_in = []

## For loop inside the lst to convert each into integer

for i in lst : 
    int(i)

    lst_in.append(int(i))
        
print(lst_in)

##Automate tuple creation

for j in range(0, len(lst_in) - 1, 2) :
    print (lst_in[j], lst_in[j+1])

#tuple1 = (lst_in[0], lst_in[1])
#tuple2 = (lst_in[2], lst_in[3])

'''2 3 - 0
3 4 - 1  - 
4 5 - 2
5 6 - 3  - 
6 7 - 4 
7 8 - 5  - 
8 9 - 6
'''
##print(tuple1)
##print(tuple2)

#list_in_01 = []
#list_in_01.append(tuple1)
#list_in_01.append(tuple2)

#print(list_in_01)


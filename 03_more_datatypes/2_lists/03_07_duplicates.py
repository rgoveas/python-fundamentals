'''

Write a script that removes all duplicates from a list.

'''

listofNums = [1, 2, 3, 4, 3, 4, 5, 100, 200, 500, 100, 300, 50000, 200, 500]

# Convert list to set and then back to list
listofNums = list(set(listofNums))

print(listofNums)

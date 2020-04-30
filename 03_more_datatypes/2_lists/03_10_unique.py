'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

list_initial = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]



unique_list = list(set(list_initial))

print("The unique values from the first list is", unique_list)



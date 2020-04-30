'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

List_flat = []

for i in range(len(starting_list)): #Traversing through the main list
  for j in range (len(starting_list[i])): #Traversing through each sublist
    List_flat.append(starting_list[i][j]) #Appending elements into our flat_list
    
print("Original List:", starting_list)
print("Flattened List:",List_flat)

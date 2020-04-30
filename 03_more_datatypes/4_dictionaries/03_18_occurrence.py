'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
from collections import Counter

user_input = str(input("Please enter a string: "))

# Count the number of occurences of each letter in the string
 
result = Counter(user_input)

print (result)

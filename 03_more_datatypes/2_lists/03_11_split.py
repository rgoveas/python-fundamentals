'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

Input_list = []
string_input = input("Enter string:")

Input_list = (string_input.split())

print(Input_list)

def most_common(Input_list):
    return max(set(Input_list), key=Input_list.count)

print(most_common(Input_list))


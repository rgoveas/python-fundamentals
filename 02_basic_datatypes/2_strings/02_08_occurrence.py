'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

input_sentence = input("Please enter a sentence : ")

letter_input  = input("Please enter a word :  ")

first = input_sentence.index(letter_input)

print("Index of first occurrence of the letter : ", first)

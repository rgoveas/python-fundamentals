'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''


input_sentence = input("Please enter a sentence : ")

symbol = input("Please enter the symbol : ")

first = input_sentence[0]

modified_str = input_sentence.replace(first, symbol)

print("Modified String is : ", modified_str)


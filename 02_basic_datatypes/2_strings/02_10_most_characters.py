'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

#First string input from the user

string1 = input("Please enter the first word : ")

print (len(string1), "," , string1)

#Second string input from the user

string2 = input("Please enter the second word:  ")
print (len(string2), "," , string2)

#Third string input from the user

string3 = input("Please enter the third word:   ")
print (len(string3), "," , string3)

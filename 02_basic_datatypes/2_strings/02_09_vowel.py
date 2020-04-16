'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

#Obtain the user-input string

string = input("Please enter a sentence : ")

#Print the total number of vowels that are used in the user-input string

vowels=0
for i in string:
      if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)


#Count the occurence of each individual vowel in the string
#Print a count for each of the vowel in the string

print ("Number of occurence of 'a' in the sentence: ", string.count("a") + string.count("A"))
print ("Number of occurence of 'e' in the sentence: ", string.count("e") + string.count("E"))
print ("Number of occurence of 'i' in the sentence: ", string.count("i") + string.count("I"))
print ("Number of occurence of 'o' in the sentence: ", string.count("o") + string.count("O"))
print ("Number of occurence of 'u' in the sentence: ", string.count("u") + string.count("U"))



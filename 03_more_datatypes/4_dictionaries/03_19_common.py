'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

from collections import Counter

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

def mergeDict(dict_1, dict_2):
    
 ##Merge dictionaries and keep values of common keys in list

   dict_3 = {**dict_1, **dict_2}
   for key, value in dict_3.items():
       if key in dict_1 and key in dict_2:
               dict_3[key] = value + dict_1[key]
 
   return dict_3
 
# Merge dictionaries and add values of common keys in a list
dict_3 = mergeDict(dict_1, dict_2)
 
print('Dictionary 3 :')
print(dict_3)
'''
dict_1 = Counter({"a": 1, "b": 2, "c": 3})
dict_2 = Counter({"a": 2, "c": 4 , "d": 2})

dict3 = Counter(dict_1 + dict_2)
print (dict3) '''




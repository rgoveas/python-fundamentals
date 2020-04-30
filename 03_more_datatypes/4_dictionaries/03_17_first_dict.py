'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''
my = {}

'''
my = {1: 0, 2: 0, 3: 0, 4: 0, 5 : 0, 6 : 0, 7 : 0, 8: 0, 9 : 0, 10 : 0}


my[1] = 1
my[2] = 4
my[3] = 9
my[4] = 16
my[5] = 25
my[6] = 36
my[7] = 49
my[8] = 64
my[9] = 81
my[10] = 100
'''

for j in range(1, 11):
    my[j] = j**2

 #print(j)
 #print(j**2)

print(my)

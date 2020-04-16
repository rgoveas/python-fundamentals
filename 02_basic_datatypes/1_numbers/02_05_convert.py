'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

input1 = int(input("Please enter an integer: "))

float1 = float(input1)

float2 = float(input("Please enter a float value: "))

input2 = float(float2)

div = float1/input2

mult = input1 * float2

print("Division of the input values: ", div)
print("Multiplication of the input values:  ", mult)

'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''
#Obtain the temperature in fahrenheit from the user

temperature_fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))

#Write the necessary code to read a degree in Fahrenheit from the console
#then convert it to Celsius and print it to the console.
    #C = (F - 32) * (5 / 9)

temperature_celcius = (temperature_fahrenheit - 32) * (5/9)

temperature_celcius = round(temperature_celcius, 3)

#Print the output for the conversion

print(temperature_fahrenheit, "degrees fahrenheit = ", temperature_celcius, "degrees celcius")

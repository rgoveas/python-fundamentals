'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
## Obtain the investment values from the user
 ##   - investment amount
 ##   - interest rate in percentage
 ## - number of years to invest

PV = float(input("Please enter the investment amount: "))

i  = float(input("Please enter the interest rate in percentage: "))
##I = float(i/100)

N = float(input("Please enter the number of years to invest: "))

I = float ((PV) * (i/100) * (N))
FV = PV + I
print("Future value : ", FV)
print("Interest earned : ", I)

# HCF of two numbers
print("Enter two numbers: ")
num1 = int(input())
num2 = int(input())
while num1 != num2:
    if num1 > num2:
        num1 = num1 - num2
    else:
        num2 = num2 - num1
print("HCF of two numbers is: ", num1)

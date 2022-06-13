# check whether a number is prime or not

print("Enter a number: ")
num = int(input())
for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

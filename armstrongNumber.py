import math

print("Enter a number")
numStr = input()
num = int(numStr)
sum = 0

for i in range(len(numStr)):
    k = math.pow(int(numStr[i]), 3)
    sum = sum + k
    i += 1

if num == sum:
    print("Yay, It's Armstrong")
else:
    print("Naah")

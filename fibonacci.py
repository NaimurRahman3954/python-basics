def fibonacci(num):
    if num < 0:
        print("Incorrect input. Input positive number")
    elif num == 0:
        return 0
    elif num == 1 or num == 1:
        return 1
    else:
        return fibonacci(num-2)+fibonacci(num-1)


print("How many terms you want in Fibonacci series?")
numStr = input()
num = int(numStr)

for i in range(num):
    answer = fibonacci(i)
    print(answer)

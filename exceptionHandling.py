# exception handling is used to handle the error
# e.g zero division error, out of bound error, index error, name error, type error, value error, etc
# 'try' and 'except' blocks are used to handle the error

def func(x):
    try:
        return 10 / x
    except:
        print("there is a zero division error")


answer = func(0)
print(answer)

answer2 = func(5)
print(answer2)

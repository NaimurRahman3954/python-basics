# The scope of a variable is the region of code in which it can be referenced.
# A variable is said to be in scope if it can be referenced by name.
# Local scope: A variable is in local scope if it is declared within a function.
# Global scope: A variable is in global scope if it is declared outside of a function.

def func():
    x = 10
    print(x)


print(x)  # error: name 'x' is not defined
func()


def func2():
    global y  # global keyword is used to declare a variable as global
    print(y+30)


y = 10
func2()

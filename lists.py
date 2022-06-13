# list is a data structure that can store multiple values in a single variable

# lists are created using square brackets
a = [1, 2, 3, 4, 5]
print(a)

# list of strings
c = ["hello", "world"]
print(c)

# mixed types
d = ["hello", 1, 2, 3, 4, 5]
print(d)

# handling individual elements in a list
print(a[0])

# nested lists
b = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5]]
print(b)

# handling individual elements in a nested list
print(b[5][0])  # prints 1

# negative indexing starts from the end of the list
print(b[-1])  # prints [1, 2, 3, 4, 5]
print(b[-2])  # prints 5
print(b[-3])  # prints 4

#sublists and slices
# sublists is a part of a list
# sublists can be accessed using the same indexing as the parent list
# print(b[5][:n]) prints upto (n-1)th element
print(b[5][1:])  # prints [2, 3, 4, 5]
print(b[5][:3])  # prints [1, 2, 3]
print(b[5][1:3])  # prints [2, 3]

# list modification
p = [1, 2, 3, 4, 5]
q = ["x", "y", "z"]
pq = p + q
print(pq)
newP = p*2  # duplicates the list.
print(newP)

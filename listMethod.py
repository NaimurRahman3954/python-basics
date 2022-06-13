from os import remove


placedVisited = ["India", "Nepal", "Malaysia", "USA", "Canada"]

# index() method returns the index of the first occurrence of the specified value.
print(placedVisited.index("India"))
print(placedVisited.index("Nepal"))

# append() method appends the given element at the end of the list.
placedVisited.append("Singapore")
print(placedVisited)

# insert() method inserts the given element at the specified position.
placedVisited.insert(2, "Thailand")
print(placedVisited)

# remove() method removes the first occurrence of the specified value.
placedVisited.remove("Singapore")
print(placedVisited)

# sort() method sorts the list in ascending order.
# python uses the ASCII values to sort the list.
placedVisited.sort()
print(placedVisited)

# lower() argument converts the string to lowercase.
placedVisited.sort(key=str.lower)  # sorts the list in alphabetical order.
print(placedVisited)

# sorts the list in reverse alphabetical order.
placedVisited.sort(key=str.lower, reverse=True)
print(placedVisited)

# reverse() method reverses the list.
placedVisited.reverse()
print(placedVisited)

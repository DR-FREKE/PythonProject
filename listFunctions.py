myList = ["Acquired Knowledge", "Intelligence",
          "Software Engineering", "Fast cars"]
myNumList = [12, 84, 54, 90, 2, 44, 38, 21]

print(len(myList))
print(len(myNumList))

# brings the last index of the list after sorted out in alphabetical order
print(max(myList))
print(max(myNumList))

# min function is opposite of the max function. In using this function in string array or
# list, the first index of the string is produced after sorted out in alphabetical order same for max
print(min(myList))
print(min(myNumList))

# sorting a list
print("sorted list")
print(sorted(myList))
print(sorted(myNumList))


# join a string to an already existing list. cannot be used if not a string
print("\n".join(myList))

# to add an element to the end of a string we use append function
myList.append('Jelly Coder')
print(myList)

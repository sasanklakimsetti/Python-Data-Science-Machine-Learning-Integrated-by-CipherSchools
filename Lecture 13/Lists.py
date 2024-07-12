# List : data structure/ complex data type in python
fruits=["apple","cherry","banana"]
print(fruits)
fruits.append("orange") #append an element into the list
print(fruits)
fruits.extend(["grape","melon"]) #extend list with another list i.e. a new list will be appended into the list
print(fruits)
fruits.remove("cherry")
print(fruits)
fruits.pop()  # the last element inserted will be removed from the list just like pop function of stack
print(fruits)
fruits.sort()  #sorts the list in ascending order. in case of characters/ string, the sorting will be done in alphabetical order
print(fruits)
print(len(fruits))
print(fruits.index("apple"))  # prints index of the element. if not found will throw an error
print(fruits[3])  # prints the element in 3rd index i.e. 4th element of the list

print("apple" in fruits)  # check whether the element is present in the list or not

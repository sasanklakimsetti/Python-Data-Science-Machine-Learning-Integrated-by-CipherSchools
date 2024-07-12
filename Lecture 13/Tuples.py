#Tuple
# Tuple is immutable i.e. unchangable
coordinates=(10.0,20.0)
print(coordinates)
print(coordinates.count(10.0))  # returns the count of occurrence of the element in the tuple
print(coordinates[1]) #prints element at the 1st index in the tuple
print(len(coordinates))
# to change elements of the tuple, convert the tuple into list
li=list(coordinates)
li[1]="hi"
print(li)
# bringing back the tuple from the list by changing the list into tuple
coordinates=tuple(li)

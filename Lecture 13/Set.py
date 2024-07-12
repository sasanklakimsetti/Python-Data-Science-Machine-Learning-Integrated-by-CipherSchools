# Set : doesn't allow the duplicate elements
# set is unordered. so indexing doesn't exist
s={1,2,3,4,1,2,3,4}  # will not add another set of 1,2,3,4 into the set
print(s)
print(len(s))
s.add(9) # appends the element into the set
s.update({10,11,12}) # adds another set into the set
print(s)
s.remove(10)
print(s)

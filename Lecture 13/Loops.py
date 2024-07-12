# Loops : used to execute a block of code repeatedly

# For loop
# i is called iterator
for i in range(1,100000+1):
    print("Python")

print("\n")  # new line
fruits=["Apple","Banana","Cherry","Melon"]
# iterating over a list
for i in range(0,len(fruits)):
    print(fruits[i])   # printing the elements of the list based on index which is ntg but iterator

# for loop runs from 0 to range-1
print("\n")
# iterating without using range
for fruit in fruits:  #fruit is iterator in this case
    print(fruit)

print("\n")
# Iterating over a string
s="Sasank"
for char in s:
    print(char)

print("\n")
person={"name":"John","age":30}

# Iterating over a dictionary

for key,value in person.items():
    print(f"{key}: {value}")

print("\n")
# using range() function with step
for i in range(0,100000,2):
    print(i)

# step defines the gap between iterators
print("\n")
# nested for loops

for i in range(10001):
    for j in range(10001):
        print(f"i={i}, j={j}")


#using the enumerate() function
# returns the index and element of  the list
fruits=["Apple","Banana","Cherry","Melon"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


# while loop
count=0
while count<10001:
    print(count)
    count+=1

# while loop with break

count=0
while True:
    print(count)
    count+=1
    if count>100000:
        break

# while loop with continue

count=0
while count<100001:
    count+=1
    if(count%2==0):
        continue
    print(count)
    
countdown=10
while(countdown>0):
    print(countdown)
    countdown-=1
print("Let's fuck")


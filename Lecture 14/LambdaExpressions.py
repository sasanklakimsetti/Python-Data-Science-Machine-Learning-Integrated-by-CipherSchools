# Simple Lambda Function
#Definition: Lambda expressions. also known as anonymous functions, are small. unnamed functions defined using the keyword. They
# are often used for short, throwaway functions.
# Use Case in Real Life: Lambda expressions are commonly used in sorting algorithms where a custom sorting key is needed. For example
# sorting a list of tuples by the second element can be achieved using a lambda function.

# same as lambda expression in java
square=lambda x:x*x
print(square(5))

# Lambda functions in map
numbers=[1,2,3,4,5]
squares=list(map(lambda x: x*x, numbers))   # prints squares of all numbers of the map
print(squares)

# Lambda function in filter
numbers=[1,2,3,4,5,6]
even_numbers=list(filter(lambda x:x%2==0, numbers))  # filters out the odd numbers and returns only even numbers present in the list
print(even_numbers)

# Lambda function in sorted
students=[("Alice",25),("Bob",20),("Charlie,23")]
sorted_students=sorted(students, key=lambda student:students[1])
print(sorted_students)
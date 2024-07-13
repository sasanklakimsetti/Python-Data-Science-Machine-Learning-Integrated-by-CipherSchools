# Functions: a block of reusable code that performs a specific task. Functions help to modularize code, making it more organized and maintainable.

# adding two numbers
def add_numbers(a,b):
    return a+b

print(add_numbers(1000,1000))

# function with default arguments
def greet(name, message="Hello"):
    return f"{message}, {name}"

print(greet("Bob"))
print(greet("Mia","Hi"))

def fun():
    print("Hello")

fun()

def square(a):
    return a**2

a=int(input("enter a: "))
print(square(a))

# function with variable length arguments
def sum_all(*args):  # prints the sum of the tuple
    return sum(args)
print(sum_all(1,2,3,4,5))

# function with keyword arguments i.e. basically passing a dictionary as an argument
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
#calling the function
display_info(name="John",age=30,city="New Jersey")

# higher-order function
# function to apply another function to given arguments
def apply_func(func,a,b):
    return func(a,b)
def multiply(a, b):
    return a*b
print(apply_func(multiply,1234,5678))


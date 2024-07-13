"""Definition: Error handling in Python is done using try, except, else, and finally blocks. It allows you to handle exceptions gracefully and
ensure that the program continues to nm.
Use Case in Real Life: Error handling is crucial in web applications to handle unexpected situations. such as database connection errors or
invalid user inputs. Proper error handling ensures that the application can provide meaningful error messages to users and recover from errors
without crashing."""

# Basic try-except block
try:
    result=10/0
except ZeroDivisionError:
    print("Cannot divide by zero")
    
# Try-except-else block
try: 
    result=10/2
except ZeroDivisionError:
    print("Cannot divide by zero")
# if except block fails then it will get into the else block
else:
    print("Division successful")
    
#Try-except-finally block
try:
    result=10/2
except:
    print("Cannot divide by zero")
else:
    print("Division successful")
# finally block will run irrespective of the result of the try block
finally:
    print("Have a nice day!!")

# Handling multiple exceptions
try:
    number=int(input("enter a number: "))
    result=10/number
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Invalid input.. Pls input a number")
else:
    print("Division successful")
finally:
    print("Keep going")
    
# Raising exceptions
def check_positive(number):
    if(number<=0):
        raise ValueError("Number must be positive")
    

try:
    check_positive(-5)  # will be passed to the function
except ValueError as e:  # the error will be raised by the function and the exception will be stored in e
    print(e)
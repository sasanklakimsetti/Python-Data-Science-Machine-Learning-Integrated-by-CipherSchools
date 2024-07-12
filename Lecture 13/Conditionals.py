# if-elif-else statement
age=20
if age<18:
    print("Minor")
elif age>=18 and age<65:
    print("Adult")
else:
    print("Senior")

# Nested if-else
#checking number is even or odd
if age%2==0:
    if age>0:
        print("Even and greater than 0")
    elif age<0:
        print("Even and less than 0")
else:
    print("Odd")
    if age>0:
        print("Odd and greater than 0")
    elif age<0:
        print("Odd and less than 0")


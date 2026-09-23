'''
---oparators---

-->operator is used to perform a specific task b/w two oprands
eg : a+b

+ ---> specific task that is addition
a,b ---> are the operands/variables

---------- Types of operators -----------

1. Arthematic operators
2. Assigment operator
3. Relational operators
4. Logical operators
5. Comparsion operators
6. Membership operators
7. Identity operators

'''


# Arthematic operators :

first_number=int(input("Enter the first number"))
second_number=int(input("Enter the second number"))

# addition of firstnumber and secondnumber is 30

print(f"addition of {first_number} and {second_number} is {first_number+second_number}")
print(f"subtraction of {first_number} and {second_number} is {first_number-second_number}")
print(f"mul of {first_number} and {second_number} is {first_number*second_number}")
print(f"power of {first_number} and {second_number} is {first_number**second_number}")
print(f"Div of {first_number} and {second_number} is {first_number/second_number}")
print(f"Floor Division of {first_number} and {second_number} is {first_number//second_number}")
print(f"Modules of {first_number} and {second_number} is {first_number%second_number}")

# Area of the cicle

radius=float(input("Enter the radius of the circle"))
area=3.14*radius*radius
print(f"area of the circle is {area}")

# simple intrest

p=int(input("Enter the amount"))
t=float(input("Enter the time"))
r=float(input("Enter the rate of intrest"))

simple_intrest=p*t*r/100
print(f"simple intrest is: {simple_intrest}")
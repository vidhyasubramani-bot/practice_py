
#Problem:
#Read a person's name, age, and city. Print them in the given format.
#Input:

#A string name
#An integer age
#A string city
#ans
"""
name=input()
age=int(input())
city=input()
print("Name:",name)
print("Age:",age)
print("City:",city)
"""
"""
#3. Arithmetic Calculator

#Take two numbers and print:

#Addition
#Subtraction
#Multiplication
#3Division
#Floor Division
#Modulus
#Exponent
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("floor division:",a//b)
print("modulous:",a%b)
print("exponent:",a**b)
"""
"""
#string length
a=str(input("enter a word:"))
print(len(a))
"""
"""
# Largest of Three Numbers
a=int(input("enter a value:"))
b=int(input("enter a value:"))
c=int(input("enter a value:"))
x=a if a>b and a>c else b if b>a and b>c else c
print(x)
"""
"""
#Reverse a String
a=input("enter the word:")
print(a[::-1])
"""
"""
#string formation
n=input("enter a word:")
print(len(n))
print(n.upper())
print(n.lower())
print(n[0])
print(n[-1])
print(n[::-1])
"""
"""
#temperature converter
celsius=int(input("enter the celsius:"))
f=(celsius * 9 / 5)+32
print(f)
"""
"""
#Student Marks
marks=list(map(int,input("enter your marks:").split()))
total=sum(marks)
average=total/len(marks)
print("Total:",total)
print("Average:",average)
"""
"""
#List Statistics
numbers=list(map(int,input("enter numbers with using space:").split()))
print("Maximum:",max(numbers))
print("Minimum:",min(numbers))
"""
"""
#Student Report
name=input("enter your name:")
marks=list(map(int,input("enter your marks with using spaces:").split()))
total=sum(marks)
average=total/len(marks)
high=max(marks)
low=min(marks)
print("Name:",name)
print("Total:",total)
print("Average:",average)
print("Highest mark:",high)
print("Lowest mark:",low)
"""
"""
#Password Checker
n=input("enter your password:")
if len(n)>8:
    print("Invalid")
else:
    print("Valid")
    """
"""
#Shopping List
items=list(input("enter your items:").split())
print("First Item:",items[0])
print("Last item:",items[-1])
print("Total Items:",len(items))
"""
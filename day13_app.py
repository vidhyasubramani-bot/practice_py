"""
#Square Pattern
n= int(input("enter the value:"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
    """
"""
#Right Triangle 
n=int(input("enter the value:"))
for i in range(1,n+1):
    print("*"*i)
    """
"""
#Inverted Triangle
n=int(input("enter the value:"))
for i in range(n,0,-1):
    print("*"*i)
    """
"""
#Number Triangle
n=int(input("enter a value:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    """
"""
#Floyd's Triangle
n=int(input("enter the number:"))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
    """
"""
#simple function
def gree():
    print("Welcome to python")
gree()

    """
"""
#Function with Parameter
def square(num):
    print("Square =",num*num)
    
square(5)

   """
"""
#Palindrome
num=int(input("enter a number:"))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if temp==rev:
    print("Palidrome")
else:
    print("Not Palindrome")

"""


   

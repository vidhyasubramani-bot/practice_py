
"""
#area calculater
choice=int(input("enter your choice(1-3):"))
if choice==1: 
    radius=float(input("enter the radius:"))
    area=22/7*radius*radius
    print("Area of circle:",area)
elif choice==2:
 length=float(input("enter a length:"))
 breadth=float(input("enter a breadth:"))
 area=length*breadth
 print(area)
elif choice==3:
    base=float(input("enter your base:"))
    height=float(input("enter your height:"))
    area=1/2*base*height
    print(area)
else:
    print("Invalid input")
    """
"""
# Conditional Statements
year=int(input("enter your year:"))
if year%4==0:
    print("it is leaf year")
else:
    print("it is not a leaf year")
    """
"""
#grade calculator
mark=int(input("enter your mark:"))
if mark==100:
    print("O grade")
elif mark>90:
    print("A+ grade")
elif mark>80:
    print("A grade")
elif mark>70:
    print("B+ grade")
elif mark>60:
    print("B grade")
elif mark>50:
    print("C grade")
else:
    print("Fail")
    """
"""
#Simple Calculator Using if-elif
a=int(input("enter first number:"))
b=int(input("enter second number:"))
n=input("enter your choice(add(1),sub(2),mulitiple(3),division(4),modulous(5),floor division(6),exponation(7)):")
if n=="1":
    print("addition:",a+b)
elif n=="2":
    print("subtraction:",a-b)
elif n=="3":
    print("multiplication:",a*b)
elif n=="4":
    print("Division:",a/b)
elif n=="5":
    print("modulous:",a%b) 
elif n=="6":
    print("Floor division:",a//b) 
else:
    print("Invalid choice") 
    """
"""
#Print Numbers
for i in range(1,101):
    print(i)
    """

"""
#Sum of First N Numbers
n=int(input("enter the number:"))
num=0
for i in range(1,n+1):
    num+=i
print(num)
"""
"""
#Multiplication Table
n=int(input("enter the multiplication table:"))
for i in range(1,10+1):
    print(i,"*",n,"=",i*n)
    """
"""
#Factorial
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
"""
"""
#reverse
num=int(input("enter the number:"))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10
print(reverse)
"""
"""
#Count Digits
n=int(input("enter a number:"))
count=1
while n>0:
    n=n//10
    count+=1
print("Total digits:",count)
"""

   
    
    

    
    

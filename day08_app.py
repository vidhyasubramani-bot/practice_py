
"""
#boolean &comparison
n=int(input("enter the value:"))
print(n>0)
"""
#2
"""
n=int(input("enter the value:"))
print(n%2==0)
"""
#3
"""
n=int(input("enter the value:"))
print(n>100 and n<500)
"""
"""
#arithmetic operators
n1=int(input("enter the value:"))
n2=int(input("enter the value:"))
print("add:",n1+n1)
print("sub:",n1-n2)
print("mulitiply:",n1*n2)
print("division:",n1/n2)
print("modulus:",n1%n2)
"""
"""
#to calculate simple intrest
p=int(input("enter the value:"))
r=int(input("enter the value:"))
t=int(input("enter the value:"))
si=p*r*t
print("SI:",si)
"""
"""
#assignment operators
x=50
x+=10
print("after add 10:",x)

x-=5
print("after sub 5:",x)
x*=2
print("after multiply by 2:",x)
"""
"""
#ternary operators
 num=int(input("enter the value:")) 
x="even" if num%2==0 else "odd"
print(x)
"""
"""
#2
a=int(input("enter the value:")) 
b=int(input("enter the value:")) 
x=a if a>b else b
print("maximum number is:",x)
"""
"""
#identity operators
a=[1,2,3]
b=a
c=[1,2,3]
print("a is b:",a is b)
print("a is c:",a is c)
print("a is not c:",a is not c)
"""
"""
#logical operators
age=int(input("enter age:"))
citizen=input("Are you citizen?(true/false): ")
citizen = citizen =="true"
if age >= 18 and citizen:
    print("Eligible for voting")
else:
    print("Not eligible for voting")
    """
"""
#2
num=int(input("enter a number:"))
if num%3==0 or num%5==0:
    print("the number is divisible by 3 or 5")
else:
    print("the number is not divisible by 3 or 5")
"""
"""
#membership operators
n=[1,2,3,4]
if 1 in n:
  print("1 in n")
else:
    print("1 not in n")
    """
    
    
  




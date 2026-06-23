"""
#assign multiple values
a,b,c=10,20,30
print(a,b,c)
"""
"""
# assign same values
x=y=z=100
print(x,y,z)
"""
"""
#variables together
name="python"
version=3.12
print("language:",name,"version:",version)
"""
"""
#global variable
x=20
def my_function():
    print("inside function:",x)
my_function()
print("outside function:",x)

"""
"""
#changing global variable
x=10
def change_value():
    global x
    x=99
change_value()
print(x)
"""
"""
# sum of digits
num=int(input("enter the value:"))
count=0
while num>0:
    digit=num%10
    count+=digit
    num=num//10
print(count)

"""
"""
# reverse the number
n=int(input("enter the value:"))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print(reverse)
"""
    


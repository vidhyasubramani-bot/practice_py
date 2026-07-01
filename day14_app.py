"""
#1. Square Pattern
n=int(input("enter the value:"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
    """
"""
#2. Right Triangle Pattern
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
    """
"""
#3. Inverted Right Triangle
n=int(input("enter a number:"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    """
"""
#4. Number Triangle
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()  
"""
"""
#5. Repeated Number Pattern
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(i):
        print(i, end=" ")
    print()  
    """
"""
#6. Floyd's Triangle
n=int(input("enter a number:"))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
    """
"""
#largest of two numbers
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if a>b:
  print("largest value is:",a)
else:
  print("largest value is:",b)
"""
"""
#even or odd numbers
num= int(input("enter the value:"))
if (num %2==0):
    print("the number is even")
else:
    print("the number is odd")
"""  
"""
#prime numbers
num=(int(input()))
if num>1:
    for i in range(2, num):
        if num % i==0:
            print("Not Prime")
            break
    else:
        print("prime")
else:
    print("not prime")
    """
"""
# or 
num=int(input("enter the value:"))
count=0
for i in range(2,num+1):
    if num % i==0:
        count+=1
if count==1:
    print("prime")
else:
    print("Not prime")
    """
"""
# palindrome
num=(input("enter the value:"))
if num==num[ : : -1]:
    print("palindrome ")
else:
    print("not palindrome")  
    """
"""
 #multiplication table
n=int(input("enter a number:"))
for i in range(1,11):
    print(i,"*",n,"=",n*i) 
"""  
"""
num=int(input("enter the value:"))
if num<0:
    print("Negative")
elif(num>0):
    print("Positive")
else:
    print("Zero")
    """
"""
#square of the number
num=int(input("enter a number:"))
print(num*num)
"""
"""
#count characters in string
text=input("enter the word:")
print("length=",len(text))
"""


    

"""
#Sum of Digits
num=int(input("enter a number:"))
total=0
while num>0:
    digit=num%10
    total=total+digit
    num=num//10
print("sum of digit:",total)
"""
"""
#Product of Digits
n=int(input("enter a number:"))
product=1
while n>0:
    digit=n%10
    product=product*digit
    n=n//10
print("Product of Digits:",product)
"""
"""
# Fibonacci Series
num=int(input("enter a number:"))
a=0
b=1
for i in range(num):
    print(a,end=" ")
    c=a+b
    a=b 
    b=c
    """
"""
n=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if n % i==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("Not a prime")
    """
"""
# Prime Numbers Between Two Limits     
start=int(input("enter a number:"))
end=int(input("enter a number:"))
for num in range(start,end+1):
  if num>1:
      count=0
      for i in range(2,num):
          if num%i==0:
              count+=1
      if count==0:
        print(num,end=" ")
        """
          

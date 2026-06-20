"""
#count the number of digits
num=int(input("enter the number:"))
count=0
while num>0:
    count+=1
    num//=10
print("count:",count)
"""
"""
#reverse the number
num=int(input("enter the value: "))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10
print("reverse=",reverse)
"""

"""
#factorial
num=int(input("enter the value:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("factorial:",fact)
"""
    
"""
#factors of the numbers
num=int(input("enter the value:"))
print("factors are:")
for i in range(1,num+1):
    if num%i==0:
     print(i)
"""



    

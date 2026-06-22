n = 5

for i in range(2*n-1):
    for j in range(2*n-1):
        if ((i==0 and j not in [0,n-1,2*n-2]) or
            (i==1 and j in [0,n-2,n,2*n-2]) or
            (i-j==2) or
            (i+j==2*n+2)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
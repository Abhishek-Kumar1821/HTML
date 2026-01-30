'''# Pyramid Star Pattern
n = 10

for i in range(1, n + 1):
    # print spaces
    print(" " * (n - i), end="")
    # print stars
    print("*" * (2 * i - 1))
n=int(input("Enter the height of the pattern:"))
l=1
for k in range(1,n+1):
    for i in range(n,k,-1):
        print(" ",end=" ")
    for j in range(1,l+1):
            print('*',end=' ')
    l=l+2
    print()'''
#Reverse pyramid star pattern
n=int(input("Enter the height of the pattern:"))
l=2*n-1
for k in range(1,n+1):
    for i in range(1,k):
        print(" ",end=" ")
        for j in range(l,0,-1):
            print('*',end=' ')
        l=l-2
        print()


        
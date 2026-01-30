'''range1=int(input("Enter starting range"))
range2=int(input("Enter final range"))
sum=0
for i in range(range1+1,range2):
    print(i,end='\t')
    sum=sum+1
print("\n sum of all number=",sum)'''
#program to print sum of all even and odd number b/w given range 
range1=int(input("Enter starting range"))
range2=int(input("Enter final range"))
esum=0
osum=0
for i in range(range1+1,range2):
    print(i,end='\t')
    if(i%2==0):
        esum=esum+i
    else:
        osum=osum+i
asum=esum+osum
print("------------------")
print("sum of all even value=",esum)
print("sum of all odd vakue=",osum)
print("-------------------")
print("sum of all number=",asum)
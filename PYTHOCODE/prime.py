'''n=int(input("Enter the range up to which you want prime numbers:"))
temp=n
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
    if(temp==rev):
        print("The number is prime.")
    else:
        print("The number is not prime.")
        '''
#Program to check prime number
num=int(input("Enter the number to check if it is prime or not:"))
div=True
for i in range(2,num):
    if(num%i==0):
        div=False
if(div==True):
   print(num,"is a prime number")
else:
    print(num,"is not a prime number")
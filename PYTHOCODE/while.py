'''count=1
while count<=5 :
    print("Hello world")
    count+=1
print(count)
#print number from 1 to 8+

i=8
while i>=1:
    print(i)
    i-=1

print("loop ended")    
    
n=int(input("Enter the number"))
i=1
while i<=10:
     print(n*i)
     i+=1 

#print the elements of the following list using a loop:
nums=[1,4,9,16,25,36,49,64,81,100] 
idx=0
while idx < len(nums):
    print(nums[idx])
    idx+=1 '''
nums=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<len(nums):
     if(nums[i]==x):
          print("FOUND at idx",i)
     else:
          print("finding..")
     i+=1
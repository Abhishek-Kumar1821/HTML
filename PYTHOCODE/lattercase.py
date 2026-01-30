#wap in python to reach continuous character up * character and print number of Uppercase lowercase and numbers available 
#in their apperance
ch=input("Enter any character:")
num_count=0
up_count=0
low_count=0
if(ch >='0' and ch<='9'):
    num_count=num_count+1
elif(ch >='a' and ch<='z'):
    low_count=low_count+1
elif(ch>='A' and ch<='Z'):
     up_count=up_count+1
while(ch !='*'):
    ch=input("Enter any character:")
    if(ch >='0' and ch<='9'):
        num_count=num_count+1
    elif(ch >='a' and ch<='z'):
        low_count=low_count+1
    elif(ch >='A' and ch<='Z'):
        up_count=up_count+1
print("Number of number count=",num_count)
print("Number of Upper count=",up_count)
print("Number of Lower count=",low_count)       
      
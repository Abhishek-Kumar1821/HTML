#wap in python to print all armstrong numbers between 100 to 999
num=101
while num<999:
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum=digit**3+sum
        temp=temp//10
        if sum==num:
            print(sum)
            num=num+1
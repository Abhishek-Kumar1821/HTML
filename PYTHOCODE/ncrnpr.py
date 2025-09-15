
n=int(input("Enter the value of n=>"))
r=int(input("Enter the value of r=>"))
fn=1
fnr=1
res=0
if n>r:
    i=0
    while(i<=n):
        fn=fn*i
        i=i+1
    print(n,"p",r,"=",(fn/fnr))
else:
    print("Value of n is less than r")
    '''

n=int(input("Enter the value of n=>"))
r=int(input("Enter the value of r=>"))

fn=1
fnr=1
res=0
fr=1
if n>r:
    i=0
    while(i<=n):
        fn=fn*i
        if i<=(n-r):
            fnr=fnr*i
            if i<=r:
                fr=fr*i
        i=i+1
    print(n,"p",r,"=",(fn/fnr*fr))
else:
    print("Value of n is less than r")
'''
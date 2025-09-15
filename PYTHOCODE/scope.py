#wap in python to create a UDF to understand the concept of Local and Global variable
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
d=int(input("Enter 4rth number:"))
e=int(input("Enter 5th number:"))

def Addition():
    global i
    i=a+b
    return i
def Subtract():
    global j
    j=a-b
    return j
def Product():
    global k 
    k=a*b
    return k
def show():
   print("Sum=",i)
   print("Subtract=",j)
   print("Product=",k) 
   c=Addition()
   d=Subtract()
   e=Product()
print("Sum",c)
print("Subtract",d)
print("Product",e)
print("Sum=",i)
print("Subtract=",j)
print("Product=",k)
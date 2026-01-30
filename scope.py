num1=10
print("Global variables num1=",num1)
def fun(num2):
    print("In function - local variables num2=",num2)
    num3=30
    print("Local variable num3=",num3)
    fun(20)
    print("Global variables num1=",num1)
    print("Global variables num3=",num3)
    
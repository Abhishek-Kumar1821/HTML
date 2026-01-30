'''def AreaCircle(r):
    ar=3.14*r*r
    return (ar)
def CircumfrenceCircle(r):
    cir=(2*3.14*r)
    return(cir)
radius=int(input("Enter the radius of circle:"))
area=AreaCircle(radius)
circum=CircumfrenceCircle(radius)
print("Area of circle is=",area)
print("Circumfrence of circle is=",circum)
#Using lambda function
area=lambda r:3.14*r*r
circum=lambda r:2*3.14*r
r=eval(input("Enter the radius of circle:"))
print("Area of circle is=",area(r))
print("Circumfrence of circle is=",circum(r))
#SI and CI Calculate using lambda function
Si=lambda p,r,t:(p*r*t)/100
P=eval(input("Enter the principle amount:"))
R=eval(input("Enter the rate of interest:"))
T=eval(input("Enter the time(In months):"))
print("Total interest is=",Si(P,R,T))
#CI=lambda p,r,t:(p*(1+r/100)**t)-p
compound_interest=lambda p,r,t:(p*(1+r/100)**t)-p
P=float(input("Enter the principle amount:"))
R=float(input("Enter the rate of interest:"))
T=float(input("Enter the time(in years):"))
CI=compound_interest(P,R,T)
print("Compound interest=",CI)'''
#Wap in python to convert Fahrenheit to Celsius 
Fahrenheit=lambda f:(f-32)*5/9
Celsius=lambda c:(c*9/5)+32
f=float(input("Enter the temperature in Fahrenheit:"))
print("Temperature in Celsius is=",Fahrenheit(f))
c=float(input("Enter the temperature in celsius:"))
print("Temperature in Fahrenheit is=",Celsius(c))




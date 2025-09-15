#write a program in python to print simple and compound interest of given p, t, r
p=float(input("Enter the principle amount:"))
t=int(input("Enter the time in years:"))
r=float(input("Enter the rate of interest:"))
si=(p*t*r)/100
ci=p*(1+r/100)**t
print("Simple Interest is:",si)
print("Compound Interset is:",ci)
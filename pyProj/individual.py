import math as mt

print("Variant 7, trapezoid perimeter")

a = float(input("Base a: "))
b = float(input("Base b: "))
h = float(input("Height h: "))

l = float(mt.sqrt((mt.pow((b-a)/2, 2))+(mt.pow(h, 2))))
perimeter = float(a + b + 2*l)
print("Perimeter is: %.3f" % (perimeter))
import math

print("Variant 7\n")

h = int(input("Hours: "))
m = int(input("Minutes: "))
# s = int(input("Seconds: "))

t = float(h*60 + m)
alfa = float(360*(t % 60)/60)

print("Degree: %.2f" % (alfa))
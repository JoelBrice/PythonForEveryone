##Python for everyone Exercise 3


hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
except Exception as e:
    raise

extra_pay = 0.0

if h>40.0:
    pay = ((h-40.0)*1.5+ 40)*r
else:
    pay = r*h

print(pay)

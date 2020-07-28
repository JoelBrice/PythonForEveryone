def computepay(h,r):
    hrs = 0.0
    rate = 0.0
    pay = 0.0
    try:
        hrs = float(h)
        rate = float(r)
    except:
        print("Not in range!")

    if hrs>40.0:
        pay = ((hrs-40)*1.5+40)*rate
    else:
        pay = hrs*rate
    return pay

hrs = input("Enter Hours: ")
rate = input("Enter rate: ")

p = computepay(hrs,rate)
print("Pay",p)

"""Check that the score is between the range and display the score level according to the score"""


score = input("Enter Score: ")
s = 0.0
try:
    s = float(score)
except:
    print("Error out of range!")


if s >=0 and s<=1:
    if s>= 0.9:
        print("A")
    elif s >=0.8:
        print("B")
    elif s>=0.7:
        print("C")
    elif s>=0.6:
        print("D")
    elif s<0.6:
        print("F")
else:
    print("Out of range")

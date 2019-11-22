Number=int(input("Enter your number"))
Temp=Number
Sum=0
while(Number>0):
    Remainder=Number%10
    Sum=Sum+(Remainder*Remainder*Remainder)
    Number=Number//10
if Temp==Sum:
    print("Number is arms")
else:
    print("Number is not arms")

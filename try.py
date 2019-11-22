Number = int(input("Please Enter any Number: "))
Original=Number
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print("\nReverse of entered number is = " ,Reverse)
Diff=Reverse-Original
if Diff==0:
    print("Number is palindrome")
else:
    print("Number is not Palindrome")

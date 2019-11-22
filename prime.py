num=int(input("enter your number "))
cnt=0
for i in range(1,num+1):
    if num%i==0:
        cnt=cnt+1
if cnt>2:
    print("number is not prime")
 else:
        if num==1:
            print(num,"is neither prime nor composite")
        else:
            print("number is prime")
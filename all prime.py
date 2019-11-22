terms=int(input("enter number of terms "))

for num in range(1,terms+1):
    count=0
    for j in range(1,num+1):
        if num%j==0:
            count=count+1
    if count==2:
        print(num)

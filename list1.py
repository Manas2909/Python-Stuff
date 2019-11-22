l=[]
sum=0
limit=int(input("enter the limit of the list: "))

for i in range(0,limit):
    elem=int(input("enter the element: "))
    l.append(elem)
    sum=sum+elem
print(l)
print(sum)
largest=0
for i in l:
    if i%2==0:
        print("even= ",i)
        
print(max(l))
l2=[]
for j in range(0,limit):
    for j in l:
        num=j**3
        l2.append(num)
    break
print(l2)

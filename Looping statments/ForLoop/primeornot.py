num=int(input("enter a number:"))#10
for i in range(2,num): #2,3,4..10
    if(num%i==0): #10%2==0
        flag=1 #1
        break
    else:
        flag=0

if(flag>0):
    print("not prime")
else:
    print("prime")



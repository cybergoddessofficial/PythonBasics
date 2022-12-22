lst=[1,2,3,4,5,6]
element=int(input("Enter the number:"))
flag=0
for i in lst:
    if(element==i):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("element found")
else:
    print("Element not found")

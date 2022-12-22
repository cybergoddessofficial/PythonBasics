lst=[1,3,4,2]
element=int(input("enter a number"))#6
lst.sort()
lower=0 #1
upper=len(lst)-1 #3
#lst    1   2   3   4
while(lower<upper): #1<3
    sum=lst[lower]+lst[upper]#lst[1] +lst[3]=2+4=6
    if(sum==element):#6==6
        print("Pair found",lst[lower],lst[upper]) #lst[1]lst[3] 2,4
        break
    elif(sum>element):#9
        upper-=1
    elif(sum<element):#5<6
        lower+=1 #lower=lower+1=0+1=1
    else:
        print("element not found")


# print(upper)
# print(lst[2])
#list   :   1  2   3   4
#index  :   0   1   2   3


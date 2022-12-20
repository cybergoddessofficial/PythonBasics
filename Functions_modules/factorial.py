def fact(num):
    f=1
    for i in range(1,num+1): #i=1,2,3,4,5
        f=f*i #f=1*1=1  f=1*2=2 f=2*3
    print(f)



n=int(input("enter a nuj:"))
fact(n) #function calling
#5=1*2*3*4*5
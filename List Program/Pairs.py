lst=[1,2,3,4]
# lst[0]    :   1
#   lst[2]  :   3
#  starting index:0 ending index:3


element=int(input("Enter a nummber:")) # 6(2,4) 5(2,3)
for item in lst:    #   1   2    outer loop
    for i in lst:   #   1   2   3   4    inner loop
        sum=0
        if(item !=1):
            sum=item+i  #sum=2+1=3  2+2=4   2+3=5   2+4=6
            if(element==sum):#6==6
                print(item,i)#(2,4)
                break
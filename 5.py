#1010
#0100
#0011
#1001
#op=1010
x = list(map(int, input("Enter  4 digit binary value: ").split()))
for i in x:
    y=i
    sum=0
    j=0
    while(i!=0):
        r=i%10
        sum=sum+(r*(2**j))
        j=j+1
        i=i//10
    if(sum%5==0):
        print(y)
            
    

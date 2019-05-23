l1=[2,3,4,5,6,7,8,9,10,23,43,14,66]
emax=0
omax=0
for i in l1:
    if(i%2==0):
        if(i>emax):
            emax=i
    else:
         if(i>omax):
             omax=i
print("max even value is",emax)
print("max odd value is",omax)

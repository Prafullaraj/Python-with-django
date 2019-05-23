#l3=[1,2,3,4,5,6,1,3,5]
#op [1,3,5]
l2=[1,1,1,2,2,3,3,4,5,5,6]
l3=[]
l3=l2
for i in l2:
    count=0
    for j in l3:
        if(i==j):
            l3.remove(j)
            count=count+1
    if(count>=1):
        for k in range(count):
            print(i)

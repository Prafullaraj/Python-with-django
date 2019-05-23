l6=[]
for i in range(1,30):
    for j in range(i,30):
        for k in range(j,30):
            if(i**2+j**2==k**2):
                l6.append(i)
                l6.append(j)
                l6.append(k)

l3=[1,2,3,4,5,6,7,8,9,(2,4),4,6,7,8,3]
count=0
for i in l3:
    if(type(i) is not tuple):
        count=count+1
    else:
        break
print(count)        

#game
point1=0
point2=0
l3=[]
l4=[]
l1=[['iron man', '1000'],
['spider man','500'],
['captain america', '600'],[ 'vision','900'],['thor', '950']]

l2=[[ 'mandarin', '200'],
['Loki','600'],
['thanos','1100'],['Ebony Maw', '900'],['Proxima Midnight', '550']]
print("Avenger team\n",l1)
print("Thanos team\n",l2)
for i in range(0,5):
    l3.append(int(l1[i][1]))
    l4.append(int(l2[i][1]))
while(len(l3)!=0 or len(l4)!=0):
    if(max(l3)>=max(l4)):
        point1=point1+1
        l3.remove(max(l3))
        l4.remove(max(l4))
    else:
        point2=point2+1
        l3.remove(max(l3))
        l4.remove(max(l4))
if(point1>point2):
    print("\n****Avengers win****")
else:
    print("\n****Thanos win****")

#wapp list=['goa','mp','up']
import re
import string
import os

l1=['goa','jharkhand','mp']
k=0
for i in l1:
    sum=0
    for j in i:
        sum=sum+ord(j)
    a=str(sum)
    l1[k].replace(l1[0],a)
    k=k+1
print(l1)

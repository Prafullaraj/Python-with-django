#d={1:{name:raj,age:21},2:{name:ayush,age:21}}
d={}
x=int(input("Enter the number of students:"))
d1={}
for i in range(1,x+1):
    name=input("enter the name")
    d1.update({'name':name})
    age=int(input("enter the age"))
    d1.update({'age':age})
    d.update({i:d1})
print(d)    
    

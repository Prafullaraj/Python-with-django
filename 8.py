#max leng of string in list
#l1=['abc','abcd','abcde','ab']
l1=['abc','abcd','abcde','ab']
max=0
for i in l1:
    count=0
    x=len(i)
    if(x>max):
        max=x
        j=i
print(max)
print(j)

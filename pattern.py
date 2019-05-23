#A
#A B
#B c D
#D E F G
#G H I J K
k=65
for i in range(0,5):
    for j in range(k,k+i+1):
        print(chr(j),end='')
    print("\r")
    k=k+i  

import random
d={'moblie':'abc','internet':'xyz','Bus':'shj','car':'bhs','aeroplane':'hhh'}
total_answer=list(d.values())
b=[]
for k,v in d.items():
    act_value=[v]
    #print(act_value)
    wro_value=[x for x in total_answer if x not in act_value]
    #print(wro_value)
    option=[act_value+random.shuffle(wro_value[:3])]
    #print(option)
    random.shuffle(option)
    #print("who invengted "+" "+k)
    print(option)    

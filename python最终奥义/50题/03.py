list=[]
for i in range(1,168):
    l = i * i
    number = l - 268 
    list.append(l)
    for a in range(i):
        if list[i-1] - list[a] == 168:
            print (number)
            
        

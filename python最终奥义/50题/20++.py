p1 = ['a','b','c']
p2 = ['x','y','z']
l1 = []
l2 = []
l3 = []
for i in p1:
    for j in p2:
        if(i=='a' and j != 'x'):
            l1.append([i,j])
        elif(i=='b'):
            l2.append([i,j])
        elif(i=='c' and j !='x' and j !='z'):
            l3.append([i,j])
for m in range(len(l1)):
    for n in range(len(l2)):
        for o in range(len(l3)):
            if (l1[m][1] != l2[n][1]) and (l1[m][1] != l3[o][1]) and (l2[n][1] != l3[o][1]):
                print('对战情况如下:')
                print(str(l1[m][0]) + ' 对战 ' + str(l1[m][1]))
                print(str(l2[n][0]) + ' 对战 ' + str(l2[n][1]))
                print(str(l3[o][0]) + ' 对战 ' + str(l3[o][1]))

i=0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b & b!=c &c!=a:
                i=i+1
                print(str(a)+str(b)+str(c))
print('一共有'+str(i)+'个值')
                

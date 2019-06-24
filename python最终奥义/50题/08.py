for i in range(1,10):
    for j in range(i):
        m = (j + 1) * i
        print(str(j + 1) + '*' + str(i) + '=' + str(m),end=' ')
    print('')

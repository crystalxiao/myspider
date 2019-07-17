with open('theres.ts', 'wb') as f:
    for i in range(2635):
        print(i)
        with open('%d.ts' % i, 'rb') as t:
            f.write(t.read())
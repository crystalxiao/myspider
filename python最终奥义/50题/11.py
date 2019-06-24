list = list(range(101,201))
for i in range(101,201):
    j = int(i ** 0.5) + 1
    for a in range(2,j + 1):
        if i % a == 0:
            list.remove(i)
            break
print('共有' + str(len(list)) + '个素数，他们分别是:' + str(list))

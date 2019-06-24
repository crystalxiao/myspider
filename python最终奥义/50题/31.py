a = input('原数组输入空格隔开').split()
a = list(map(int,a))
b = int(input('插入数:'))
a.append(b)
if a[0] > a[1]:
    a.sort(reverse = True)
else:
    a.sort()
print(a)

a = input('请输入空格隔开:').split()
a = list(map(int,a))
n = len(a)
m = int(input('请输入m:'))
for i in range(m):
    a.insert(m * 2,a[0])
    del a[0]
for j in range(m):
    a.insert(0,a[n - 1])
    del a[n]
print(a)

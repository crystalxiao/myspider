a = input('请输入数组，空格分割开:').split()
a = list(map(int,a))
for i in range(len(a)):
    if a[i] == max(a):
        a[0],a[i] = a[i],a[0]
        break
for j in range(len(a)):
    if a[j] == min(a):
        a[len(a) - 1],a[j] = a[j],a[len(a) - 1]
        break
print(a)

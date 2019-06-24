def delate(list,yushu):
    list1 = []
    for m in range(len(list)):
        if not((m + 1) % 3 == 3 - yushu) | ((yushu == 0) & ((m + 1) % 3 == 0)) :
            list1.append(list[m])
    yushu = (len(list) - (3 - yushu)) % 3  #多余的数（下一次的数列需要先被3减再%3）
    list = list1
    if len(list) > 2:
        delate(list,yushu)
        return delate(list,yushu)
    else:
        return list[1]
n = int(input('输入n的值'))
a = [1 for lengths in range(n)]
for i in range(n):
    a[i] = i + 1
print('第' + str(delate(a,0)) + '个人')






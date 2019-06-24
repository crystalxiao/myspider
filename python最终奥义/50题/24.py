n = input('用空格分隔多个数据:')
list = n.split()
for i in range (len(list) // 2):
    list[i],list[len(list) - 1 - i] = list[len(list) - 1 - i],list[i]
print(list)

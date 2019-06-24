x = int(input('请输入x的值:'))
y = int(input('请输入y的值:'))
z = int(input('请输入z的值:'))
list = []
list.append(x)
list.append(y)
list.append(z)
list.sort()
print(str(list[0]) + '\t' + str(list[1]) + '\t' + str(list[2]))

n = int(input('几个数相加:'))
a = int(input('请输入a的数值:'))
total = 0
for i in range(1,n + 1):
    number = 0
    for j in range(i):
        number = a * (10 ** j) + number
    total = total + number
print('结果是:' + str(total))

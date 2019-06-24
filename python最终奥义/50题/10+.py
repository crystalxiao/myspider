m = int(input('请输入第几个月:'))
total = [2 for i in range(m)]
old = [0 for i in range(m)]#呆了三个月的兔子
old[2] = 2
total[2] = 4
new = old#新出生的兔子
for i in range(m):
    if i > 2:
        new[i] = new[i - 3] + old[i - 1]
        old[i] = new[i]
        total[i] = total[i - 1] + new[i]
        #每个月新出生的兔子和呆了三个月的兔子是一样多的
        #为了便于理解不直接对等，不使用一个列表
print('生到这个月一共有' + str(total[m - 1]) + '只兔子')
    
    

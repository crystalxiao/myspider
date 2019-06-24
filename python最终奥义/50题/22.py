def he(n):
    total = 0
    for i in range(n + 1):
        total = total + i
    return total
n = int(input('请输入值:'))
totals = 0
for m in range(n + 1):
    totals = totals + he(m)
print('和为' + str(totals))

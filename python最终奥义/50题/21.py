n = int(input('请输入:'))
list = [1,2]
total = 0
for a in range(n + 1):
    if a > 1:
        list.append(list[a - 1] + list[a - 2])
for b in range(n):
    total = total + list[b + 1] / list[b]
print('和为' + str(total))

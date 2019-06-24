a = input('输入八进制数字：')
n = int(a)
total = 0
for i in range(len(a)):
    m = n // (10 ** i) % 10
    total = total + m * (8 ** i)
print('十进制数字为:' + str(total))

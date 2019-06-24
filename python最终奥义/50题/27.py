num = input('输入')
length = len(num)
n = int(num)
for i in range(length // 2):
    a = n // 10 ** i % 10
    b = n // 10 ** (length - 1 - i) % 10
    if a != b:
        print('不是回文数')
        break
    elif (a == b) & (i == (length // 2) - 1):
        print('是')

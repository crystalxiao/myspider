num = input('输入')
leng = len(num)
n = int(num)
total = 0
list = [0 for le in range(leng)]
for i in range(leng):
    list[i] = n // (10 ** i) % 10
    total = total + list[i] * (10 ** (leng - 1 - i))
print('长度' + str(leng))
print('倒过来' + str(total))

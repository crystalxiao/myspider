import math
a = input('输入空格隔开').split()
b = list(map(int,a))
length = len(b)
wei = int(math.sqrt(length))
total_1 = 0
total_2 = 0
for n in range(wei):
    total_1 = total_1 + b[n * wei + n]
    total_2 = total_2 + b[(n + 1) * wei - 1 - n]
if wei % 2 == 0:
    total = total_1 + total_2
else:
    total = total_1 + total_2 - b[(length - 1) // 2]
print('和为' + str(total))

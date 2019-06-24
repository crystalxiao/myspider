n = int(input('请输入第几次下落:'))
h = 10
if n == 1:
    total = 10
else:
    total = 10
    for i in range(n - 1):
        h = h / 2
        total = total + h * 2
h = h / 2
print('共经过了' + str(total) + '米')
print('第' + str(n) + '次反弹了' + str(h) + '米')

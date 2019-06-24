n = int(input('请输入要求自幂数的位数:'))
list=[0 for a in range(n + 1)]
for i in range(10 ** (n - 1),10 ** n - 1):
    total = 0
    for weishu in range(1,n + 1):
        list[weishu] = i // 10 ** (weishu - 1) % 10
        total = total + (list[weishu]) ** n
    if total == i:
        print(i)

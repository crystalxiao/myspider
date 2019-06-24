def jiangjin(l):
    if l <= 100000:
        money = l * 10 / 100
    elif l <= 200000:
        money = 10000 + (l - 100000) * 7.5 / 100
    elif l <= 400000:
        money = 17500 + (l - 200000) * 5 / 100
    elif l <= 600000:
        money = 27500 + (l - 400000) * 3 / 100
    elif l <= 1000000:
        money = 33500 + (l - 600000) * 1.5 / 100
    else:
        money = 39500 + (l - 1000000) * 1 / 100
    print (money)
    l = input('请输入利润:')
    l = int(l)
    jiangjin(l)
l = input('请输入利润:')
l = int(l)
jiangjin(l)

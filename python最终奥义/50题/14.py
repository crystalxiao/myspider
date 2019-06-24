def gbs(a,b):
    for i in range(1,b + 1):
        x = a * i
        for k in range(a + 1):
            y = b * k
            if x == y :
                print('最小公倍数是:'+ str(x))
                return
            elif x > y:
                continue
            else:
                break
def gys(a,b):
    list = []
    for i in range(2,b + 1):
        if a % i == 0:
            if b % i == 0:
                list.append(i)
    print('最大公约数是:' + str(list[len(list) - 1]))
a=input('请输入m:')
b=input('请输入n:')
a=int(a)
b=int(b)
gbs(a,b)
gys(a,b)

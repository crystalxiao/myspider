def hnt(n, a, b, c):
    if n == 1:
        print('把' + a + '的第一个圆盘移动到' + c)
    else:
        hnt(n - 1, a, c, b)
        print('把' + a + '的第一个圆盘移动到' + c)
        hnt(n - 1, b, a, c)
def han(n):
    hnt(n, 'A', 'B', 'C')
    n = input('请输入圆盘数:')
    n = int(n)
    han(n)
n = input('请输入圆盘数:')
n = int(n)
han(n)

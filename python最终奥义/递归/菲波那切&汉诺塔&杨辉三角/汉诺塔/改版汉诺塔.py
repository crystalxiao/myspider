def pt(a,b,m,n):
    if (m <= n) & (m > 0):
        print('把' + str(a) +'的第'+ str(m) + '大的铁饼放到' + str(b) + '上')
    else:
        return None
def hnt(n):
    if n % 2 == 0:
        for i in range(n // 2):
            pt('a','b',2 * i + 1,n)
            pt('c','b',2 * i,n)
            pt('a','c',2 * i + 2,n)
            pt('b','c',2 * i + 1,n)
    else:
        for i in range((n + 1) // 2 ):
            pt('a','b',2 * i + 1,n)
            pt('c','b',2 * i,n)
            pt('a','c',2 * i + 2,n)
            pt('b','c',2 * i + 1,n)
    print('移动完成,OJBK')
    n = input('请输入铁饼数:')
    n = int(n)
    hnt(n)
n = input('请输入铁饼数:')
n = int(n)
hnt(n)

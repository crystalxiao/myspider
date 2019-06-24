def fbnq(n):
    a = 0
    b = 1
    fb = 0
    if n < 1:
        print('菲波那切数列有第零项？')
        n = input('菲波那切第n项是:')
        n = int(n)
        fbnq(n)
    elif n == 1:
        fb = 1
    else:
        m = n // 2
        for i in range(m):
            a = a + b
            b = a + b
            if n % 2 == 0:
                fb = a
            else:
                fb = b
    print("你要求的数值是:" + str(fb))
    n = input('菲波那切第n项是:')
    n = int(n)
    fbnq(n)
n = input('菲波那切第n项是:')
n = int(n)
fbnq(n)

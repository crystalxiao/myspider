def panduan(n):
    fb = [0 for lengths in range(n + 2)]
    fb[0] = 1
    fb[1] = 1
    for i in range(n + 2):
        if i < 2:
            fb[i] = fb[i]
        else:
            fb[i] = fb[(i - 1)] + fb[(i - 2)]
        if fb[i] < n:
            continue
        elif fb[i] == n:
            print('它是菲波那切数列的第' + str(i + 1) + '项')
            break
        else:
            print('它不是菲波那切数列的值')
            break
    n = input('请输入你要判断的数值:')
    n = int(n)
    panduan(n)
n = input('请输入你要判断的数值:')
n = int(n)
panduan(n)

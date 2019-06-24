def queen(chess,m = 0):
    if m == 8:
        print(chess)
        return 0
    for x in range(8):
        chess[m] = x
        panduan = 1
        for y in range(m):
            if x == chess[y] or m - y == abs(x - chess[y]):
                panduan = 0
        if panduan == 1:
            queen(chess,m+1)
queen([None]*8)

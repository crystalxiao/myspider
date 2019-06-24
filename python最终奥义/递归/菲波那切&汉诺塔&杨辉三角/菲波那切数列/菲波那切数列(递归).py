def fbnq(n):
    fbnq(1) = 1
    fbnq(2) = 1
    fbnq(n) = fbnq(n-1)+fbnq(n-2)
    return fbnq(n)
print(fbnq(10))

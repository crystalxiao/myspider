for a in range(1,10):
    for b in range(10):
        for c in range(10):
            d = 100 * a + 10 * b + c
            if d == a ** 3 + b ** 3 + c ** 3:
                print(str(d))

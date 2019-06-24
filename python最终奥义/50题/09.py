for i in range(8):
    if i % 2 == 0:
        for j in range(4):
            print('▇',end='  ')
        print()
    else:
        for j in range(4):
            print('  ',end='▇')
        print()

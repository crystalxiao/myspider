def yanghui(length):
    list = [[0 for col in range((2 * length - 1))]for row in range(length)]
    for row in range(length):
        for col in range(2 * length - 1):
            if (col == (length - row - 1))|(col == (length + row - 1)):
                list[row][col] = 1
            elif (col > (length -row - 1)) & (col < (length + row - 1)) & ((col - (length - row - 1)) % 2 ==0):
                list[row][col] = list[(row - 1)][(col - 1)] + list[(row - 1)][(col + 1)]
            else:
                list[row][col] = " "
            print(list[row][col],end = "")
        print("\n")
    length = int(input("请输入要打印的行数:"))
    yanghui(length)
length = int(input("请输入要打印的行数:"))
yanghui(length)

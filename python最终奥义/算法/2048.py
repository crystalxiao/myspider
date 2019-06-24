import random

def main2048(game_map):

    #寻找0:
    def space_zero(game_map):
        list_zero = []
        for row in range(4):
            for col in range(4):
                if game_map[row][col] == 0:
                    list_zero.append(row * 10 + col)
        return list_zero

    #定义一个生成2的方法
    def birth_two(game_map):
        new_two = random.randint(0,len(space_zero(game_map)) - 1)
        new_two_space = space_zero(game_map)[new_two]
        row = new_two_space // 10
        col = new_two_space % 10
        game_map[row][col] = 2

    '''#判断是否为0：
    def is_zero(a,b):
        if game_map[a][b] == 0:
            return True
        else:
            return False'''

    #相同方块合并规则
    def levelup(a,b):
        if a == b:
            a = a * 2
            b = 0
        return a,b
            #print(a,b)
    
    #方块与0合并规则
    def levelzero(a,b):
        if b == 0:
            #print('yes')
            b = a
            a = 0
        return(a,b)
            #a = 0
            #print(a,b)

    #上下左右移动
    def move_left(game_map):
        for i in range(3):
            for row in range(4):
                for col in [3,2,1]:
                    game_map[row][col],game_map[row][col - 1] = levelzero(game_map[row][col],game_map[row][col - 1])
        for row in range(4):
            for col in range(3):
                game_map[row][col],game_map[row][col + 1] = levelup(game_map[row][col],game_map[row][col + 1])
        for i in range(3):
            for row in range(4):
                for col in [3,2,1]:
                    game_map[row][col],game_map[row][col - 1] = levelzero(game_map[row][col],game_map[row][col - 1])

    def move_right(game_map):
        for i in range(3):
            for row in range(4):
                for col in range(3):
                    game_map[row][col],game_map[row][col + 1] = levelzero(game_map[row][col],game_map[row][col + 1])
        for row in range(4):
            for col in [3,2,1]:
                game_map[row][col],game_map[row][col - 1] = levelup(game_map[row][col],game_map[row][col - 1])
        for i in range(3):
            for row in range(4):
                for col in range(3):
                    game_map[row][col],game_map[row][col + 1] = levelzero(game_map[row][col],game_map[row][col + 1])

    def move_top(game_map):
        for i in range(3):
            for col in range(4):
                for row in [3,2,1]:
                    game_map[row][col],game_map[row - 1][col] = levelzero(game_map[row][col],game_map[row - 1][col])
        for col in range(4):
            for row in range(3):
                game_map[row][col],game_map[row + 1][col] = levelup(game_map[row][col],game_map[row + 1][col])
        for i in range(3):
            for col in range(4):
                for row in [3,2,1]:
                    game_map[row][col],game_map[row - 1][col] = levelzero(game_map[row][col],game_map[row - 1][col])

    def move_bottom(game_map):
        for i in range(3):
            for col in range(4):
                for row in range(3):
                    game_map[row][col],game_map[row + 1][col] = levelzero(game_map[row][col],game_map[row + 1][col])
        for col in range(4):
            for row in [3,2,1]:
                game_map[row][col],game_map[row - 1][col] = levelup(game_map[row][col],game_map[row - 1][col])
        for i in range(3):
            for col in range(4):
                for row in range(3):
                    game_map[row][col],game_map[row + 1][col] = levelzero(game_map[row][col],game_map[row + 1][col])

    def keymove(game_map):
        wsad = input('请输入WSAD+回车键来控制上下左右:')
        if wsad == 'w' or wsad == 'W':
            move_top(game_map)
        elif wsad == 's' or wsad == 'S':
            move_bottom(game_map)
        elif wsad == 'a' or wsad == 'A':
            move_left(game_map)
        elif wsad == 'd' or wsad == 'D':
            move_right(game_map)
        else:
            print('输入错误，游戏结束')
        birth_two(game_map)

    print(str(game_map[0]) + '\n' + str(game_map[1]) + '\n' + str(game_map[2]) + '\n' + str(game_map[3]))
    keymove(game_map)
    main2048(game_map)

start = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
main2048(start)
    

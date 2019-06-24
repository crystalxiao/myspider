#判断是否为相同数字
def like(n):
    length_str = len(str(n))
    length_set = len(set(str(n)))
    if length_str == length_set:
        return True
    else:
        return False

#循环判断是否相同数字及奇偶性
total = 0
for i in range(1,100000000):
    if like(i) == True:
        if i % 2 == 1:
            total += 1
print('共有' + str(total) + '个奇数')
    

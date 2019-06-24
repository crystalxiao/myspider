a = int(input('请输入原数:'))
jinzhi_10 = int(input('请输入原数进制:'))
jinzhi_2 = int(input('请输入转化后进制:'))
total = 0
total_10 = 0
for i in range(len(str(a))):
    m = a // (10 ** i) % 10  #原进制数的每个位置
    total_10 = total_10 + m * (8 ** i)  #每个位置变成十进制的一部分
def zhuanhuan(n,i):
    global total
    div = n % jinzhi_2
    total = total + div * (10 ** i)
    i = i + 1
    new_num = n // jinzhi_2
    if new_num != 0:
        zhuanhuan(new_num,i)
zhuanhuan(total_10,0)
print('转化后为:' + str(total))
        
        

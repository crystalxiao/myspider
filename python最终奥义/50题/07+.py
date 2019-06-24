import re
a = int(input('请输入一个质数:'))
list = []
b = int(a * 0.5 + 1)
def fenjie(n,list):
    for i in range(2,b):
        if (n % i == 0) & (n != 1):
            n = int(n / i)
            list.append(i)
            fenjie(n,list)
            break
fenjie(a,list)
lists = str(list)
li = re.sub(r',', ' *', lists)
li = re.sub(r'[\[\]]', '', li)
print(str(a) + ' = ' + li)

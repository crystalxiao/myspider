year = input('请输入年份:')
month = input('请输入月份:')
day = input('请输入日期:')
y = int(year)
m = int(month)
d = int(day)
total = 0
list1 = [0,31,29,31,30,31,30,31,31,30,31,30,31]
list2 = [0,31,28,31,30,31,30,31,31,30,31,30,31]
if y % 4 == 0:
    for i in range(m):
        total = total + list1[i] + d
else:
    for i in range(m):
        total = total + list2[i] + d
print('今天是这一年的第' + str(total) + '天')

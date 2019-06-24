score = int(input('请输入分数:'))
if score >= 90:
    level = '优秀'
elif score >= 60:
    level = '及格'
else:
    level = '辣鸡'
print(level)

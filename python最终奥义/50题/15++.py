a = input('请输入字符:')
english = 0
number = 0
space = 0
other = 0
for i in a:
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        english = english + 1
    elif i in '0123456789':
        number = number + 1
    elif i == ' ':
        space = space + 1
    else:
        other = other + 1
print('字母数量为' + str(english))
print('数字数量为' + str(number))
print('空格数量为' + str(space))
print('其它数量为' + str(other))

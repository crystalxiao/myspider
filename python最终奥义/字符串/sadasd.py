def trim(s):
    if s == '':
        return ''
    elif s[0] == ' ':
        s = s[1:len(s)]
        trim(s)
        return trim(s)
    elif s[-1] == ' ':
        s = s[:len(s)-1]
        trim(s)
        return trim(s)
    else:
        return s

print(trim('hello  '))
# 测试:
print (trim('hello  '))
if trim('  hello') != 'hello':
    print('2测试失败!')
elif trim('  hello  ') != 'hello':
    print('3测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('4测试失败!')
elif trim('') != '':
    print('5测试失败!')
elif trim('    ') != '':
    print('6测试失败!')
else:
    print('测试成功!')

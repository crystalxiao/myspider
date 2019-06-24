abc = input('第一个字母')
if abc == 'm' or abc =='M':
    print('周一')
elif abc == 'w' or abc =='W':
    print('周二')
elif abc == 'f' or abc =='F':
    print('周五')
elif abc == 't' or abc =='T':
    qwer = input('第二个字母')
    if qwer == 'u' or qwer == 'U':
        print('周二')
    else:
        print('周四')
elif abc == 's' or abc =='S':
    qwer = input('第二个字母')
    if qwer == 'a' or qwer == 'A':
        print('周六')
    else:
        print('周日')
else:
    print('输入有误')
    

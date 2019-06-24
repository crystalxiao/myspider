from random import choice

def mima(choose):
    pass_1 = [i for i in range(10)]
    pass_2 = [5,7,9,4,0,6,3,1,2,8]
    pass_prime = ['03','05','07','09','11','13','17','19','23','29','31','37','41','43','47','53','59','61','67','71','73','79','83','89','97']

    #字符串转换ord(第一层加密)
    def code_password(words):
        string = ''
        for i in words:
            if i.isalpha():
                pw = ord(i) - 23
            else:
                pw = ord(i)
            string += str(pw)
        return string

    #新的数字密码转化pass_2对应数字(第二层加密)
    def num_password(number):
        for n in range(10):
            if num_1[n] == number:
                number = num_2[n]
                return number

    #ord转换新的数字密码(第三层加密)
    def prime_password(numbers):
        prime = choice(pass_prime)
        prime_num = int(prime)
        shang = numbers // prime_num
        yushu = numbers % prime_num
        str_yushu = str(yushu)
        if len(str_yushu) == 1:
            str_yushu = '0' + str_yushu
        string = prime + str_yushu +str(shang)
        return string

    #对应三个解码
    def depass_code(words):
        string = ''
        for i in range(0,len(words)-1,2):
            st_code = words[i] + words[i + 1]
            if st_code !='32': 
                string += chr(int(st_code) + 23)
            else:
                string += chr(int(st_code))
        return string
        
    def depass_prime(string):
        total = int(string)
        prime_str = string[0] + string[1]
        prime = int(prime_str)
        yushu = int(string[2] + string[3])
        shang = total % (10 ** (len(string) - 4))
        number = shang * prime + yushu
        str_number = str(number)
        if len(str_number) != 6:
            str_number = '0' + str_number
        return str_number

    def depass_num(number):
        for n in range(10):
            if num_2[n] == number:
                number = num_1[n]
                return number

    #加密
    if choose == '1':
        yuju = input('请输入要加密的语句,回车键确认:')
        string = ''
        string_six = ''
        #第一层加密
        code_str = code_password(yuju)
        #第二层加密
        for i in code_str:
            i_num = int(i)
            i_password = num_password(i_num)
            string += str(i_password)
        #第三层加密
        leng = len(string)
        for l in range(0,leng // 6):
            new_string = string[l*6] + string[l*6+1] + string[l*6+2] + string[l*6+3] + string[l*6+4] + string[l*6+5]
            prime_string = prime_password(int(new_string))
            string_six += prime_string + ' '
        for m in range(0,leng % 6):
            yu_string = string[leng - leng % 6 + m]
            string_six += yu_string
        print('加密后的内容为:' + str(string_six))
        choose = input('加密请输入1,解密请输入2,回车键确认:')
        mima(choose)

    #解密
    elif choose == '2':
        yuju = input('请输入要解密的语句,回车键确认:').split(' ')
        string = ''
        string_real = ''
        #第三层解码
        for i in range(len(yuju) - 1):
            string += depass_prime(yuju[i])
        if len(yuju[len(yuju) - 1]) < 6:
            string += str(yuju[len(yuju) - 1])
        else:
            string += depass_prime(yuju[len(yuju) - 1])
        #第二层解码
        for l in string:
            l_num = int(l)
            l_real = depass_num(l_num)
            string_real += str(l_real)
        #第一层解码
        real_talk = depass_code(string_real)
        print('解密后的内容为:' + real_talk)
        choose = input('加密请输入1,解密请输入2,回车键确认:')
        mima(choose)

    #输入其它重新输入
    else:
        choose = input('请先用"1"或"2"选择加密或者解密:')
        mima(choose)

choose = input('加密请输入1,解密请输入2,回车键确认:')
mima(choose)

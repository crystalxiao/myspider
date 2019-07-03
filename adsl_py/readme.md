adsl使用方法：
    将此包放于python的包目录中
    from adsl-py.adsl import ADSL_Tool  
    实例化ADSL_Tool后调用相应方法进行操作

可调用方法:
    connect()       开始拨号
    disconnect()    中止拨号
    reconnect()     重新拨号(只有在拨号状态才能断开重播)
    cmd()           执行终端方法

实例属性：
    ip              当前网络ip
    name            adsl名称
    status          是否处于拨号状态
    sys             目前主机操作系统

ep:
    from adsl-py.adsl import ADSL_Tool 
    net = ADSL_Tool(url='xxx', token='xxx')
    net.connect() #adsl拨号
    print(net.ip) #打印当前网络ip
    print(net.status) #True
    net.disconnect() #取消拨号
    print(net.status) #False

注意事项：
    获取网络ip的方法为爬取ip138提供的本机网络ip，因此使用此模块
    前需要先到 http://www.ip138.com/ 得到返回网络ip的临时网页url
    并在初始化时添加，或在settings中设置保存，也支持ip138提供的
    接口服务，更改token即可
    

server使用方法:

    from adsl_py import server

    #需在settings中设置IP138token或url
    ser = server.ADSL_Server()
    ser.start()

server另一种用法,继承ADSL_Server后重写getIP方法，注意返回值必须为本机网络ip的字符串:

    from adsl_py import server

    class MyServer(server.ADSL_Server):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def getIP():
            xxxxxx
            return 本机ip

    ser = MyServer()
    ser.start()


client的使用方法:

    方法有三个：
        connect()   建立连接
        getIP()     获取主机当前网络ip
        close()     关闭连接

    from adsl_py import client

    #host为服务机的本地ip地址，若配置了settings的server_host则不用填写
    cli = client.ADSL_Client(host='xxxxxx')
    cli.connect()
    print(cli.getIP())
    cli.close()


本项目长期维护与github: https://github.com/zongrongjin/myspider/tree/master/adsl-py
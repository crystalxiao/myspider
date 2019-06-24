#######################################################################################
#########此游戏由KayaK-Z开发，致敬开发者的同桌————本游戏的主人公Tony(他不是理发匠)##########
#######################################################################################

#First module : begin the game (it's just a joke)
import time
print('程序开始,游戏加载中...')
time.sleep(2)
print('加载人物模型...')
time.sleep(3)
print('加载人物技能...')
time.sleep(0.5)
print('加载完毕，正在读取您的角色信息...')
time.sleep(5)
print('读取完毕，正在连接服务器...')
time.sleep(3)
startname = input('连接成功，检测到该电脑未创建角色，请输入你的角色昵称:')
print('我觉得"Tony"这个名字更适合你，你就叫"Tony"吧\n游戏将在3秒后开始...')
time.sleep(3)

#######################################################################################

food_li = []
tools_li = []
buff_li = []
boss_li = []
tool_dic = {}
tool_name = {}
buff_name = {}
boss_name = {}

#Second module : the class of player
class xiaoming():
    def __init__(self,x = 1,y = 1):
        self.weight = 62
        self.hair_count = 100000
        self.age = 18
        self.position = [x,y]
        self.name = 'Tony'
        self.backpack = tool_dic
        self.start_name = startname
        self.new_name = None
        self.attack = 0
        self.protect = 0
        self.speed = 1
        self.lucky = -100

    #Can I get the tools ?
    def get_tools(self,tool_li):
        for i in tool_li:
            if i.position == self.position:
                if i.name in self.backpack:
                    self.backpack[i.name] += 1
                else:
                    self.backpack[i.name] = 1
                i.position = [999,999]
                print('%s获得了传说中的神器:%s，目前拥有数量为%d'%(self.name,i.name,self.backpack[i.name]))
                break

    #Where is my hair ?     
    def hair_change(self,weight_change):
        hair_change_speed = 10
        self.hair_count += weight_change * hair_change_speed

    #I'm eating foods
    def eat_food(self,food):
        self.weight += abs(food.energy)
        self.hair_change(food.energy)
    
    #I'm moving by bike
    def move(self,x,y):
        start = self.position
        self.position = [x,y]
        distance = abs(x - start[0]) + abs(y - start[1])
        cost_year = 0.2 * distance / self.speed
        self.age += cost_year
        print('经过%.1f年的长途跋涉，%s终于到达了目标地点。\n目前年龄：%.1f岁'%(cost_year,self.name,self.age))
        self.iseat(food_li)
        self.get_tools(tools_li)

    #I'm moving by biubiubiu ~
    def magic_move(self,x,y):
        start = self.position
        self.position = [x,y]
        distance = abs(x - start[0]) + abs(y - start[1])
        cost_year = 0.1 * distance / self.speed
        self.weight -= 0.1 * distance / self.speed
        self.age += cost_year
        print('经过%.1f年的时空旅行，%s终于到达了目标地点。\n目前年龄：%.1f岁'%(cost_year,self.name,self.age))
        self.iseat(food_li)
        self.get_tools(tools_li)

    #Can I eat sth. ?
    def iseat(self,args):
        for i in args:
            if self.position == i.position:
                i.position = [999,999]
                self.eat_food(i)
                print('%s吃下了%s，觉得元气满满，真香！\n目前体重:%.1fKG，头发还有%d根'%(self.name,i.name,self.weight,self.hair_count))
                break

    #Which method I should choose ?
    def move_method(self):
        flag = True
        while flag:
            x1 = int(input('请输入要到的坐标x值:'))
            y1 = int(input('请输入要到的坐标y值:'))
            move_by = int(input('1.骑自行车前往\n2.穿越时空隧道前往\n请输入方法:'))
            if move_by == 1:
                self.move(x1,y1)
                flag = False
            elif move_by == 2:
                self.magic_move(x1,y1)
                flag = False
            else:
                print('输入有误，请重新输入')

    #It's my status
    def status(self):
        if tool_dic == {}:
            num = 0
        else:
            num = sum(tool_dic.values())
        print('''
        姓名: %s            年龄: %.1f岁
        体重: %.1fKG          发量: %d根
        速度: %d               攻击: %d
        防御: %d               当前位置: %s
        幸运: %d            物品数: %d      
                '''%(self.name,self.age,self.weight,self.hair_count,self.speed,self.attack,self.protect,[self.position[0],self.position[1]],self.lucky,num))

    #Show my backpack and a samll suprise
    def mybackpack(self):
        if tool_dic == {}:
            print('你的背包神马都没有，你个穷逼')
            self.name = '穷逼'
        else:
            print('%s的背包如下:'%(self.name))
            bp = tool_dic.items()
            for tool,number in bp:
                print(tool,':',number)
            if self.name == '穷逼':
                print('恭喜你不是穷逼了!')
                self.name_reset()
    
    #I want reset my name
    def name_reset(self):
        self.new_name = input('请输入你的新姓名:')
        if self.new_name != self.start_name:
            print('其实我还是觉得"%s"这个名字更好听~'%(self.start_name))
            self.name = self.start_name
        else:
            print('你对这个名字还真是钟情啊~')
        self.start_name = self.new_name
        print('改名成功')

    #I want use my tools
    def use_tools(self,usewhat):
        if usewhat not in tool_dic:
            print('使用失败,您没有%s'%(usewhat))
        else:
            if usewhat == '改名卡':
                self.name_reset()
            else:
                self.speed += tool_name[usewhat].speeds
                self.attack += tool_name[usewhat].attacks
                self.protect += tool_name[usewhat].protects
            tool_dic[usewhat] -= 1
            print('使用%s成功，目前还余%d个'%(usewhat,tool_dic[usewhat]))
            if tool_dic[usewhat] == 0:
                tool_dic.pop(usewhat)
            

#####################################################################################

#Third module : the class of food
class food():

    def add(self):
        food_li.append(self)

    def __init__(self,cn_name,energys,*args):
        self.name = cn_name
        self.energy = energys
        self.position = [args[0],args[1]]
        self.add()


#####################################################################################

#Fouth module : the classes of tools
class tools():

    def add(self):
        tools_li.append(self)
        tool_name[self.name] = self

    def __init__(self,cn_name,*args,speed = 0,attack = 0,protect = 0):
        self.name = cn_name
        self.speeds = speed
        self.attacks = attack
        self.protects = protect
        self.position = [args[0],args[1]]
        self.add()


#####################################################################################

#Fifth module : the class of buffs
class buffs():

    def add(self):
        buff_li.append(self)
        buff_name[self.name] = self

    def __init__(self,cn_name,*args,speed = 0,attack = 0,protect = 0,luck = 0):
        self.name = cn_name
        self.speeds = speed
        self.attacks = attack
        self.protects = protect
        self.position = [args[0],args[1]]
        self.lucky = luck
        self.add()


#####################################################################################

#Sixth module : the class of boss
class boss():

    def add(self):
        boss_li.append(self)
        boss_name[self.name] = self

    def __init__(self,cn_name,*args,HP = 1000,attack = 10,protect = 20,luck = 30):
        self.name = cn_name
        self.hp = HP
        self.attacks = attack
        self.protects = protect
        self.position = [args[0],args[1]]
        self.lucky = luck
        self.add()

#####################################################################################

def maps_look(a):
    maps_all = [a.position]
    boss_all = []
    for f in food_li:
        maps_all.append(f.position)
    for t in tools_li:
        maps_all.append(t.position)
    for b in buff_li:
        maps_all.append(b.position)
    for m in boss_li:
        boss_all.append(m.position)
    print('  ', end = '|')
    for colnum in range(1, 40):
        if colnum < 10:
            print('', colnum, end = '|')
        else:
            print(colnum, end = '|')
    print('')
    for row in range(1, 40):
        if row < 10:
            print('', row, end = '|')
        else:
            print(row, end = '|')
        for col in range(1, 40):
            if [row, col] == a.position:
                print('我', end='|')
            elif [row, col] in maps_all:
                print('物', end = '|')
            elif [row, col] in boss_all:
                print('怪', end = '|')
            else:
                print('  ', end = '|')
        print('')


#Class all of the variables
shit = food('一碗热翔', -1.5, 5, 5)
hair = food('一缕秀发', 2, 10, 8)
clean = food('一个卫生巾', -3, 11, 26)
someth = food('神秘异物', 5, 20, 9)

sword = tools('消食片', 25, 25, attack=10)
shield = tools('万能胶', 3, 14, protect=10)
shoes = tools('跑得快', 19, 13, speed=10)
whosyourdaddy = tools('万年金巴豆', 4, 8, attack=999)
who_can_kill_me = tools('性感小护士', 1, 26, protect=999)
magic_move_card = tools('疯狂的赛车', 31, 5, speed=999)
reset_name_card = tools('改名卡', 39, 1)

a_buff = buffs('攻击BUFF', 8, 18, attack=25)

fuck_sky = boss('日天兽', 12, 13, luck=100)
eat_bottom = boss('吃土兽', 36, 33, HP=1888)
man_monster = boss('人妖兽', 19, 36, HP=888)
gold_pig = boss('金猪', 16, 34, HP=1, luck=0)
king = boss('屎神', 39, 39, HP=9999, attack=500, protect=999, luck=66)

# food_li.extend([shit,hair,clean,someth])
# tools_li.extend([sword,shield,shoes,whosyourdaddy,who_can_kill_me,magic_move_card])
p1 = xiaoming()


######################################################################################

#Main code
def main():
    p1.status()
    input_status = True
    while input_status:
        do_sth = input('1.开始移动，2.查询当前状态，3.查看当前背包,4.查看地图，输入道具名直接使用:')
        if do_sth == '1':
            p1.move_method()
        elif do_sth == '2':
            p1.status()
        elif do_sth == '3':
            p1.mybackpack()
        elif do_sth == '4':
            maps_look(p1)
        else:
            p1.use_tools(do_sth)


######################################################################################

main()
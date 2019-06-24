import math
import matplotlib.pyplot as plt
import numpy
import turtle as tt
def run(lengths,angles):
    length=int(lengths)*2.5
    angle=90-int(angles)
    #计算水平和竖直方向运动距离
    tx=3.5#弹性常量
    g=9.8#重力加速度
    v0=length*tx
    v2=v0*math.sin(2*math.pi/360*angle)
    v1=v0*math.cos(2*math.pi/360*angle)
    t=2*v1/g
    s2=v2*t
    s1=v1*t/2
    #构造过抛物线的三点
    x1=0
    y1=0
    x2=s2
    y2=0
    x3=s2/2
    y3=s1
    #求抛物线的方程
    a=((x3-x1)*(y1-y2)-(x1-x2)*(y3-y1))/((x1-x2)*(x2-x3)*(x3-x1))
    b=(y1-y2-a*(x1*x1-x2*x2))/(x1-x2)
    c=y1-a*x1*x1-b*x1
    #print(math.sin(2*math.pi/360*jiaodu))
    tt.screensize(1000,600,"green")
    tt.pensize(5)
    tt.speed(10)
    tt.pencolor("red")
    tt.penup()
    tt.goto(-450,-200)
    tt.pendown()
    for x in range(0,int(s2)):
        y=a*x*x+b*x+c
        tt.goto(x-450,y-200)
    lengths=input("请输入拉弹弓的力度(1-10)：")
    angles=input("请输入拉弹弓的角度(0-90)：")
    run(lengths,angles)
lengths=input("请输入拉弹弓的力度(1-10)：")
angles=input("请输入拉弹弓的角度(0-90)：")
run(lengths,angles)


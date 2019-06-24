import math
import matplotlib.pyplot as plt
import numpy
import turtle as tt
from sympy import *
def run(lengths,angles):
    length=int(lengths)*2.5#（自定义）
    angle=90-int(angles)
    #计算水平和竖直方向运动距离
    tx=3.5#弹性常量（自定义）
    g=9.8#重力加速度
    v0=length*tx
    v2=v0*math.sin(2*math.pi/360*angle)
    v1=v0*math.cos(2*math.pi/360*angle)
    t=2*v1/g
    s2=v2*t
    s1=g*t/2*t/2/2
    #构造过抛物线的三点
    x1=0
    y1=0
    x2=s2
    y2=0
    x3=s2/2
    y3=s1
    #求抛物线的方程
    a=Symbol('a')
    b=Symbol('b')
    c=Symbol('c')
    answer=solve([a*x1*x1+b*x1+c-y1,a*x2*x2+b*x2+c-y2,a*x3*x3+b*x3+c-y3],[a,b,c])
    a=answer[a]
    b=answer[b]
    c=answer[c]
    #画出抛物线
    tt.screensize(1000,600,"lightblue")
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


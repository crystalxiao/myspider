#t:top,be:behind,r:right,l:left,f:front,bo:bottom
#旋转均为90度
t = [
    ['红','红','红'],
    ['红','红','红'],
    ['红','红','红']
    ]
be = [
    ['黄','黄','黄'],
    ['黄','黄','黄'],
    ['黄','黄','黄']
    ]
r = [
    ['绿','绿','绿'],
    ['绿','绿','绿'],
    ['绿','绿','绿']
    ]
l = [
    ['蓝','蓝','蓝'],
    ['蓝','蓝','蓝'],
    ['蓝','蓝','蓝']
    ]
f =[
    ['白','白','白'],
    ['白','白','白'],
    ['白','白','白']
    ]
bo = [
    ['橙','橙','橙'],
    ['橙','橙','橙'],
    ['橙','橙','橙']
    ]

#将一个数组倒序后输出，但不改变原数组
def re(li):
    l = []
    for i in range(len(li)):
        l.append(li[len(li) - 1 - i])
    return l

#特殊情况
def res(li):
    l = [[li[0][2],li[0][1],li[0][0]],[li[1][2],li[1][1],li[1][0]],[li[2][2],li[2][1],li[2][0]]]
    return l

#将A面顺时针旋转后A面的颜色分布
def cw(a):
    a[0],a[1],a[2] = [a[2][0],a[1][0],a[0][0]],[a[2][1],a[1][1],a[0][1]],[a[2][2],a[1][2],a[0][2]]

#将A面逆时针旋转后A面的颜色分布
def acw(a):
    a[0],a[1],a[2] = [a[0][2],a[1][2],a[2][2]],[a[0][1],a[1][1],a[2][1]],[a[0][0],a[1][0],a[2][0]]

#顺时针旋转第N层后，改变他们的数组值    
def cw_row_around(f,l,b,r,n):
    f[n],l[n],b[n],r[n] = r[n],f[n],re(l[n]),re(b[n])

#逆时针旋转第N层后，改变他们的数组值 
def acw_row_around(f,l,b,r,n):
    f[n],l[n],b[n],r[n] = l[n],re(b[n]),re(r[n]),f[n]

#顺时针旋转第N列后，改变他们的数组值 
def cw_col_around(f,bo,be,t,n):
    for i in range(3):
        f[i][n],bo[i][n],be[2-i][n],t[i][n] = t[i][n],f[i][n],bo[i][n],be[2-i][n]

#逆时针旋转第N列后，改变他们的数组值 
def acw_col_around(f,bo,be,t,n):
    for i in range(3):
        f[i][n],bo[i][n],be[2-i][n],t[i][n] = bo[i][n],be[2-i][n],t[i][n],f[i][n]

#顺时针水平旋转整个魔方
def cw_all(f,l,be,r,t,bo):
    f,l,be,r = r,f,res(l),res(be)
    cw(t)
    cw(bo)
    return f,l,be,r,t,bo

#逆时针水平旋转整个魔方
def acw_all(f,l,be,r,t,bo):
    f,l,be,r = l,res(be),res(r),f
    acw(t)
    acw(bo)
    return f,l,be,r,t,bo

#顺时针竖直旋转整个魔方
def cw_col_all(f,l,be,r,t,bo):
    f,t,be,bo = bo,f,re(t),re(be)
    cw(l)
    cw(r)
    return f,l,be,r,t,bo

#逆时针竖直旋转整个魔方
def acw_col_all(f,l,be,r,t,bo):
    f,t,be,bo = t,re(be),re(bo),f
    acw(l)
    acw(r)
    return f,l,be,r,t,bo
    
#调用方法:
while True:
    print('它的上面是:\n',t[0],'\n',t[1],'\n',t[2])
    print('它的前面是:\n',f[0],'\n',f[1],'\n',f[2])
    print('它的右面是:\n',r[0],'\n',r[1],'\n',r[2])    

    #r代表row，c代表col，123代表第123层/列，01代表顺时针逆时针
    #最后四个代表旋转整个魔方
    a = input('请输入操作方法:')
    if a == 'r1.0':
        cw_row_around(f,l,be,r,0)
        cw(t)
    elif a == 'r1.1':
        acw_row_around(f,l,be,r,0)
        acw(t)
    elif a == 'r2.0':
        cw_row_around(f,l,be,r,1)
    elif a == 'r2.1':
        acw_row_around(f,l,be,r,1)
    elif a == 'r3.0':
        cw_row_around(f,l,be,r,2)       
    elif a == 'r3.1':
        acw_row_around(f,l,be,r,2)
    elif a == 'c1.0':
        cw_col_around(f,bo,be,t,0)
        cw(l)
    elif a == 'c1.1':
        acw_col_around(f,bo,be,t,0)
        acw(l)
    elif a == 'c2.0':
        cw_col_around(f,bo,be,t,1)
    elif a == 'c2.1':
        acw_col_around(f,bo,be,t,1)
    elif a == 'c3.0':
        cw_col_around(f,bo,be,t,2)
        cw(r)
    elif a == 'c3.1':
        acw_col_around(f,bo,be,t,2)
        acw(r)
    elif a == 'r00':
        f,l,be,r,t,bo = cw_all(f,l,be,r,t,bo)
    elif a == 'r01':
        f,l,be,r,t,bo = acw_all(f,l,be,r,t,bo)
    elif a == 'c00':
        f,l,be,r,t,bo = cw_col_all(f,l,be,r,t,bo)
    elif a == 'c01':
        f,l,be,r,t,bo = acw_col_all(f,l,be,r,t,bo)

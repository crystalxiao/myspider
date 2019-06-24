from tkinter import *

ssr = ['ssr' + str(i + 1) for i in range(22)]
other_ssr = ['联动ssr' + str(i + 1) for i in range(6)]
other_sr = ['联动sr1']
other_r = ['联动r1']
sp = ['sp' + str(i + 1) for i in range(4)]
sr = ['sr' + str(i + 1) for i in range(48)]
r = ['r' + str(i + 1) for i in range(35)]
n = ['n' + str(i + 1) for i in range(12)]
gua = ['呱太' + str(i + 1) for i in range(14)]

draw = Tk()
draw.geometry('900x900')
white_card = Button(draw,bd = '10px,4px',bg = 'lightgray',text = '破碎符咒')
blue_card = Button(draw,bd = '10px,4px',bg = 'lightblue',text = '神秘符咒')
black_card = Button(draw,bd = '10px,4px',bg = 'pink',text = '勾玉召唤')

cv = Canvas(draw,bg = 'black')

filename = PhotoImage(file = "ssr.gif")
image = cv.create_image(450,10,anchor=NE, image=filename)

cv.pack()
white_card.pack()
blue_card.pack()
black_card.pack()
draw.mainloop()

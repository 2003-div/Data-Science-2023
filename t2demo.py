from turtle import *

pensize(3)
speed('fastest')
bgcolor('red')
pencolor('white')

for i in range (5):
    rt (144)
    fd(100)
    for i in range (5):
        rt (144)
        fd(50)
        for i in range (5):
            rt (144)
            fd(25)
    
hideturtle()
mainloop()


from turtle import *
pensize(3)
speed('fastest')
bgcolor('black')
pencolor('red')

for i in range(4):
    lt(360/4)
    fd(100)
    for i in range(4):
        lt(360/4)
        fd(50)
        for i in range(4):
            lt(360/4)
            fd(25)
hideturtle()
mainloop()

    
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
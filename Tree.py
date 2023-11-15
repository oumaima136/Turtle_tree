import turtle 
import random

angle = 20
turtle.bgcolor("#696969")
t = turtle.Turtle(visible=False)
t.speed('fastest') 
t.setheading(90)
t.penup()

t.setpos(0,-150)


def drawlevel(size,level):
        t.pensize(level*0.4)
        t.pencolor((t.heading())*0.1/100,(t.heading())*0.1/100,(t.heading())*0.1/100)
        t.pendown()
        t.forward(size)

        
        if level>0:
            ang1 = random.random() * 15 + 10
            ang2 = random.random() * 15 + 10
            lenght = size * (random.random()*0.2 + 0.7)
            t.left(ang1)
            drawlevel(lenght,level-1)
            t.right(ang1 + ang2)
            drawlevel(lenght,level-1)
            t.left(ang2)
        else:
              t.left(90)
              t.pencolor((t.heading()+400)*0.1/100,(t.heading()+400)*0.1/100,(t.heading()+400)*0.1/100)
              t.circle(2)
              t.pencolor((t.heading())*0.1/100,(t.heading())*0.1/100,(t.heading())*0.1/100)
              t.right(90)
        t.penup()
        t.backward(size)
            

level = 10
length = 100
#draw tree with 10 levels of size 100 
drawlevel(length,level)

turtle.done()
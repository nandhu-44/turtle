from turtle import *
from randomcolor import *

window = Screen()
window.bgcolor("yellow")

t = Turtle()
t.pensize(2)
t.penup()
t.back(90)
t.forward(50)
t.pendown()

t.color(randomColor())
t.left(90)
t.forward(20)
t.right(150)
t.forward(22)
t.right(-150)
t.forward(20)

t.penup()
t.right(90)
t.forward(20)
t.pendown()


t.right(90)
t.forward(20)
t.back(20)
t.left(90)
t.forward(14)
t.right(90)
t.forward(20)
t.back(10)
t.right(90)
t.forward(14)

t.penup()
t.back(34)
t.left(90)
t.pendown()
t.right(180)


t.back(10)
t.forward(20)
t.right(150)
t.forward(22)
t.right(-150)
t.forward(20)


t.penup()
t.right(90)
t.forward(20)
t.pendown()
t.right(90)

t.forward(20)
t.left(90)
for i in range(180):
    t.forward(30/180)
    t.left(1)
t.penup()
t.right(180)
t.forward(24)
t.pendown()
t.right(90)
t.forward(20)
t.back(10)
t.left(90)
t.forward(14)
t.left(90)
t.back(10)
t.forward(20)
t.right(90)
t.penup()
t.forward(20)
t.pendown()
t.right(90)
t.forward(15)

for i in range(180):
    t.forward(15/180)
    t.left(1)
t.forward(15)

t.penup()
t.left(90)
t.forward(70)
t.right(90)
t.forward(70)
t.right(90)
t.left(90)
t.forward(20)
t.right(90)
t.pendown()
for i in range(360):
    currColor = 'red'
    t.color(currColor)
    t.right(1)
    t.forward(2)





window.exitonclick()


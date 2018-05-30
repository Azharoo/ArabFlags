﻿import turtle
window = turtle.Screen()
window.bgcolor("white")
window.title("United Arab Emirates الإمارات العربية المتحدة")
flag = turtle.Turtle()
flag.speed(10)
flag.color("green")

def Rectangle(stylo, h, l,color):
	flag.down()
	stylo.fillcolor(color)
	stylo.begin_fill()
	stylo.color(color)
	stylo.forward(l)
	stylo.left(90)
	stylo.forward(h)
	stylo.left(90)
	stylo.forward(l)
	stylo.left(90)
	stylo.forward(h)
	stylo.end_fill()
	flag.up()

Rectangle(flag, 50, 200, "black")
flag.goto(0,100)
flag.left(90)
Rectangle(flag, 50, 200, (0.008, 0.588, 0.008))
flag.goto(0,0)
flag.left(90)
Rectangle(flag, 150,60, (0.925, 0.008, 0.004))
flag.ht() # اخفاء مؤشر الماوس
window.exitonclick()
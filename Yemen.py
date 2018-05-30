import turtle
window = turtle.Screen()
window.bgcolor("white")
flag = turtle.Turtle()
window.title("Yemen اليمن")
#flag.shape("turtle")
flag.color("green")



def mostatil(stylo, h, l,color):
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
	flag.ht()
	flag.up()




mostatil(flag, 50, 200, "black")

flag.goto(0,100)
flag.left(90)
mostatil(flag, 50, 200, (0.925, 0.008, 0.004))




window.exitonclick()

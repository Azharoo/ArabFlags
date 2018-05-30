import turtle
window = turtle.Screen()
window.bgcolor("white")
window.title("Jordan")
flag = turtle.Turtle()
#flag.shape("turtle")
flag.color("green")


def etoile(stylo,color, tail):
	i=0
	stylo.fillcolor(color)
	stylo.begin_fill()
	while i < 7:	
		stylo.forward(tail)
		stylo.right(180*6/7)
		i+=1
	stylo.end_fill()

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
	flag.up()
def motalat(stylo, cote,color):
	stylo.down()
	stylo.fillcolor(color)
	stylo.begin_fill()
	stylo.color(color)
	stylo.forward(cote)
	stylo.left(120)
	stylo.forward(cote)
	stylo.left(120)
	stylo.forward(cote)
	stylo.end_fill()
	stylo.up()




mostatil(flag, 33, 200, (0.008, 0.588, 0.008))

flag.backward(66)
flag.left(90)

mostatil(flag, 33, 200, "black")
flag.goto(0,0)
flag.left(120)
motalat(flag,99,(0.925, 0.008, 0.004))
flag.goto(30,60)
etoile(flag,"white",25)
flag.ht()
window.exitonclick()

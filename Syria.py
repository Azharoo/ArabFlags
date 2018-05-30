import turtle
window = turtle.Screen()
window.bgcolor("white")
window.title("Syria سوريا")
flag = turtle.Turtle()
#flag.shape("turtle")
def etoile(stylo,color, tail):
	i=0
	stylo.fillcolor(color)
	stylo.begin_fill()
	while i < 5:	
		stylo.forward(tail)
		stylo.right(180*4/5)
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


hauteur=100
largeur = 200

mostatil(flag, hauteur/3, largeur, "black")
flag.goto(0,hauteur*2/3)
flag.left(90)
mostatil(flag, hauteur/3, largeur, (0.925, 0.008, 0.004))
flag.left(90)
flag.goto(50,52)
etoile(flag,(0.008, 0.588, 0.008),25)
flag.goto(115,52)
etoile(flag,(0.008, 0.588, 0.008),25)
flag.ht()

window.exitonclick()

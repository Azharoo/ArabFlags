import turtle
window = turtle.Screen()
window.bgcolor("white")
window.title("Tunisia تونس")
flag = turtle.Turtle()
#flag.shape("turtle")
flag.color("green")
flag.speed(10)



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
def da2ira(stylo, rayon,color):
	stylo.down()
	stylo.color(color)
	stylo.fillcolor(color)
	stylo.begin_fill()
	stylo.circle(rayon,360)
	stylo.end_fill()
	stylo.up()

def etoile(stylo,color, tail):
	i=0
	stylo.fillcolor(color)
	stylo.begin_fill()
	while i < 5:	
		stylo.forward(tail)
		stylo.right(180*4/5)
		i+=1
	stylo.end_fill()


largeur=400
hauteur=200
rayon1=hauteur/4
flag.goto(-(largeur/2),-(hauteur/2))
mostatil(flag, hauteur, largeur, (0.925, 0.008, 0.004))
flag.goto(-rayon1,0)
flag.fillcolor("white")
da2ira(flag, rayon1,"white")
flag.goto(-rayon1+9,0)
da2ira(flag, rayon1-10, "red")
flag.goto(-rayon1+22,0)
da2ira(flag, rayon1-13, "white")
flag.left(90)
flag.forward(17)
flag.left(10)
etoile(flag,"red",35)

flag.ht()

window.exitonclick()  

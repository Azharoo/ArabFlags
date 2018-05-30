import turtle



def draw_drapo(taille,  couleur):
	
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color(couleur)
	brad.speed(2)
	brad.fillcolor(couleur)
	brad.begin_fill()
	brad.goto(-taille/2,0)

	i=0
	while i < 5:	
		brad.forward(taille)
		brad.right(180*4/5)
		
		i+=1
	brad.end_fill()	
	brad.ht()

window = turtle.Screen()
window.title("Somalia الصومال")
window.bgcolor((0.004, 0.537, 1))
draw_drapo(150, (1,1,1))

window.exitonclick()


	


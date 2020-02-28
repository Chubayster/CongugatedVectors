import turtle
from turtle import Turtle, Screen

screen = Screen()

turtle.tracer(0,0) # now trurtle renders only on updates

#grid
g = Turtle("arrow")
g.color(0.88,0.88,0.9)
g.pensize(2)
g.speed(-1)
g.penup()

for n in range(-4,4):
	g.penup()
	g.goto(200*n-100,-1000)
	g.pendown()
	g.goto(200*n-100,1000)

for n in range(-4,4):
	g.penup()
	g.goto(-1000,200*n-100)
	g.pendown()
	g.goto(1000,200*n-100)

#Conjectured bases
subx = Turtle()
subx.color('blue')
subx.speed(-1)
subx.shape("arrow")
subx.pensize(4)
subx.penup()
subx.goto(-100,-100)
subx.pendown()
subx.setheading(subx.towards(0,-100))
subx.goto(100,-100)

suby = Turtle()
suby.color('blue')
suby.speed(-1)
suby.shape("arrow")
suby.pensize(4)
suby.penup()
suby.goto(-100,-100)
suby.pendown()
suby.setheading(suby.towards(-100,100))
suby.goto(-100,100)


#Bases
x = Turtle()
x.speed(-1)
x.shape("arrow")
x.pensize(4)
x.penup()
x.goto(-100,-100)
x.pendown()
x.setheading(x.towards(0,-100))
x.goto(100,-100)

y = Turtle()
y.speed(-1)
y.shape("arrow")
y.pensize(4)
y.penup()
y.goto(-100,-100)
y.pendown()
y.setheading(y.towards(-100,100))
y.goto(-100,100)


def conjegatedCords():

    E1_x = 0.005 * (x.xcor() + 100)
    E1_y = 0.005 * (x.ycor() + 100)

    E2_x = 0.005 * (y.xcor() + 100)
    E2_y = 0.005 * (y.ycor() + 100)

    det = (E1_x**2 + E1_y**2)*(E2_x**2+E2_y**2)+(E1_x*E2_x+E1_y*E2_y)**2
    
    invMatrx = [[1,0],[0,1]]
    invMatrx[0][0] = (E2_x**2 + E2_y**2)/ det
    invMatrx[0][1] = (E1_x*E2_x + E1_y*E2_y)/ det
    invMatrx[1][0] = (E1_x*E2_x + E1_y*E2_y)/ det
    invMatrx[1][1] = (E1_x**2 + E1_y**2)/ det

    x1 = (invMatrx[0][0]*E1_x + invMatrx[0][1]*E1_y)*200 -100
    y1 = (invMatrx[1][0]*E1_x + invMatrx[1][1]*E1_y)*200 -100
    x2 = (invMatrx[0][0]*E2_x + invMatrx[0][1]*E2_y)*200 -100
    y2 = (invMatrx[1][0]*E2_x + invMatrx[1][1]*E2_y)*200 -100
    redrawConjegatedBases(x1,y1,x2,y2)


def draggingx(x_,y_):
	x.ondrag(None)
	x.clear()
	x.penup()
	x.goto(-100,-100)
	x.pendown()
	x.setheading(x.towards(x_,y_))
	x.goto(x_,y_);
	conjegatedCords()
	turtle.update()
	x.ondrag(draggingx)

def draggingy(x_,y_):
	y.ondrag(None)
	y.clear()
	y.penup()
	y.goto(-100,-100)
	y.pendown()
	y.setheading(y.towards(x_,y_))
	y.goto(x_,y_);
	conjegatedCords()
	turtle.update()
	y.ondrag(draggingy)

def redrawConjegatedBases(x1,y1,x2,y2):
	subx.clear()
	subx.penup()
	subx.goto(-100,-100)
	subx.pendown()
	subx.setheading(subx.towards(x1,y1))
	subx.goto(x1,y1)

	suby.clear()
	suby.penup()
	suby.goto(-100,-100)
	suby.pendown()
	suby.setheading(suby.towards(x2,y2))
	suby.goto(x2,y2)

def clickright():
	f = 0


def main():
	turtle.listen()
	x.ondrag(draggingx)
	y.ondrag(draggingy)
	


	turtle.onscreenclick(clickright(),2)

	screen.mainloop()


turtle.update()
main()

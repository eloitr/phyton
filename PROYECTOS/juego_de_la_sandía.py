from nturl2path import pathname2url
import turtle

#Pagina principal
wn = turtle.Screen()
wn.title("Juego de la Sandía")
wn.bgcolor("white")
wn.setup(width=700, height=700)
wn.tracer(0)

#LINIES
linies =turtle.Turtle()
linies.speed(0)
linies.color("black")
linies.penup()
linies.goto(-310, 310)
linies.pendown()
linies.left(180)
for i in range(0,3):
    linies.left(90)
    linies.forward(620)



#ELEMENTS
arandano = turtle.Turtle()
arandano.speed(0)
arandano.shape("circle")
arandano.color("blue")
arandano.penup()
arandano.goto(0, 0)
arandano.shapesize(stretch_wid=1, stretch_len=1)
arandano.hideturtle()

manzana = turtle.Turtle()
manzana.speed(0)
manzana.shape("circle")
manzana.color("blue")
manzana.penup()
manzana.goto(0, 0)
manzana.shapesize(stretch_wid=1, stretch_len=1)
manzana.hideturtle()

aguacate = turtle.Turtle()
aguacate.speed(0)
aguacate.shape("circle")
aguacate.color("blue")
aguacate.penup()
aguacate.goto(0, 0)
aguacate.shapesize(stretch_wid=1, stretch_len=1)
aguacate.hideturtle()

platano = turtle.Turtle()
platano.speed(0)
platano.shape("circle")
platano.color("blue")
platano.penup()
platano.goto(0, 0)
platano.shapesize(stretch_wid=1, stretch_len=1)
platano.hideturtle()

naranja = turtle.Turtle()
naranja.speed(0)
naranja.shape("circle")
naranja.color("blue")
naranja.penup()
naranja.goto(0, 0)
naranja.shapesize(stretch_wid=1, stretch_len=1)
naranja.hideturtle()

#NUBE
nube = turtle.Turtle()
nube.speed(0)
nube.shape("circle")
nube.color("blue")
nube.penup()
nube.goto(0, 310)
nube.shapesize(stretch_wid=2, stretch_len=4)

def ir_left ():
    x = nube.xcor()
    nube.setx(x-20)
    if x < -265:
        nube.setx(x+20)
def ir_right ():
    x = nube.xcor()
    nube.setx(x+20)
    if x > 265:
        nube.setx(x-20)
    
wn.listen()
wn.onkeypress(ir_left, "Left") 
wn.onkeypress(ir_right, "Right") 






while True:
    wn.update()
    linies.hideturtle()
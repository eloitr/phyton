import time
import turtle
import random


posponer = 0.1

#ventana
wn = turtle.Screen()
wn.title("Juego de la Serpiente")
wn.bgcolor("black")
wn.setup(width= 600, height= 600)
wn.tracer(0)

#cap de la serp inicial
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("blue")
cabeza.penup()
cabeza.goto(0, 0)
cabeza_direction ="stop"


#texto

class texto(self):
    self.texto_1p

texto_1p=turtle.Turtle()
texto_1p.penup()
texto_1p.speed(0)
texto_1p.color("white")
texto_1p.hideturtle()
texto_1p.goto(500,-100)
texto_1p.write(
'''
    ______________________
    |                    |
    |                    |
    |      1 player      |
    |                    |
    |____________________|
    
''', align ="center", font = ("Courier", 24, "normal"))
texto_2p=turtle.Turtle()
texto_2p.penup()
texto_2p.speed(0)
texto_2p.color("white")
texto_2p.hideturtle()
texto_2p.goto(-600,-100)
texto_2p.write(
'''
    ______________________
    |                    |
    |                    |
    |      2 player      |
    |                    |
    |____________________|
    
''', align ="center", font = ("Courier", 24, "normal"))
def mov():
    if cabeza_direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza_direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y-20)  
    if cabeza_direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-20)   
    if cabeza_direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x+20) 
def ir_up():
    global cabeza_direction
    if cabeza_direction != "down":
        cabeza_direction = "up"
def ir_down():
    global cabeza_direction
    if cabeza_direction != "up":
        cabeza_direction = "down"  
def ir_left():
    global cabeza_direction
    if cabeza_direction != "right":
        cabeza_direction = "left"    
def ir_right():
    global cabeza_direction
    if cabeza_direction != "left":
        cabeza_direction = "right"
wn.listen()
wn.onkeypress(ir_up, "Up")  
wn.onkeypress(ir_down, "Down") 
wn.onkeypress(ir_left, "Left") 
wn.onkeypress(ir_right, "Right") 
while True:
    wn.update()
    mov()
    time.sleep(posponer)
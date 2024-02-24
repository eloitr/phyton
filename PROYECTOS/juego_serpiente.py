import turtle
import time
import random



posponer=0.1

#conf window
wn = turtle.Screen()
wn.title("Juego de Eloi")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#Cap de la serp
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0, 0)
cabeza_direction ="stop"

#menjar
menjar = turtle.Turtle()
menjar.speed(0)
menjar.shape("circle")
menjar.color("red")
menjar.penup()
menjar.goto(0, 100)
menjar_direction ="stop"

#linies
linies =turtle.Turtle()
linies.speed(0)
linies.color("cyan")
linies.penup()
linies.goto(310, -310)
linies.pendown()
for i in range(0,4):
    linies.left(90)
    linies.forward(620)
    




#cos
segmentos = []

score=0
high_score=0
texto=turtle.Turtle()
texto.penup()
texto.speed(0)
texto.color("white")
texto.hideturtle()
texto.goto(0,350)


#FUNCIONES
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
    
    
    
    if cabeza.xcor() > 280:
        y = cabeza.ycor()
        cabeza.goto(-280, y )
    
    if cabeza.xcor() < -280:
        y = cabeza.ycor()
        cabeza.goto(280, y )
        
    if cabeza.ycor() > 280:
        x = cabeza.xcor()
        cabeza.goto(x,-280)

    if cabeza.ycor() < -280:
        x = cabeza.xcor()
        cabeza.goto(x, 280)
    
    if cabeza.distance(menjar)<20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        menjar.goto(x, y)
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        score +=5
        if score >= high_score:
            high_score = score
        #texto
        
        
        texto.clear()
        texto.write(f"Score:{score}      High Score:{high_score} ", align ="center", font = ("Courier", 24, "normal"))
    
    
    
    
    totalSeg = len(segmentos)
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[totalSeg - 1].goto(x, y)
    for index in range(totalSeg-1, 0, -1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x, y)
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)
        

       
    
    linies.hideturtle()
    mov()
    
    #colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            
            cabeza_direction ="stop"
            turtle.delay(3000)
            
            cabeza.goto(0, 0)
            menjar.goto(0, 100)
            cabeza_direction ="stop"
            for segmento in segmentos:
                segmento.goto(5000, 5000)
            segmentos.clear()
            score = 0
            
           
            
            
            
            
    time.sleep(posponer)
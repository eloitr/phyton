import turtle
import time
import random



posponer=0.1

#conf window
wn = turtle.Screen()
wn.title("Juego de Eloi")
wn.bgcolor("black")
wn.setup(width= 600, height= 600)
wn.tracer(0)

#Cap de la serp
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("blue")
cabeza.penup()
cabeza.goto(-100, 0)
cabeza_direction ="stop"

cabeza_2 = turtle.Turtle()
cabeza_2.speed(0)
cabeza_2.shape("square")
cabeza_2.color("yellow")
cabeza_2.penup()
cabeza_2.goto(100, 0)
cabeza_2_direction ="stop"

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
segmentos_2 = []

score=0
high_score=0
texto=turtle.Turtle()
texto.penup()
texto.speed(0)
texto.color("white")
texto.hideturtle()
texto.goto(-350,350)

score_2=0
high_score_2=0
texto_2=turtle.Turtle()
texto_2.penup()
texto_2.speed(0)
texto_2.color("white")
texto_2.hideturtle()
texto_2.goto(350,350)


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

def mov_2():
    if cabeza_2_direction == "up":
        y = cabeza_2.ycor()
        cabeza_2.sety(y+20)
    if cabeza_2_direction == "down":
        y = cabeza_2.ycor()
        cabeza_2.sety(y-20)  
    if cabeza_2_direction == "left":
        x = cabeza_2.xcor()
        cabeza_2.setx(x-20)   
    if cabeza_2_direction == "right":
        x = cabeza_2.xcor()
        cabeza_2.setx(x+20) 

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

def ir_up_2():
    global cabeza_2_direction
    if cabeza_2_direction != "down":
        cabeza_2_direction = "up"
def ir_down_2():
    global cabeza_2_direction
    if cabeza_2_direction != "up":
        cabeza_2_direction = "down"    
def ir_left_2():
    global cabeza_2_direction
    if cabeza_2_direction != "right":
        cabeza_2_direction = "left"   
def ir_right_2():
    global cabeza_2_direction
    if cabeza_2_direction != "left":
        cabeza_2_direction = "right"

    
    
wn.listen()
wn.onkeypress(ir_up, "w")  
wn.onkeypress(ir_down, "s") 
wn.onkeypress(ir_left, "a") 
wn.onkeypress(ir_right, "d") 
wn.onkeypress(ir_up_2, "Up")
wn.onkeypress(ir_down_2, "Down")
wn.onkeypress(ir_left_2, "Left")
wn.onkeypress(ir_right_2, "Right") 

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
    
    if cabeza_2.xcor() > 280:
        y = cabeza_2.ycor()
        cabeza_2.goto(-280, y )
    if cabeza_2.xcor() < -280:
        y = cabeza_2.ycor()
        cabeza_2.goto(280, y )    
    if cabeza_2.ycor() > 280:
        x = cabeza_2.xcor()
        cabeza_2.goto(x,-280)
    if cabeza_2.ycor() < -280:
        x = cabeza_2.xcor()
        cabeza_2.goto(x, 280)
    
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
        texto.write(f"Score: {score}      High Score: {high_score} ", align ="center", font = ("Courier", 15, "normal"))
    
    if cabeza_2.distance(menjar)<20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        menjar.goto(x, y)
        nuevo_segmento_2 = turtle.Turtle()
        nuevo_segmento_2.speed(0)
        nuevo_segmento_2.shape("square")
        nuevo_segmento_2.color("grey")
        nuevo_segmento_2.penup()
        segmentos_2.append(nuevo_segmento_2)
        score_2 +=5
        if score_2 >= high_score_2:
            high_score_2 = score_2
        #texto
        texto_2.clear()
        texto_2.write(f"Score 2: {score_2}      High Score 2: {high_score_2} ", align ="center", font = ("Courier", 15, "normal"))
    
    
    
    
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
        
    totalSeg_2 = len(segmentos_2)
    if totalSeg_2 > 0:
        x_2 = cabeza_2.xcor()
        y_2 = cabeza_2.ycor()
        segmentos_2[totalSeg_2 - 1].goto(x_2, y_2)
    for index_2 in range(totalSeg_2-1, 0, -1):
        x_2 = segmentos_2[index_2-1].xcor()
        y_2 = segmentos_2[index_2-1].ycor()
        segmentos_2[index_2].goto(x_2, y_2)
    if totalSeg_2 > 0:
        x_2 = cabeza_2.xcor()
        y_2 = cabeza_2.ycor()
        segmentos_2[0].goto(x_2, y_2)

    
    
    linies.hideturtle()
    mov()
    mov_2()
    
    #colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            
            cabeza_direction ="stop"
            
            
            cabeza.goto(-100, 0)
            
            cabeza_direction ="stop"
            for segmento in segmentos:
                segmento.goto(5000, 5000)
            segmentos.clear()
            score = 0
    
    for segmento_2 in segmentos_2:
        if segmento_2.distance(cabeza_2) < 20:
            
            cabeza_2_direction ="stop"
            
            
            cabeza_2.goto(100, 0)
            
            cabeza_2_direction ="stop"
            for segmento_2 in segmentos_2:
                segmento_2.goto(5000, 5000)
            segmentos_2.clear()
            score_2 = 0
            
            
    time.sleep(posponer)
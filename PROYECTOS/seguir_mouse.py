import turtle


def dragging(x, y):

    t.goto(x,y)

wn = turtle.Screen()
wn.title("Pruebas")
wn.setup(width=600, height=600)

t = turtle.Turtle()
t.speed(-1)
# ! t.penup()


wn.onclick(dragging)
    
    
wn.mainloop()

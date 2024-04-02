import tkinter as tk
from tkinter import ttk 
from math import sqrt







ventana_principal = tk.Tk()
ventana_principal.config(width=1500, height=1000)
ventana_principal.title("Equacions de 2n grau")
def cuadraticas ():
    a_valor = ttk.Label(
    text ="a = "
    )    
    a_valor.place(x=350, y=20) 
    b_valor = ttk.Label(
    text ="b = "
    )   
    b_valor.place(x=350, y=40) 
    c_valor = ttk.Label(
    text ="c = "
    )     
    c_valor.place(x=350, y=60) 

    def calcul_equacio():

        a1 = float(caja_nombre_a.get())
        b1 = float(caja_nombre_b.get())
        c1 = float(caja_nombre_c.get())

        discriminante = b1**2 - 4*a1*c1

        if discriminante >= 0:
            x1 = (-b1 + sqrt(discriminante)) / (2*a1)
            x2 = (-b1 - sqrt(discriminante)) / (2*a1)
            resposta.config(text=f"x1={x1} i x2={x2}")
        else:
            parte_real = -b1 / (2*a1)
            parte_imaginaria = sqrt(abs(discriminante)) / (2*a1)
            x1 = complex(parte_real, parte_imaginaria)
            x2 = complex(parte_real, -parte_imaginaria)
            resposta.config(text=f"x1={x1} i x2={x2}")
    caja_nombre_a = ttk.Entry(ventana_principal)
    caja_nombre_a.place(x=400, y=20)

    caja_nombre_b = ttk.Entry(ventana_principal)
    caja_nombre_b.place(x=400, y=40)

    caja_nombre_c = ttk.Entry(ventana_principal)
    caja_nombre_c.place(x=400, y=60)

    resposta = ttk.Label(
    ventana_principal,
    text="Resultat:"
    )
    resposta.place(x=400, y=250)

    boto_calcul = ttk.Button(
    ventana_principal,
    text="Calcular",
    command=calcul_equacio
    )
    boto_calcul.place(x=400, y=100)

def calculadora ():
    calc = tk.Toplevel ()
    calc.title("Calculadora")
    calc.config(width=200, height=100)
    display = ttk.Entry(calc)
    display.grid(row=0, column=2, columnspan=2, rowspan=2)
    
    def get_numbers(n):
        current_text = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current_text + str(n))

    def operators (text):
        current_text = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current_text + text)

    def clear_display():
        display.delete(0, tk.END)

    def backspace():
        current_text = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current_text[:-1])

    
    def resolver():
        try:
            display_state = display.get()
            result = eval(display_state)
            clear_display()
            display.insert(0, result)
        except Exception:
            clear_display()
            display.insert(0, "Error")


        


    # Numeric Buttons:
    for i in range(1, 10):
        ttk.Button(calc, text=str(i), command=lambda i=i: get_numbers(i)).grid(row=(i - 1) // 3 + 3, column=(i - 1) % 3 + 1)
    
    #Operadores:
    boton_sumar=ttk.Button(calc, text="+", command= lambda :operators("+"))
    boton_sumar.grid(row=3, column=4)
    boton_restar=ttk.Button(calc, text="-", command= lambda :operators("-"))
    boton_restar.grid(row=4, column=4)

    boton_multiplicar=ttk.Button(calc, text="x", command= lambda :operators("*"))
    boton_multiplicar.grid(row=5, column=4)

    boton_dividir=ttk.Button(calc, text="/", command= lambda :operators("/"))
    boton_dividir.grid(row=6, column=4)

    boton_comma=ttk.Button(calc, text=".", command= lambda :operators("."))
    boton_comma.grid(row=6, column=1)

    boton_zero=ttk.Button(calc, text="0", command= lambda :get_numbers(0))
    boton_zero.grid(row=6, column=2)

    boton_exponente=ttk.Button(calc, text="^x", command= lambda :operators("**"))
    boton_exponente.grid(row=6, column=3)
    
    #funciones especiales
    boton_flecha=ttk.Button(calc, text="🔙", command=backspace)
    boton_flecha.grid(row=0, column=4, rowspan=2)

    boton_ac=ttk.Button(calc, text="AC", command=clear_display)
    boton_ac.grid(row=0, column=1, rowspan=2)

    boton_parentesis1=ttk.Button(calc, text="(", command= lambda :operators("("))
    boton_parentesis1.grid(row=0, column=5)

    boton_parentesis2=ttk.Button(calc, text=")", command= lambda :operators(")"))
    boton_parentesis2.grid(row=1, column=5)

    boton_igual=ttk.Button(calc, text="=", command = lambda: resolver ())
    boton_igual.grid(row= 2, column = 5, rowspan= 4)


     

def abrir_botones():
    cuadraticas_boton = ttk.Button(
    ventana_principal,
    text = "Cuadráticas",
    command = cuadraticas
    )
    cuadraticas_boton.place(x=125, y=100)
    calculadora_boton = ttk.Button(
    ventana_principal,
    text = "Calculadora",
    command = calculadora 
    ) 
    calculadora_boton.place(x=125, y=150)
    
      


boton_yes = ttk.Button(
    ventana_principal,
    text = "Sí",
    command = abrir_botones
    )
boton_yes.place(width=50, heigh=50)
boton_yes.place(x=125, y=50)

boton_no = ttk.Button(
    ventana_principal,
    text = "No"
    )
boton_no.place(width=50, heigh=50)
boton_no.place(x=200, y=50)

pregunta_inicial = ttk.Label(
    text="Vols iniciar el programa?"
)

pregunta_inicial.place(x=125, y=25)











#--------------------Càlcul_Terminal------------------------------


iniciar = input("Vols iniciar el programa(Sí/No)")
while iniciar == "Sí":
    print("PROGRAMA PER A RESOLDRE EQUACIONS DE GRAU 2: \n Inserir coeficients en l'ordre habitual (a,b i c)")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    resultat_arrel = (b**2 -4*a*c)**0.5
    b_negatiu = -b
    divisor = 2*a

    x1 = (b_negatiu + resultat_arrel)/divisor
    x2 = (b_negatiu - resultat_arrel)/divisor

    print (f"Els 2 resultats de x són {x1} i {x2}.")
    iniciar = input("Vols iniciar el programa(Sí/No)")


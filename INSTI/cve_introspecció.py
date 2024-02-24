import tkinter as tk
from tkinter import ttk 

ventana_principal = tk.Tk()
ventana_principal.config(width=375, height=100)
ventana_principal.title("INTROSPECCIÓ CVE")

text_instruccions = ttk.Label(
    ventana_principal,
    text = "Fes click a un dels botons.\nVeuràs la informació en una pestanya nova"
)
text_instruccions.place(x= 125, y=30)

separació = ttk.Label(
    ventana_principal,
    text = "|\n|\n|\n|\n|\n|\n|\n"
)
separació.place(x=100, y=0)

def fortaleses():
    fortaleses = tk.Toplevel ()
    fortaleses.title("FORTALESES")
    fortaleses.config(width=1500, height=500)
    text_fortaleses = ttk.Label(
        fortaleses,
        text = 
        "Crec que soc bo en assignatures d'aspecte tècnic/matemàtic. També en música, trompeta. \n\nCrec que se'm donen bé les mates, física, la música, tocar la trompeta... També se'm dona bé alguns tipus d'esport com la bici, córrer... \n\nCrec que allò que em distingeix de la resta és la capacitat de treballar en grup organitzadament, saber liderar i mantenir una bona comunicació, treballar eficientment sota pressió... A més de les qualitats (fortaleses) ja esmentades. \n\nEls altres veuen em mi les següents fortaleses (Company: Quim Carandell):\n\t- Treball, esforç, interès...\n\t- Se'm donen bé les mates, música...\n\t- Bons discursos, comunicació..."
        )
    text_fortaleses.place(x=0, y=0)
    
text_fortaleses = tk.Button(
    ventana_principal,
    text = "FORTALESES",
    background="DarkSeaGreen1",
    command = fortaleses
    )
text_fortaleses.place(x=0, y=0) 

def oportunitats():
    oportunitats = tk.Toplevel ()
    oportunitats.title("OPORTUNITATS")
    oportunitats.config(width=1500, height=500)
    text_oportunitats = ttk.Label(
        oportunitats,
        text="Segons les fortaleses, crec que en el meu futur veig dues clares possibilitats:\n\t- Àmbit musical (Grau superior de trompeta): ** \n\t- Ambit tècnic: ** \nCrec que per assolir aquests objectius, va ser molt positiu el canvi que l'any passat vaig fer (entrant al conservatori i venint al MIR). \nHauria de seguir en aquest camí els següents dos anys, és a dir, fer el batxillerat al MIR i mantenir oberta la possiblilitat per a les dues opcions esmentades. \nQuines accions has dut a terme perquè el que has fet funcioni? !!"
    )
    text_oportunitats.place(x=0, y=0)
    
text_oportunitats = tk.Button(
    ventana_principal,
    text = "OPORTUNITATS",
    background="cyan",
    command=oportunitats
    )
text_oportunitats.place(x=0, y=25) 

def debilitats():
    debilitats = tk.Toplevel()
    debilitats.title("DEBILITATS")
    debilitats.config(width=1500, height=500)
    text_debilitats = tk.Label(
        debilitats,
        text = ""
    )
    text_debilitats.place(x=0, y=0)
text_debilitats = tk.Button(
    ventana_principal,
    text = "DEBILITATS",
    background="red",
    command=debilitats
    )
text_debilitats.place(x=0, y=50)

def otro():
    otro = tk.Toplevel()
    otro.title("otro")
    otro.config(width=1500, height=500)
    text_otro = tk.Label(
        otro,
        text = ""
    )
    text_otro.place(x=0, y=0)
text_otro = tk.Button(
    ventana_principal,
    background="HotPink1",
    text = "otro",
    command=otro
    )
text_otro.place(x=0, y=75)

ventana_principal.mainloop()
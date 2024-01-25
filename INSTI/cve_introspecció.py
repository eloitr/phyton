import tkinter as tk
from tkinter import ttk 

ventana_principal = tk.Tk()
ventana_principal.config(width=1000, height=500)
ventana_principal.title("INTROSPECCIÓ CVE")

def fortaleses():
    fortaleses = tk.Toplevel ()
    fortaleses.title("FORTALESES")
    fortaleses.config(width=500, height=500)
    text_fortaleses = ttk.Label(
        fortaleses,
        text = 
        "Crec que soc bo en assignatures d'aspecte tècnic/matemàtic. També en música, trompeta. \n\nCrec que se'm donen bé les mates, física, la música, tocar la trompeta... També se'm dona bé alguns tipus d'esport com la bici, córrer... \n\nCrec que allò que em distingeix de la resta és la capacitat de treballar en grup organitzadament, saber liderar i mantenir una bona comunicació, treballar eficientment sota pressió... A més de les qualitats (fortaleses) ja esmentades. \n\nEls altres veuen em mi les següents fortaleses (Company: Quim Carandell):\n\t- Treball, esforç, interès...\n\t- Se'm donen bé les mates, música...\n\t- Bons discursos, comunicació..."
        )
    text_fortaleses.place(x=0, y=0)
    
text_fortaleses = ttk.Button(
    ventana_principal,
    text = "FORTALESES",
    command = fortaleses
    )
text_fortaleses.place(x=350, y=20) 

def oportunitats():
    oportunitats = tk.Toplevel ()
    oportunitats.title("OPORTUNITATS")
    oportunitats.config(width=500, height=500)
    text_oportunitats = ttk.Label(
        oportunitats,
        text="Segons les fortaleses, crec que en el meu futur veig dues clares possibilitats:\n\t- Àmbit musical (Grau superior de trompeta): ** \n\t- Ambit tècnic: ** \nCrec que per assolir aquests objectius, va ser molt positiu el canvi que l'any passat vaig fer (entrant al conservatori i venint al MIR). \nHauria de seguir en aquest camí els següents dos anys, és a dir, fer el batxillerat al MIR i mantenir oberta la possiblilitat per a les dues opcions esmentades. \nQuines accions has dut a terme perquè el que has fet funcioni? !!"
    )
    text_oportunitats.place(x=0, y=0)
    
text_oportunitats = ttk.Button(
    ventana_principal,
    text = "OPORTUNITATS",
    command=oportunitats
    )
text_oportunitats.place(x=350, y=50) 



ventana_principal.mainloop()
import tkinter as tk
from tkinter import ttk 

ventana_principal = tk.Tk()
ventana_principal.config(width=1000, height=500)
ventana_principal.title("INTROSPECCIÓ CVE")

def fortaleses():
    fortaleses = tk.Toplevel ()
    fortaleses.title("FORTALESES")
    fortaleses.config(width=200, height=100)
    
text_fortaleses = ttk.Button(
    ventana_principal,
    text = "Què se'm dona bé? Què m'agrada?",
    command = fortaleses
    )
text_fortaleses.place(x=350, y=20) 

text_oportunitats = ttk.Button(
    ventana_principal,
    text = "Segons les fortaleses, quines oportunitats tinc?" 
    )
text_oportunitats.place(x=350, y=50) 



ventana_principal.mainloop()
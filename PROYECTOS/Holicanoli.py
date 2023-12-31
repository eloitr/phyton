print("----------------------------------------------------")
inici_sessió = input("Vols iniciar sessió?(Sí/No)")
print(inici_sessió)

if inici_sessió == "Sí":
    usuari = input ("Incereix el teu nom:(Eloi/Eloi2)")
    print (usuari)
    if usuari == "Eloi":
        print(f"Hola  + {usuari}")
    elif usuari == "Eloi2":
        print("Hola " + usuari)
    else:
        print("Usuari no identificat")
elif inici_sessió == "No":
    print("Pos ves-te'n subnormal!")

else: 
    print("Resposta no vàlida.")



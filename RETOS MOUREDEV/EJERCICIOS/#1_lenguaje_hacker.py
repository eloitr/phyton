print ("Reto #1")
seguir = input ("Iniciar? ")    
while seguir == "SI" or "SÍ" or "Si" or "Sí" or "si" or "sí":
    def leet_traduction(text):
        traduccion = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
            "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
            "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
            "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}

        texto_leet = ""

        for word in text:
            if word.upper() in traduccion.keys():
                texto_leet += traduccion[word.upper()]
            else:
                texto_leet += word
        
        return texto_leet

    print (leet_traduction(input("Texto a traducir: ")))


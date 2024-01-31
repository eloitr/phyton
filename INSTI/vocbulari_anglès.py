import random
 
while True:
    vocabulari = {"zip": "cremallera", "brand":"marca", "clothing":"vestimenta", "compliment":"cumplido", "deliver":"entregar", "frames":"marcs", "glamorous":"glamurós", 
                  "hoodie":"dessuadora amb caputxa", "sleeve":"màniga", "sleeveless":"sense màniga", "stylish":"elegant", "suit":"quedar bé", "swap":"intercanviar", "layer":"capes", "plain":"pla" or "llis", "price tag":"etiqueta",
                  "range":"rango", "ripped":"estripat", "assess":"evaluar", "cheat":"fer trampes", "daydream":"estar als núvols", "draw a conclusion":"arribar a la conclusió", "figure out":"desxifrar" or "resoldre", "focus":"concentrar-se en", "gamble":"apostar",
                  "make an effort":"fer un esforç", "read someone's mind":"llegir la ment a algú", "recall":"recordar", "recognise":"recordar", "remind":"recordar a algú", "suspect":"sospitar", "take turns":"fer torns", "think over":"reflexionar", "":"",
                  "airline":"aerolínea", "board":"embarcar", "check in":"facturar", "crew":"tripulació", "delay":"retard", "fabulous":"fabulós", "flight attendant":"assafata" or "assistenta de vol", "full board":"pensió completa", "gate":"porta",
                  "half board":"mitja pensió", "high season":"temporada alta", "in advance":"per avançat", "lively":"animat", "luxurious":"de luxe", "on a budget":"pressupost", "overcrowded":"molt concorregut" or "molta get", "rate":"nota" or "Classificació", "unforgettable":"inolvidable",
                  "within walking distance":"a prop" or "a poca distància", "youth hostel":"hostal per a joves" or "hostal jove", "book":"reservar", "take off":"enlairar-se", "land":"aterrrar", "by car":"amb cotxe" or "en cotxe", "on foot":"a peu", "on time":"a temps"
    }

    escollir= random.choice(list(vocabulari.items()))
    print(escollir[0])
    resposta = input("Significat?:")
    if resposta == escollir[1]:
        print("Molt bé")
    else:
        print("malament")
  
    


else :
    print("adeu")
    
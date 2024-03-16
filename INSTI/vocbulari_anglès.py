import random

while True:
    vocabulari = {"appearance": "aspecte", "beat":"ritme", "colorful":"colorit", 
                "experience":"experiència", "flavour":"sabor" or "gust", "gorgeous":"preciós" or "bonic",
                "pattern":"estampat", "rotten":"podrit", "rough":"rugós", "scent":"olor" or "aroma",
                "scratch":"rascar" or "acariciar", "shape":"forma", "shiny":"brillant",
                "smooth":"llis" or "tranquil", "soft":"suau", "stare":"mirar fixament",
                "stink":"fer pudor" or "apestar", "tickle":"fer pessigolles", "whisper":"xiuxiuejar", "yell":"cridar"
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
    
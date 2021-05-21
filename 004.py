censura = ["ARMAS","DROGAS","PORNO"]

texto = input("Ingrese un texto: ").strip()
lista = texto.upper().split(" ")

for i in range(len(censura)):
    if censura[i] in lista:
        print("Contenido no apto para menores.")

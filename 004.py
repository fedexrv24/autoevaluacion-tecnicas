censura = ["ARMAS","DROGAS","PORNO"]

while True:
    pregunta = input("Desea ingresar una nueva palabra inapropiada? \nS / N \n").upper().strip()
    if pregunta == "N":
        print("No")
        break

    elif pregunta == "S":
        add = input("Ingrese la nueva palabra: ").upper().strip()
        censura.append(add)
        print(censura)
        continue

    else:
        print("Opcion incorrecta.")
        continue

texto = input("Ingrese un texto: ").upper().strip()
lista = texto.split(" ")

for i in range(len(censura)):
    if censura[i] in lista:
        no_apto = input("Contenido no apto para menores.\nVer? \nS / N \n").upper().strip()

        if no_apto == "N":
            break

        elif no_apto == "S":
            print(texto.capitalize())
            break

        else:
            print("Opcion incorrecta.")
            continue

    elif i == len(censura)-1:
        print(texto.capialize())
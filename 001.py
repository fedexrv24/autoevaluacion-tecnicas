caracter = ""
string = input("Ingresar cadena de texto: ").strip()

for i in string:
        print(caracter + i)
        caracter += "_"
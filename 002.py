prom = 0
tot = 0
numeros = input("Ingrese numero: ").strip()

while True:
        if len(numeros) == 0:
                break
        try:
                decimal = float(numeros)
                tot += decimal
                prom += 1

        except ValueError:
                print("Error. Ingrese un numero.")

        numeros = input("Ingrese numero o enter para salir: ").strip()

resultado = tot / prom
print(resultado)
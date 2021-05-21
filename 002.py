total = []
numeros = input("Ingrese numero: ").strip()

while True:
        if len(numeros) == 0:
                break
        try:
                decimal = float(numeros)
                total.append(decimal)

        except ValueError:
                print("Error. Ingrese un numero.")

        numeros = input("Ingrese numero o enter para salir: ").strip()

prom = 0
for i in total:
    prom += i

print(prom/len(total))
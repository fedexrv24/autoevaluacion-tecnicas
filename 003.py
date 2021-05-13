mail = input("Ingrese un mail: ").strip()

lista = mail.split("@")
lista2 = lista[1].split(".")
print(lista2[0].capitalize())
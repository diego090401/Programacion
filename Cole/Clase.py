canasta = {}
seguir = True
while seguir :
    art = input("Ingrese el nombre de su articulo: ")
    precio = int(input("Ingrese el precio de su articulo: "))
    canasta[art] = precio
    seguir = input("Desea seguir ?").lower()
    if seguir == "si":
        pass
    else:
        break
print(canasta.keys)
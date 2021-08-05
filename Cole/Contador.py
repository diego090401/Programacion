def contador():
    nombre = input("Ingrese su nombre: ")
    contador = 0
    letra = input("Ingrese la letra que quiere evaluar: ")
    for a in nombre:
        if a == letra:
            contador = contador + 1
    return contador

contador =contador()
print(contador)
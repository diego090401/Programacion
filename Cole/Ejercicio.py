indice = int(input("De cuanto quiere que sea su lista: "))
lista = []
posicion = 0

for i in range(indice):
    print (posicion)
    lista.append("")

    lista[posicion] = input("Ingrese el nuevo valor: ")
    posicion = posicion + 1


print(lista) 
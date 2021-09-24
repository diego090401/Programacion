def Cedula_sin_repetir():
    Cedula = [int(i) for i in input("Por favor ingrese su cedula con formato X-XXXX-XXXX: ") if i != "-"]
    Cedula.remove(0)
    Cedula_sin_repetir = []
    for i in Cedula:
        if Cedula_sin_repetir.count(i) == 0:
            Cedula_sin_repetir.append(i)
    Cedula_sin_repetir.sort()
    return Cedula_sin_repetir

def Promedio(Lista):
    Total = 0
    for i in Lista : 
        Total  = Total + i
    Promedio = int(Total) // len(Lista)
    return Promedio

def Palabra(Promedio):
    Palabra = input(f'Ingrese una palabra de {Promedio} letras: ')
    return Palabra[Promedio//3]

def run():
    Lista = Cedula_sin_repetir()
    P = Promedio(Lista)
    MiPalabra = Palabra(P)
    print(MiPalabra)
if __name__ == '__main__':
    run()
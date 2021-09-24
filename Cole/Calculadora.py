Lista = input("Ingrese su operacion en formato X + B: ")

Suma = Lista.count("+")
Resta =Lista.count("-")
Divison =Lista.count("/")
Multiplicacion = Lista.count("*")
if Suma == 1 :
    Valor1, valor2 =Lista.split("+")
    print( int(Valor1) +int(valor2))
if Resta == 1 :
    Valor1, valor2 =Lista.split("-")
    print( int(Valor1) -int(valor2))
if Multiplicacion == 1 :
    Valor1, valor2 =Lista.split("*")
    print( int(Valor1) *int(valor2))
if Divison == 1 :
    Valor1, valor2 =Lista.split("/")
    print( int(Valor1) /int(valor2))
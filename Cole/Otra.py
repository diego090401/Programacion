#Programa que verifique si una palabra es un palindromo 
palabra = str(input("Ingrese una palabra: "))
try : 
    palabra = str(palabra)
except:
    print("El caracter ingresado no esta compuesto solo por letras, intente de nuevo")
    exit()
lowercase = palabra.lower()
p_a_l = list (lowercase)
p_r = p_a_l[:: -1]
if p_r == p_a_l:
    print("Es un palindromo")
else: 
    print("No es un palindromo")
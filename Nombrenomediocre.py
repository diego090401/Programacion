Nombre = input("Ingrese su nombre y apellido: ")
Nombre = list(Nombre)
for i in range(len(Nombre)):
    if Nombre[i] == " ":
            Nombre[i] = "."
        
print(''.join(Nombre) + "@ccal.com")


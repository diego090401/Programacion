Cedula = input("Ingrese su cedula: ")
Indice = 0 
Cedula = list(Cedula)
Cedula_0 = []
for i in range(len(Cedula)):
    if i == 1 or i == 5:
        if Cedula[i] == '0':
            pass
    else: 
        Cedula_0.append(Cedula[i])



if Cedula_0[0] == "1":
    print("\nSan Jose")
elif Cedula_0[0] == "2" :
        print("\nAlajuela")
elif Cedula_0[0] == "4" :
        print("\nCartago") 
elif Cedula_0[0] == "5" :
        print("\nGuanacaste") 
elif Cedula_0[0] == "6" : 
        print("\nPuntarenas")
elif Cedula_0[0] == "7":
        print("\nLimon") 

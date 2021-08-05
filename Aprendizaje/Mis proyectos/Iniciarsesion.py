def InsertUser(Users): # Funcio para que las personas puedan ingresear un nuevo usuario
    
    UserCount = input("Cuantos usuarios quieres ingresar: ")
    
    try: #Asegurandose que el usuario solo digite numeros
        UserCount == int(UserCount)
    except:
        print( "El valor ingresado no es un numero")
        exit()
    UserCount = int(UserCount)
    for i in range (UserCount): # Loop para crear la cantidad de usuarios deseada
        Username = str(input("Ingrese el nombre de su nuevo usuario: "))
        password = str(input("Ingrese su clave: "))
        try: 
            password = input("Ingrese su clave de nuevo: ")
        except:
            print("Las claves no coiciden, por favor intente de nuevo")
            exit()
        User = dict(Userkey = Username, passwordkey = password)
        Users.append(User)
        print(User)
    
def Login(Users): #Esta es una funcion para el momento en el que el usuario tenga que iniciar sesion
    found = False
    access = False
    log = input("Ingrese su usuario: ")
    for i in range(len(Users)):
        if Users[i]["Userkey"] == log :
            Userid = i 
            
            found = True
    if found == True:
        
        password = input("Ingrese su clave: ")      
        if Users[i]["passwordkey"] == password:
            print("Ha ingresado con exito")
            access = True
            return access
        else:
            print("Clave incorrecta")
    else:
        print("El usuario no existe")
    return access
    
    

def Update(Users): #Funcion para que el usuario pueda actualizar sus clave  
    access = Login(Users)
    if access  == True:
        NewPassworKey = input("Ingrese su nueva clave: ")
        Users[Userid]["passwordkey"] = NewPassworKey
        
        

def Compro(par):

    if par == "s" or par =="n":
        pass
    else:
        print("No ha ingresado ninguna de las opciones, intente de nuevo")
        exit()
Userid = 0
Users = [{"Userkey": "Prueba", "passwordkey" : "1234" }]

def run():
    while True :
        
        Eleccion = input("Desea ingresar un usuario nuevo(s o n) ? ")
        Eleccion.lower()
        Compro(Eleccion)
        if Eleccion == "s":
            InsertUser(Users )
            
        
        
        Eleccion = input("Desea ingresar a su cuenta (s o n) ? ")
        Eleccion.lower()
        Compro(Eleccion)
        if Eleccion == "s":
                Login(Users)

        
        Eleccion = input("Desea actualizar su clave (s o n) ? ")
        Eleccion.lower()
        Compro(Eleccion)
        if Eleccion == "s":
            Update(Users)

            
        Eleccion = input("Desea volver al inicio (s o n) ? ")
        Eleccion.lower()
        Compro(Eleccion)
        if Eleccion == "s":
            print (Users)
        else:
            exit()
        
    

if __name__ == '__main__' :
    run()

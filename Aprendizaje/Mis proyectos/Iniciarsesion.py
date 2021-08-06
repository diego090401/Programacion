Userid = 0
Users = [{"Userkey": "Prueba", "passwordkey" : "1234" }]

def InsertManyUsers(): # Funcion para que las personas puedan ingresear varios usuarios al mismo tiempo
    
    UserCount = input("Cuantos usuarios quieres ingresar: ") # Se le pregunta al usuario cuantos perfiles quiere ingresar
    
    try: #Asegurandose que el usuario solo digite numeros
        UserCount == int(UserCount)
    except:
        print( "El valor ingresado no es un numero")
        exit()
    UserCount = int(UserCount)
    for i in range (UserCount): # For para crear la cantidad de usuarios deseada
        Username = str(input("Ingrese el nombre de su nuevo usuario: "))
        for i in range(len(Users)): #For para aseguararse de que el usuario que se quiere ingresar no exista en la base de datos 
            if Users[i]["Userkey"]== Username:
                print("El usuario ya existe")
                exit()

        password = str(input("Ingrese su clave: "))
        try: 
            password = input("Ingrese su clave de nuevo: ")
        except:
            print("Las claves no coiciden, por favor intente de nuevo")
            exit()
        User = dict(Userkey = Username, passwordkey = password) #Agrega a la lista de usuarios un diccionario con la clave del usuario y su nombre
        Users.append(User)
        print("Usuario ingresado con exito")
    

def InsertUser(): # Funcion para ingresar un unico usuario
        Username = str(input("Ingrese el nombre de su nuevo usuario: "))
        for i in range(len(Users)): #For para aseguararse de que el usuario que se quiere ingresar no exista en la base de datos 
            if Users[i]["Userkey"]== Username:
                print("El usuario ya existe")
                exit()
        password = str(input("Ingrese su clave: "))
        try: 
            password == input("Ingrese su clave de nuevo: ")
        except:
            print("Las claves no coiciden, por favor intente de nuevo")
            exit()
        User = dict(Userkey = Username, passwordkey = password) #Agrega a la lista de usuarios un diccionario con la clave del usuario y su nombre
        Users.append(User)
        print("Usuario ingresado con exito")
    
def Login(): #Esta es una funcion para el momento en el que el usuario tenga que iniciar sesion
    found = False
    log = input("Ingrese su usuario: ") # Le pedimos a la persona su usuario y nos aseguramos de que exista en la base de datos
    for i in range(len(Users)):
        if Users[i]["Userkey"] == log :
            Userid = i 
            found = True

    if found == True: # Si si se encontro el usuario, se le solicita que ingrese su constrasena y nos aseguramos que esta coincida con los registros de la base de datos
        
        password = input("Ingrese su clave: ")      
        if Users[i]["passwordkey"] == password:
            print("Ha ingresado con exito")
            access = True
            
        else:
            print("Clave incorrecta")
    else:
        print("El usuario no existe")
    return access
    
def Update(access): #Funcion para que el usuario pueda actualizar sus clave  
    
    if access  == True: #Sirve para saber si el usuario ya inicio sesio o si todavia no lo ha hecho
        NewPassworKey = input("Ingrese su nueva clave: ")
        Users[Userid]["passwordkey"] = NewPassworKey
    while access == False:
        Login()
      
def Compro(par): # Esta funcion sirve para comprobar que los valores digitados por el usuario si sean alguna de las opciones disponibles

    if par == "s" or par =="n":
        pass
    else:
        print("No ha ingresado ninguna de las opciones, intente de nuevo")
        exit()

def run(): #Funcion donde corre el codigo princpal
    while True :
        
        Eleccion = input("Desea ingresar usuarios ?(s o n) \nEn caso de quere ingresar mas de uno digite sx: ")
        if Eleccion == "s" or Eleccion =="n" or Eleccion == "sx":
            pass
        
        else:
            print("No ha ingresado ninguna de las opciones, intente de nuevo")
            exit()

        if Eleccion == "s":
            InsertUser()
        if Eleccion =="sx":
            InsertManyUsers()

        Eleccion = input("Desea ingresar a su cuenta (s o n) ? ")
        Eleccion.lower()
        Compro(Eleccion)
        if Eleccion == "s":
                access = Login()

        Eleccion = input("Desea actualizar su clave (s o n) ? ")
        Eleccion.lower()
        Compro(Eleccion)
        if Eleccion == "s":
            Update( access)

        Eleccion = input("Desea volver al inicio (s o n) ? ")
        Eleccion.lower()
        Compro(Eleccion)
        if Eleccion == "s":
            pass
        else:
            exit()
        
if __name__ == '__main__' : #Entry point
    run()

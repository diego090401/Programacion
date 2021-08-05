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
    
def Login(Users): #Esta es una funcio para el momento en el que el usuario tenga que iniciar sesio
    indice = 0 
    log = input("Ingrese su usuario: ")
    for i in range(len(Users)):
        if Users[i]["Userkey"] == log :
            indice = i
            print("Si sirvio")
    


def Update(Users): #Funcio para que el usuario pueda actualizar sus datos
    pass

def Compro(par, Status):

    if par == "s" or par =="n":
        pass
    else:
        print("No ha ingresado ninguna de las opciones, intente de nuevo")
        exit()
   
Users = []
Status = 1 
def run():
    while Status == 1 :
        print("Desea ingresar un usuario nuevo(s o n): ")
        Eleccion = input()
        Eleccion.lower()
        Compro(Eleccion, Status)
        if Eleccion == "s":
            InsertUser(Users)
            
        
        print("Desea ingresar a su cuenta (s o n)")
        Eleccion = input()
        Eleccion.lower()
        Compro(Eleccion, Status)
        if Eleccion == "s":
                Login(Users)

        print("Desea actualizar los datos de su cuenta ?")
        Eleccion = input()
        Eleccion.lower()
        Compro(Eleccion, Status)
        if Eleccion == "s":
            Update(Users)
    

if __name__ == '__main__' :
    run()

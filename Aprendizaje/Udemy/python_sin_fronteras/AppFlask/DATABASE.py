import mysql.connector
class DATABASE():
    DATAB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = 'Diego0904',
    database = 'tareas',
    )
    cursor = DATAB.cursor()
    def InsertIntoUsuarios(DATAB= DATAB, cursor=cursor):
        NewUsername = str(input("Ingrese su nombre de usuario :"))
        NewMail = str(input("Ingrese su email: "))
        NewPassword = str(input("Ingrese su constraseña: "))
        NewUser = (NewUsername, NewMail, NewPassword)
        InsertIntoUsuarios = "insert into usuarios(username, user_mail, user_password) values (%s, %s, %s)"
        cursor.execute(InsertIntoUsuarios, NewUser)
        DATAB.commit()
        
    def UpdateUsername(DATAB= DATAB, cursor=cursor) : 
        
        LastaUsername, UpdatedUsername=  str(input("Ingrese su anterior nombre de usuario: ")), str(input("Ingrese su nuevo nombre de usuario: "))
        UpdatedData = (UpdatedUsername, LastaUsername)
        UpdateUsername = "update usuarios set username = %s where username = %s"
        cursor.execute(UpdateUsername, UpdatedData)
        DATAB.commit()

    def ShowUsuarioTable(DATAB= DATAB, cursor=cursor):
        cursor.execute("select username from usuarios")
        RawUsuarioTable =cursor.fetchall()
        
        return RawUsuarioTable
    def DeleteUser (DATAB= DATAB, cursor=cursor):
        DeleteUser = "delete from usuarios where usuario_id = %s"
        Usuario_id = (4, )
        cursor.execute(DeleteUser, Usuario_id)
        DATAB.commit()
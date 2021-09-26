import mysql.connector
from DATABASE import DATABASE as db

def run():
    # db.ShowUsuarioTable()
    # db.InsertIntoUsuarios()
    # db.ShowUsuarioTable()
    db.DeleteUser()
if __name__ == "__main__":
    run()
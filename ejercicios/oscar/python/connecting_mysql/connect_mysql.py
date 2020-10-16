import mysql.connector

class mysql():

    def connectar():
        mydb = mysql.connector.connect(
        host="108.179.252.18",
        user="grupo859_oscar",
        password="Oscar12345",
        database="grupo859_estudios_python"
        )

    def crear_tabla()
print(mydb)


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE clientes (nombre VARCHAR(255))")



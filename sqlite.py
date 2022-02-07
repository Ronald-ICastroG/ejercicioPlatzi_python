import sqlite3


conn=sqlite3.connect('merge.db')

cursor=conn.cursor()

#CREAR TABLA
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre VARCHAR,
    apellidos VARCHAR,
    edad integer,
    genero varchar
    )
    """);

if conn!=None:
    print(f"conexion establecida ...{merge}")


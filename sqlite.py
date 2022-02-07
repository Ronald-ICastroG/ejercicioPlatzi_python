from heapq import merge
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
    print(f"conexion establecida a {merge}")

#Insertar

#cursor.execute("INSERT INTO usuarios VALUES(null,'pietro','salchicha',34,'M')")
#conn.commit()

users=[
    ('Juan','Pindonga',29,'M'),
       ('Pedro','Rimalas',33,'M'),
       ('Diego','ConBotas',88,'M'),
       ('Dalia','Morantes',40,'F')
       ]

cursor.executemany("INSERT INTO usuarios values (null,?,?,?,?)",users)
conn.commit()

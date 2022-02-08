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
    print("conectado con exito")

#Insertar

#cursor.execute("INSERT INTO usuarios VALUES(null,'pietro','salchicha',34,'M')")
#conn.commit()

users=[
    ('Juan','Pindonga',29,'M'),
       ('Pedro','Rimalas',33,'M'),
       ('Diego','ConBotas',88,'M'),
       ('Dalia','Morantes',40,'F')
       ]

#cursor.executemany("INSERT INTO usuarios values (null,?,?,?,?)",users)
#conn.commit()


#read


"""
cursor.execute("SELECT * FROM usuarios")
usuarios=cursor.fetchall()

for usuario in usuarios:
    print("ID: ",usuario[0])
    print("Nombre: ",usuario[1])
    print("Apellidos: ",usuario[2])
    print("Edad: ",usuario[3])
    print("Género: ",usuario[4])
    print("\n ------------------")
    
conn.commit()
"""

#update

cursor.execute("Update usuarios SET nombre='Francisco' WHERE nombre='Pedro'")

conn.commit()
#rowcount falta





#Delete
cursor.execute("delete from usuarios where nombre='pietro'")
conn.commit()
print(cursor.rowcount)




conn.close()




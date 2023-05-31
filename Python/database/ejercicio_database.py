"""
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo
entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
"""

import os
import sqlite3


def create_table_alumnos(database, table):
    if not os.path.isfile(database):
        # Create database
        con = sqlite3.connect(database)
        cur = con.cursor()
        query = f"""CREATE TABLE "{table}" (
                "ID"	INTEGER NOT NULL UNIQUE,
                "nombre"	TEXT,
                "apellido"	TEXT,
                PRIMARY KEY("ID" AUTOINCREMENT)
            );"""
        cur.execute(query)
        con.close()

def add_alumnos(database, table, nombre, apellido):
    con = sqlite3.connect(database)
    cur = con.cursor()
    query = f"""INSERT INTO {table} (nombre, apellido) VALUES ("{nombre}", "{apellido}") """
    cur.execute(query)
    con.commit()
    con.close()

def search_by_name(database, table, nombre):
    con = sqlite3.connect(database)
    cur = con.cursor()
    query = f"""SELECT * FROM {table} WHERE "nombre" = '{nombre}' """
    res = cur.execute(query)
    values = res.fetchall()
    con.close()
    return values

database = 'mydatabase.db'
table = 'Alumnos'

# Crear tabla vacía con estructura (id, nombre, apellido)
create_table_alumnos(database, table)


# Se llena con nombres y apellidos
nombres = ['Juan', 'Pablo', 'Pedro', 'Ricardo', 'Oihana', 'Maria', 'Valentina', 'Paco', 'Juan']
apellidos = ['Martinez', 'García', 'Ortíz', 'Romero', 'Salto', 'Botella', 'Vaso', 'Taza', 'Primo']

for nya in zip(nombres, apellidos):
    add_alumnos(database, table, nya[0], nya[1])

# Se busca un nombre y se muestran los resultados
nombre_a_buscar = 'Juan'
busqueda = search_by_name(database, table, nombre_a_buscar)
if len(busqueda)>0:
    print(f'Los siguientes resultados corresponde a tu búsqueda de {nombre_a_buscar}')
    for resultados in busqueda:
        print(f"\t* [ID: {resultados[0]}] {resultados[1]} {resultados[2]}")
else:
    print(f'Lo siento. No hay ningún resultado para la búsqueda de {nombre_a_buscar}')
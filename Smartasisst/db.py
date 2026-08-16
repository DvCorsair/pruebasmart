import sqlite3
import os


def crear_base():

    os.makedirs(
        "datos",
        exist_ok=True
    )

    conexion = sqlite3.connect(
        "C:/Users/leand/OneDrive/Desktop/Smartasisst/datos/reclamos.db"#Configuren C.........\\datos\\reclamos.db para windows
    )

    cursor = conexion.cursor()#sin el curso no hay consulta. Puntero

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS historial_reclamos(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        comentario TEXT,

        categoria TEXT,

        prioridad TEXT

    )

    """)

    conexion.commit()
    conexion.close()

#Inicia la carga de comentarios
def guardar_reclamo(
    comentario,
    categoria,
    prioridad
):

    conexion = sqlite3.connect(
        "datos/reclamos.db"
    )

    cursor = conexion.cursor()

    cursor.execute("""

    INSERT INTO historial_reclamos(
        comentario,
        categoria,
        prioridad
    )

    VALUES (?, ?, ?)

    """,

    (
        comentario,
        categoria,
        prioridad
    ))

    conexion.commit()
    conexion.close()


def mostrar_historial():

    conexion = sqlite3.connect(
        "datos/reclamos.db"
    )

    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM historial_reclamos"
    )

    registros = cursor.fetchall()#metodo para obtener las filas (de tuplas) de la consulta

    conexion.close()

    return registros

#Actualizar 27-6-26

def actualizar_reclamo( id_reclamo, categoria, prioridad ): 
    
    conexion = sqlite3.connect( "datos/reclamos.db" ) #\ \\actualizar direcciones en el caso de windows
    
    cursor = conexion.cursor() 
    
    cursor.execute(""" UPDATE historial_reclamos SET categoria = ?, 
                   prioridad = ? 
                   WHERE id = ? """, 
    ( categoria, prioridad, id_reclamo )) 
    conexion.commit() 
    conexion.close()

#Eliminar 27-6-26

def eliminar_reclamo( id_reclamo ): 
    
    conexion = sqlite3.connect( "datos/reclamos.db" ) 
    
    cursor = conexion.cursor() 
    
    cursor.execute(""" DELETE FROM historial_reclamos WHERE id = ? """, (id_reclamo,)) 
    
    conexion.commit() 
    
    conexion.close()

#Contar reclamos 3-7-26

def contar_reclamos():

    conexion = sqlite3.connect("datos/reclamos.db")

    cursor = conexion.cursor()

    cursor.execute("""

    SELECT COUNT(*)

    FROM historial_reclamos

    """)

    cantidad = cursor.fetchone()[0]

    conexion.close()

    return cantidad

#buscar categorias 3-7-26
def buscar_categoria(categoria):

    conexion = sqlite3.connect("datos/reclamos.db")

    cursor = conexion.cursor()

    cursor.execute("""

    SELECT *

    FROM historial_reclamos

    WHERE categoria = ?

    """,

    (categoria,))

    registros = cursor.fetchall()

    conexion.close()

    return registros

#Contar por categorías
def contar_por_categoria():

    conexion = sqlite3.connect("datos/reclamos.db")

    cursor = conexion.cursor()

    cursor.execute("""

    SELECT categoria,
           COUNT(*)

    FROM historial_reclamos

    GROUP BY categoria

    """)

    datos = cursor.fetchall()

    conexion.close()

    return datos

import sqlite3
import pandas as pd


def cargar_datos():

    conexion = sqlite3.connect("datos/reclamos.db")

    df = pd.read_sql_query(
        "SELECT * FROM historial_reclamos",
        conexion
    )

    conexion.close()

    return df


def generar_estadisticas():

    df = cargar_datos()

    return {
        "total": len(df),
        "categorias": df["categoria"].value_counts(),
        "prioridades": df["prioridad"].value_counts()
    }


"""
import sqlite3
import pandas as pd

conexion = sqlite3.connect(
    "datos/reclamos.db"
)

df = pd.read_sql_query(
    "SELECT * FROM historial_reclamos",
    conexion
)
#print(df)
#print(df.head()) #las primeras cinco
#print(df.tail()) #las últimas cinco
#print(len(df))
#print(df.info())
#print(df.describe())
#print(
#    df["categoria"].value_counts()
#)
#print(
#   df["prioridad"].value_counts()
#)
#conexion.close()
"""

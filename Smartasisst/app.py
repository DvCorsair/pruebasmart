from analizador import analizar_comentario
from respuesta import generar_respuesta
from db import guardar_reclamo
from db import mostrar_historial
from analisis import generar_estadisticas#esto agrego para el bloque de estadíticas
##from ia import consultar_ia#agregar este import para obtener los datos de la funcion consultar_ia
import streamlit as st

st.title("SmartAssist AI Analyst")
st.subheader("Sistema Inteligente de Gestión de Reclamos")
st.write("Bienvenido al sistema.")
st.divider()#separador

#agregando componentes
comentario = st.text_area(
    "Ingrese el comentario"
)
#Botón
#if st.button("Analizar"):
#    print(comentario)

if st.button("Procesar"):
    resultado = analizar_comentario(
        comentario
    )
    respuesta = generar_respuesta(
        resultado["categoria"]
    )
    guardar_reclamo(
        comentario,
        resultado["categoria"],
        resultado["prioridad"]
    )
    st.success("Reclamo registrado.")
    st.write(resultado)
    st.write(respuesta)

#Historial
if st.button(
    "Ver historial"
):
    historial = mostrar_historial()
    st.table(historial)

#Estadísticas--> usamos analisis.py

if st.button("Ver Estadísticas"):

   estadisticas = generar_estadisticas()

   #agregar cálculos para identificar la categoría predominante 

   categoria = estadisticas["categorias"].idxmax()

   cantidad = estadisticas["categorias"].max()

   #podemos hacer lo mismo con las prioridades
   
   prioridad = estadisticas["prioridades"].idxmax()
   
   cantidad = estadisticas["prioridades"].max()



   #st.write(estadisticas) #aqui muestra un diccionario por eso comento
   
   st.metric(
    "Total de reclamos",
    estadisticas["total"]
   )

   st.subheader("Cantidad por categoría")

    #mostrar por categoría
   st.write(
    estadisticas["categorias"]
   )

   st.subheader("Gráfico por categorías")
   #mostrar por gráfico
   st.bar_chart(
    estadisticas["categorias"]

    #prioridades
   )
   st.subheader("Cantidad por prioridad")

   st.write(
    estadisticas["prioridades"]
  )

   st.bar_chart(
    estadisticas["prioridades"]
    )
###################
   st.subheader("Cálculos automáticos")

   st.success(
        f"Categoría predominante: {categoria} ({cantidad} reclamos)"
    )
   st.info(
        f"Prioridad predominante: {prioridad} ({cantidad})"
    )


#IA
st.header(" Análisis Inteligente")
if st.button("Generar informe con IA"):
    estadisticas = generar_estadisticas()
    prompt = f"""
    Estas son las estadísticas del sistema:
    {estadisticas}
 Elabora un informe indicando:
    - categoría predominante;
    - prioridad predominante;
    - posibles causas;
    - tres recomendaciones. """

    #respuesta = consultar_ia(prompt)#aqui falta el desarrollo
    st.write(respuesta)

#Salir
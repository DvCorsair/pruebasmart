from api_client import obtener_datos
from analizador import analizar_comentario 
from respuesta import generar_respuesta
from db import (crear_base, guardar_reclamo, mostrar_historial, actualizar_reclamo, eliminar_reclamo, contar_reclamos, buscar_categoria, contar_por_categoria )
from analisis import generar_estadisticas

crear_base() 

while True: 
    
    print("\nSMARTASSIST AI ANALYST") 
    print("1 - Nuevo reclamo") 
    print("2 - Ver historial") 
    print("3 - Modificar reclamo") 
    print("4 - Eliminar reclamo")
    print("5 - Contar Reclamos")
    print("6 - Buscar por categoría") 
    print("7 - Estadísticas con Pandas")
    print("8 - Generar Reporte")
    print("9 - Salir") 
    opcion = input( "\nSeleccione una opción: " ) 
    
    if opcion == "1": 
        comentario = input( "\nIngrese comentario: " ) 
        resultado = analizar_comentario( comentario ) 
        respuesta = generar_respuesta( resultado["categoria"] ) 
        guardar_reclamo( comentario, resultado["categoria"], resultado["prioridad"] ) 
        print( "\nCategoría:", resultado["categoria"] ) 
        print( "Prioridad:", resultado["prioridad"] ) 
        print( "Respuesta:", respuesta ) 
    
    elif opcion == "2": 
        historial = mostrar_historial() 
        print("\nHISTORIAL") 
        for fila in historial: 
            print(fila) 
            
    elif opcion == "3": 
        id_reclamo = int( input( "\nID del reclamo: " ) ) 
        categoria = input( "Nueva categoría: " ).upper() 
        prioridad = input( "Nueva prioridad: " ).upper()
        actualizar_reclamo( id_reclamo, categoria, prioridad ) #llama a la función actualizar_reclamo que esta db.py
        print( "\nReclamo actualizado." ) 
        
    elif opcion == "4": 
        id_reclamo = int( input( "\nID a eliminar: " ) ) 
        eliminar_reclamo( id_reclamo ) #llama a la función eliminar_reclamo que esta en db.py
        print( "\nReclamo eliminado." ) 

    elif opcion == "5":
        contar = contar_reclamos()
        print( "\n Cantidad de Reclamos:", contar ) 

    elif opcion == "6":
        categoria = input( "Nombre de la categoría: " ).upper() 
        print(categoria)
        resultado = buscar_categoria(categoria)
        print("\nListado por categoría seleccionada.")
        for fila in resultado: 
            print(fila) 
        
    elif opcion == "7":
        
        estadisticas = generar_estadisticas()

        print("\n===== SMARTASSIST ANALYTICS =====")

        print(f"\nTotal de reclamos: {estadisticas['total']}")

        print("\nCategorías:")
        print(estadisticas["categorias"])

        print("\nPrioridades:")
        print(estadisticas["prioridades"])
        
        #generar_estadisticas()
        #resultado = generar_estadisticas()
        #print("\nCantidad de reclamos por categorías: ")
        #for fila in resultado: 
            #print( "\nCategoría:", ["categoria"] ) 
        #    print(fila) 
    
    elif opcion == "8":
        #def generar_reporte():
            total = contar_reclamos()
            categorias = contar_por_categoria()
            print()
            print("========================")
            print("REPORTE SMARTASSIST")
            print("========================")
            print()
            print("Total de reclamos:", total)
            print()
            for categoria, cantidad in categorias:
                print(categoria, ":", cantidad )
            
        
    elif opcion == "9": 
        print( "\nHasta luego." )          
        break 
    
    else: print( "\nOpción incorrecta." )

def generar_respuesta(categoria):

    respuestas = {

        "ERROR_ACCESO":
        "Verifique sus credenciales e intente nuevamente.",

        "RENDIMIENTO":
        "Nuestro equipo está revisando el rendimiento del sistema.",

        "FACTURACION":
        "Su consulta fue derivada al área administrativa.",

        "CONSULTA":
        "Gracias por contactarse con nosotros.",

        "DEVOLUCION":
        "Nuestro equipo esta verificando tu caso",

        "CANCELACION":
        "En un minuto nos comunicamos"
    }

    return respuestas[categoria]

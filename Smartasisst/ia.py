import ollama

def consultar_ia(prompt):

    respuesta = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un analista de soporte técnico. "
                    "Debes elaborar informes claros, profesionales, "
                    "objetivos y basados únicamente en los datos recibidos."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return respuesta["message"]["content"]
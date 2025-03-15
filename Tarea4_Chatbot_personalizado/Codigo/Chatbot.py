from openai import OpenAI
import requests

# Reemplaza 'TU_API_KEY' con tu Clave API de DeepSeek
API_KEY = 'sk-53751d5c6f344a5dbc0571de9f51313e' 
API_URL = 'https://api.deepseek.com/v1/chat/completions'


def enviar_mensaje(message, modelo="deepseek-chat"):
    headers = {
        'Authorization': f"Bearer {API_KEY}",
        'Content-Type': 'application/json'
    }

    # Historial de mensajes en formato correcto
    historico = [
        {"role": "system", "content": "Simula la especialidad de Paul ekman en las emociones y responde cada pregunta con mucho cariño"},
        {"role": "user", "content": message}
    ]

    data = {
        'model': modelo,
        'messages': historico
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as err:
        return f"Error de la API: {err}"
    except Exception as e:
        return f"Error inesperado: {e}"

def main():
    print("Bienvenido al chatbot de DeepSeek. Escribe 'salir' para terminar.")
    while True:
        message_usuario = input('Tu: ')
        if message_usuario.lower() == 'salir':
            print("Chatbot: ¡Hasta luego!")
            break
        respuesta = enviar_mensaje(message_usuario)
        print(f"Chatbot: {respuesta}")

if __name__ == "_main_":
    main()
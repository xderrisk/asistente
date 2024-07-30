import google.generativeai as genai
from src.apis import Gemini_API
from tiempo import Tiempo

class ChatIAGenerativa:
    def __init__(self):
        self.configure()
        self.setup_model()

    def configure(self):
        genai.configure(api_key=Gemini_API)
        self.instrucciones = """
        Eres un asistente que trata de explicar cualquier tema de forma breve
        y solo cuando le pida algo en especifico como tipos de alguna cosa
        me responderas con mas texto, pero recuerda se lo mas breve posible
        y sigue estas instrucciones:

        1. Cuando se trate de numeros y expresiones matematicas me responderas con el nombre en letras
        
        repondeme a lo siguente: 
        """

    def setup_model(self):
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 100,
            "response_mime_type": "text/plain",
        }

        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash-latest",
            generation_config=self.generation_config,
        )

        self.chat_session = self.model.start_chat(history=[])

    def send_message(self, message):
        response = self.chat_session.send_message(self.instrucciones+message)
        print("\n"+response.text)
        return response.text

if __name__ == "__main__":
    chat_bot = ChatIAGenerativa()
    response = chat_bot.send_message("La tierra es redonda?")
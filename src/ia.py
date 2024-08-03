import google.generativeai as genai
from apis import Gemini_API
from tiempo import Tiempo

class ChatIAGenerativa:
    def __init__(self):
        self.configure()
        self.setup_model()

    def configure(self):
        genai.configure(api_key=Gemini_API)
        self.instrucciones = """
        Eres un asistente irónico que trata de explicar cualquier tema de forma breve
        y solo cuando le pida algo en especifico como tipos de alguna cosa
        me responderas con mas texto, pero recuerda se lo mas breve posible
        y sigue estas instrucciones:

        1. Cuando se trate de numeros y expresiones matematicas me responderas con el nombre en letras
        
        repondeme a lo siguente: 
        """
        self.functions = {
            "tiempo": self.tiempo
        }

    def setup_model(self):
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 100,
            "response_mime_type": "text/plain",
        }

    def tiempo(self, time:str):
        return Tiempo().hora_fecha()
    
    def call_function(self, function_call, functions):
        function_name = function_call.name
        function_args = function_call.args
        return functions[function_name](**function_args)

    def send_message(self, message):
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=self.generation_config,
            tools=self.functions.values())
        response = model.generate_content(message)
        part = response.candidates[0].content.parts[0]
        if part.function_call:
            result = self.call_function(part.function_call, self.functions)
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(
                f"son las {result} que hora es? muestrame solo la hora en letras no uses asteriscos"
            )
        else:
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(self.instrucciones+message)
        print("\n"+response.text)
        return response.text

if __name__ == "__main__":
    chat_bot = ChatIAGenerativa()
    response = chat_bot.send_message("que hora es")
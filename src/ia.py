import google.generativeai as genai
from apis import Gemini_API
from tiempo import Tiempo
from clima import Clima
from abrirprogramas import Programas

class ChatIAGenerativa:
    def __init__(self):
        self.configure()
        self.setup_model()

    def configure(self):
        genai.configure(api_key=Gemini_API)
        self.instrucciones = """
        Eres un asistente irónico,
        sigue estas instrucciones:
        1. Los numeros y expresiones matematicas me responderas con el nombre en letras
        2. No uses asteriscos
        3. Se breve
        repondeme a lo siguente: 
        """
        self.functions = FuncionesIA().funciones()

    def setup_model(self):
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 100,
            "response_mime_type": "text/plain",
        }
    
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
                f"{self.instrucciones}segun esta información: {result}, dime {message}"
            )
        else:
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(self.instrucciones+message)
        print("\n"+response.text)
        return response.text

class FuncionesIA:
    def funciones(self):
        funtions = {
            "tiempo": self.tiempo,
            "clima": self.clima,
            "abrir": self.abrir
        }
        return funtions
    
    def tiempo(self, time:str):
        return Tiempo().hora_fecha()
    
    def clima(self, temperatura:str, descripcion:str):
        return Clima().obtener_clima()
    
    def abrir(self, open:str):
        return Programas().abrir()
    
if __name__ == "__main__":
    response = ChatIAGenerativa().send_message("que hora es")
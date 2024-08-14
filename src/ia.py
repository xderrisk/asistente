import google.generativeai as genai
from apis import Gemini_API
from tiempo import Tiempo
from clima import Clima
from abrirprogramas import Programas
import platform

class ChatIAGenerativa:
    def __init__(self):
        self.configure()
        self.setup_model()

    def configure(self):
        genai.configure(api_key=Gemini_API)
        self.instrucciones = """
        Eres un asistente, sigue estas instrucciones:
        1. Los numeros y expresiones matematicas me responderas con el nombre en letras
        2. No uses asteriscos
        3. Se breve
        repondeme a lo siguente: 
        """
        self.functions = self.funciones()

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
        self.message = message
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=self.generation_config,
            tools=self.functions.values())
        response = model.generate_content(self.message)
        part = response.candidates[0].content.parts[0]
        print(part)
        if part.function_call:
            response = self.call_function(part.function_call, self.functions)
        else:
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(self.instrucciones+self.message)
            response = response.text
        print("\n"+response)
        return response

    def funciones(self):
        funtions = {
            "hora": self.hora,
            "clima": self.clima,
            "abrir": self.abrir
        }
        return funtions
    
    def hora(self, time:str):
        tiempo = Tiempo().hora_fecha()
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(f"""Dado la siguiente información sobre el tiempo actual: {tiempo}
                                          - respondeme {self.message}""")
        print(response)
        tiempo = response.text
        return tiempo
    
    def clima(self, ciudad:str, temperatura:str, descripcion:str):
        clima = Clima().obtener_clima()
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(f"""Dado la siguiente información sobre el clima:
                                          - lugar: {clima[0]}
                                          - temperatura: {clima[1]}°
                                          - descripción: {clima[2]}
                                          Dime el clima segun la info que te he ofrecido
                                          (dime el lugar, la temperatura y la descripción)""")
        print(response)
        clima = response.text
        return clima
    
    def abrir(self, open:str):
        version = platform.version()
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(f"""Dado el nombre de un programa como '{self.message}',
                                          responde con el nombre exacto del comando que se usa
                                          para abrir ese programa en la terminal de {version}
                                          (el texto debe estar en minusculas)""")
        print(response.text)
        programa = response.text.strip().lower()
        return Programas().abrir(programa)
    
if __name__ == "__main__":
    response = ChatIAGenerativa().send_message("que hora es")
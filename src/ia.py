import google.generativeai as genai
from tiempo import Tiempo
from clima import Clima
from programas import Programas
from web import Abrir
from musica import Reproducir
from rutas import ruta
import configparser
import platform
import distro

class ChatIAGenerativa:
    def __init__(self):
        self.configure()
        self.setup_model()

    def configure(self):
        try:
            config = configparser.ConfigParser()
            config.read(ruta('config.ini'))
            Gemini_API = config.get('API', 'geminiapikey')
            genai.configure(api_key=Gemini_API)
            self.instrucciones = """
            Eres un asistente ironico pero siempre da una respuesta correcta a todo de forma breve,
            repondeme a lo siguente: 
            """
            self.functions = self.funciones()
        except configparser.NoSectionError as e:
            print(f"Error en la configuración: No se pudo encontrar la sección en el archivo de configuración. {e}")
        except configparser.NoOptionError as e:
            print(f"Error en la configuración: No se encontró la opción 'geminiapikey'. {e}")
        except Exception as e:
            print(f"Error al configurar la API de Gemini: {e}")

    def setup_model(self):
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 25,
            "response_mime_type": "text/plain",
        }
    
    def call_function(self, function_call, functions):
        function_name = function_call.name
        function_args = function_call.args
        return functions[function_name](**function_args)

    def send_message(self, message):
        self.message = message
        try:
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
            response = response.replace("*", "").replace("\n", "")
            return response
        except Exception as e:
            error_message = str(e)
            if "API_KEY_INVALID" in error_message or "InvalidArgument" in error_message:
                return "Clave API no válida. Verifica tu configuración."
            print(f"Error al enviar el mensaje: {e}")
            return "Agregue su API en la Configuración"

    def funciones(self):
        funtions = {
            "hora": self.hora,
            "clima": self.clima,
            "abrir_programa": self.abrir_programa,
            "web" : self.web,
            "musica" : self.musica
        }
        return funtions
    
    def hora(self, time:str):
        tiempo = Tiempo().hora_fecha()
        try:
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(f"""Dado la siguiente información sobre el tiempo actual: {tiempo}
                                              - respondeme {self.message}(no me des informacion extra,
                                              si te pido la fecha escribelo en letras)""")
            print(response)
            tiempo = response.text
            return tiempo
        except Exception as e:
            print(f"Error al obtener la hora: {e}")
            return "Hubo un problema al obtener la hora."

    def clima(self, descripcion:str):
        clima = Clima().obtener_clima()
        try:
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(f"""Dado la siguiente información sobre el clima: {clima}
                                              comentame de forma resumida como esta el clima""")
            print(response)
            clima = response.text
            return clima
        except Exception as e:
            print(f"Error al obtener el clima: {e}")
            return "Hubo un problema al obtener el clima."

    def abrir_programa(self, open:str):
        sistema = platform.system()
        if sistema == "Linux":
            sabor = distro.name()
        else:
            sabor == platform.version()
        try:
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(f"""Dado el nombre de un programa como(ignora "abre"): '{self.message}',
                                              responde con el nombre exacto del comando que se usa
                                              para abrir ese programa en la terminal de {sistema} {sabor}
                                              (el texto debe estar en minusculas)""")
            print(response.text)
            programa = response.text.strip().lower()
            return Programas().abrir(programa)
        except Exception as e:
            print(f"Error al abrir el programa: {e}")
            return "Hubo un problema al abrir el programa."

    def web(self, open:str):
        try:
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(f"""Dame el link oficial de(ignora "abre la pagina de"): '{self.message}',
                                              respondeme solo con el link exacto, si no existe avisame""")
            print(response.text)
            url = response.text.strip().lower()
            return Abrir().web(url)
        except Exception as e:
            print(f"Error al abrir la página web: {e}")
            return "Hubo un problema al abrir la página web."

    def musica(self, open:str):
        try:
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(f"""Dada la siguiente instruccion que cancion quiero
                                              reproducir: '{self.message}', respondeme solo con el
                                              nombre de la canción""")
            print(response.text)
            cancion = response.text.strip().lower()
            return Reproducir().youtube_music(cancion)
        except Exception as e:
            print(f"Error al reproducir música: {e}")
            return "Hubo un problema al reproducir la música."

if __name__ == "__main__":
    respuesta = ChatIAGenerativa().send_message("clima de hoy")
    print(respuesta)

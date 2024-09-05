import webbrowser
import requests

class Abrir:
    def web(self, url):
        try:
            # Agrega un tiempo de espera de 5 segundos
            response = requests.get(url, timeout=5)
            # Verifica si la respuesta tiene un código de estado 200
            if response.status_code == 200:
                webbrowser.open(url)
                return "Abriendo la página"
            else:
                return "La página no existe"
        except requests.exceptions.Timeout:
            return "El servidor tardó demasiado en responder"
        except requests.exceptions.RequestException as e:
            # Captura errores como la imposibilidad de conectar, URL incorrecta, etc.
            return "Error al intentar acceder a la página"

if __name__ == "__main__":
    # URL de la página web que deseas abrir
    url = 'https://www.facebook.com'
    resultado = Abrir().web(url)
    print(resultado)

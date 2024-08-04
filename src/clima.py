import requests
from apis import Weather_API
class Clima:
    def __init__(self):
        self.obtener_clima

    def obtener_clima(self):
        clave_api = Weather_API
        ciudad = 'Jipijapa'
        pais = "EC"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={clave_api}&lang=es&units=metric"
        respuesta = requests.get(url)
        datos = respuesta.json()
        print(datos)
        if respuesta.status_code == 200:
            descripcion = datos['weather'][0]['description']
            temperatura = datos['main']['temp']
            humedad = datos['main']['humidity']
            viento = datos['wind']['speed']

            print(f"Clima en {ciudad}:")
            print(f"Descripción: {descripcion}")
            print(f"Temperatura: {temperatura}°C")
            print(f"Humedad: {humedad}%")
            print(f"Velocidad del viento: {viento} m/s")
        else:
            print(f"No se pudo obtener el clima de {ciudad}. Error: {datos['message']}")

        return descripcion, temperatura

if __name__ == "__main__":

    Clima().obtener_clima()

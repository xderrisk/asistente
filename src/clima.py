import requests
from src.apis import Weather_API

def obtener_clima(ciudad, pais, clave_api):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={clave_api}&lang=es&units=metric"
    respuesta = requests.get(url)
    datos = respuesta.json()

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

clave_api = Weather_API
ciudad = 'Jipijapa'
pais = "EC"

obtener_clima(ciudad, pais, clave_api)

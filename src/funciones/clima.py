import requests
import configparser
from bs4 import BeautifulSoup
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rutas import ruta

class Clima:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(ruta('config.ini'))
        self.ubicacion = self.config.get('DATA', 'ubicacion', fallback='')
        self.url = f"https://www.google.com/search?q=clima+{self.ubicacion}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        self.obtener_clima()
    
    def obtener_clima(self):
        # Hacer una solicitud a la URL
        response = requests.get(self.url, headers=self.headers)
        
        if response.status_code == 200:
            # Analizar el contenido HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Buscar el elemento que contiene la temperatura
            temp_elem = soup.find('span', {'class': 'wob_t', 'id': 'wob_tm'})
            # Buscar el elemento que contiene la descripción del clima
            desc_elem = soup.find('span', {'id': 'wob_dc'})
            
            if temp_elem and desc_elem:
                temperatura = temp_elem.text
                descripcion = desc_elem.text
                return f"El clima en {self.ubicacion} es {descripcion} con una temperatura de {temperatura}°C."
            else:
                return "No se pudo obtener la información del clima."
        else:
            return "Error al hacer la solicitud."

if __name__ == "__main__":
    clima = Clima().obtener_clima()
    print(clima)

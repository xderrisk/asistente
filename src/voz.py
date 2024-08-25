from playsound import playsound
from rutas import ruta
from gtts import gTTS
import platform
import os

class TextoAVoz:
    def __init__(self, texto):
        texto = texto
        tts = gTTS(text=texto, lang='es')
        ruta_voz = ruta('media/voz.mp3')
        tts.save(ruta_voz)

        sistema = platform.system()

        if sistema == "Windows":
            # Reproducir el archivo de audio en Windows
            playsound(ruta_voz)
        elif sistema == "Linux":
            # Reproducir el archivo de audio en Linux
            os.system(f"mpg321 {ruta_voz}")
        else:
            print("Sistema operativo no soportado.")

if __name__ == "__main__":
    texto = "Prueba"
    TextoAVoz(texto)
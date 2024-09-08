from playsound import playsound
from rutas import ruta
from gtts import gTTS
import os

class TextoAVoz:
    def __init__(self, texto):
        texto = texto
        tts = gTTS(text=texto, lang='es')
        ruta_voz = ruta('media/voz.mp3')
        tts.save(ruta_voz)
        playsound(ruta_voz)
        os.remove(ruta_voz)

if __name__ == "__main__":
    texto = "Prueba"
    TextoAVoz(texto)
from gtts import gTTS
import platform
import os

class TextoAVoz:
    def __init__(self, texto):
        texto = texto
        tts = gTTS(text=texto, lang='es')
        directorio_madre = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_media = os.path.join(directorio_madre, 'media')
        ruta_voz = os.path.join(ruta_media, 'voz.mp3')
        tts.save(ruta_voz)

        sistema = platform.system()

        if sistema == "Windows":
            # Reproducir el archivo de audio en Windows
            os.system(f"start {ruta_voz}")
        elif sistema == "Darwin":
            # Reproducir el archivo de audio en MacOS
            os.system(f"afplay {ruta_voz}")
        elif sistema == "Linux":
            # Reproducir el archivo de audio en Linux
            os.system(f"mpg321 {ruta_voz}")
            # o usa ffplay si no tienes mpg321
            # os.system("ffplay -nodisp -autoexit ejemplo.mp3")
        else:
            print("Sistema operativo no soportado.")

if __name__ == "__main__":
    texto = "Prueba"
    TextoAVoz(texto)

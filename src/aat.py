import speech_recognition as sr
import os

class AudioATexto:
    def __init__(self):
        self.directorio_madre = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ruta_media = os.path.join(self.directorio_madre, 'media')
        self.audio_file = os.path.join(self.ruta_media, 'grabacion.wav')
        self.recognizer = sr.Recognizer()

    def convertir(self):
        with sr.AudioFile(self.audio_file) as source:
            audio = self.recognizer.record(source)

        try:
            text = self.recognizer.recognize_google(audio, language="es-ES")
            print(text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition no pudo entender el audio")
        except sr.RequestError as e:
            print(f"No se pudo conectar con el servicio de Google Speech Recognition; {e}")

if __name__ == "__main__":
    audio_a_text = AudioATexto()
    audio_a_text.convertir()

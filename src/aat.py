import speech_recognition as sr

class AudioATexto:
    def __init__(self, audio_file):
        self.audio_file = audio_file
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
    audio_a_text = AudioATexto("grabacion.wav")
    audio_a_text.convertir()

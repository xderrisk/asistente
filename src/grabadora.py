from rutas import ruta
from playsound import playsound
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import threading
import wavio
import time
import os

class GrabadoraVoz:
    def __init__(self):
        self.frecuencia_muestreo = 44100
        self.canales = 2
        self.nombre_archivo = ruta('media/grabacion.wav')
        self.frames = []
        self.grabando = False
        self.ultimo_sonido = time.time()
        self.tiempo_silencio = 3  # Tiempo máximo de silencio en segundos

        self.iniciar_grabacion()
        time.sleep(self.tiempo_silencio + 1)  # Espera un poco más después de la grabación para asegurar el final

        self.detener_grabacion()
        print("Grabación guardada en", self.nombre_archivo)
        self.texto = self.convertir()

        os.remove(self.nombre_archivo)

        playsound(ruta('media/stop.mp3'))

    def iniciar_grabacion(self):
        self.frames = []
        self.grabando = True
        self.ultimo_sonido = time.time()
        self.hilo_grabacion = threading.Thread(target=self.grabar)
        self.hilo_grabacion.start()
        print("Grabando...")
        playsound(ruta('media/run.mp3'))

    def grabar(self):
        self.stream = sd.InputStream(samplerate=self.frecuencia_muestreo, channels=self.canales, callback=self.callback)
        with self.stream:
            while self.grabando:
                if time.time() - self.ultimo_sonido > self.tiempo_silencio:
                    self.detener_grabacion()
                sd.sleep(100)

    def callback(self, indata, frames, time_info, status):
        volumen = np.linalg.norm(indata)  # Calcular el volumen del audio
        if volumen > 5.01:  # Umbral para considerar sonido (ajusta según sea necesario)
            self.ultimo_sonido = time.time()
        self.frames.append(indata.copy())

    def detener_grabacion(self):
        if self.grabando:
            self.grabando = False
            self.stream.stop()
            self.stream.close()

            if self.frames:  # Verificar que self.frames no esté vacío
                audio_data = np.concatenate(self.frames, axis=0)

                # Normalizar el audio para evitar clipping
                max_valor = np.max(np.abs(audio_data))
                if max_valor > 1.0:
                    audio_data = audio_data / max_valor

                wavio.write(self.nombre_archivo, audio_data, self.frecuencia_muestreo, sampwidth=2)
            else:
                print("No se grabó ningún sonido.")

    def convertir(self):
        self.audio_file = ruta('media/grabacion.wav')
        self.recognizer = sr.Recognizer()
        with sr.AudioFile(self.audio_file) as source:
            audio = self.recognizer.record(source)

        try:
            text = self.recognizer.recognize_google(audio, language="es-ES")
            return text
        except sr.UnknownValueError:
            text = "No se pudo entender el audio"
            return text
        except sr.RequestError as e:
            text = "No se pudo conectar con el servicio"
            return text

if __name__ == "__main__":
    grabacion = GrabadoraVoz()
    print(grabacion.texto)
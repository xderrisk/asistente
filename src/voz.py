from elevenlabs.client import ElevenLabs
from src.apis import ElevenLabs_API
from elevenlabs import play

class Respuesta:
    def __init__(self, texto):
        self.texto = texto
        self.configure()
        self.voz()

    def configure(self):
        self.client = ElevenLabs(api_key=ElevenLabs_API)

    def voz(self):
        audio = self.client.generate(
            text = self.texto,
            voice = "erKgR0s8Y67t4iiHuA9R"
        )
        play(audio)

if __name__ == "__main__":
    texto = "Prueba"
    Respuesta(texto)
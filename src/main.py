from grabadora import GrabadoraVoz
from aat import AudioATexto
from ia import ChatIAGenerativa
from voz import Respuesta

if __name__ == "__main__":

    # grabacion de voz
    grabadora = GrabadoraVoz()

    # voz a texto
    audio = AudioATexto("media/grabacion.wav")
    texto = audio.convertir()

    # chat ia de google
    chat = ChatIAGenerativa()
    respuesta = chat.send_message(texto)

    # texto a voz
    voz = Respuesta(respuesta)
from grabadora import GrabadoraVoz
from aat import AudioATexto
from ia import ChatIAGenerativa
from voz import TextoAVoz

if __name__ == "__main__":

    # grabacion de voz
    grabadora = GrabadoraVoz()

    # voz a texto
    audio = AudioATexto()
    texto = audio.convertir()

    # chat ia de google
    chat = ChatIAGenerativa()
    respuesta = chat.send_message(texto)

    # texto a voz
    voz = TextoAVoz(respuesta)

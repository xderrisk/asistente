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

    if texto != "No se pudo entender el audio" and "No se pudo conectar con el servicio":
        # chat ia de google
        chat = ChatIAGenerativa()
        respuesta = chat.send_message(texto)

        # texto a voz
        voz = TextoAVoz(respuesta)

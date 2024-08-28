from grabadora import GrabadoraVoz
from ia import ChatIAGenerativa
from voz import TextoAVoz

def asistente():

    texto = GrabadoraVoz().texto
    print(f"Texto capturado: {texto}")

    if texto != "No se pudo entender el audio" and texto != "No se pudo conectar con el servicio":

        respuesta = ChatIAGenerativa().send_message(texto)
        print(f"Respuesta de IA: {respuesta}")

        TextoAVoz(respuesta)
    else:
        print(f"Error: {texto}")
        TextoAVoz(texto)

if __name__ == "__main__":
    asistente()
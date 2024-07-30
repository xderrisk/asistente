from datetime import datetime
class Tiempo:
    def __init__(self):
        self.hora()

    def hora(self):
        ahora = datetime.now()
        fecha_hora_formateada = ahora.strftime("son las %H y %M")
        print("Fecha y hora actuales:", fecha_hora_formateada)
        return fecha_hora_formateada

if __name__ == "__main__":
    Tiempo()
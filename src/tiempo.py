from datetime import datetime
class Tiempo:
    def __init__(self):
        self.hora_fecha()

    def hora_fecha(self):
        ahora = datetime.now()
        tiempo = ahora.strftime("%Y-%m-%d %H:%M:%S")
        print(tiempo)
        return tiempo

if __name__ == "__main__":
    Tiempo()
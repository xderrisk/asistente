from datetime import datetime
class Tiempo:
    def __init__(self):
        self.hora_fecha()

    def hora_fecha(self):
        ahora = datetime.now()
        tiempo = ahora.strftime("%Y-%m-%d %H:%M:%S")
        return tiempo

if __name__ == "__main__":
    time = Tiempo().hora_fecha()
    print(time)
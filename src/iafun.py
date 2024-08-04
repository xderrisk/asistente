from tiempo import Tiempo
from clima import Clima

class Funciones:
    def funciones(self):
        functions = {
            "tiempo": self.tiempo,
            "clima": self.clima
        }
        return functions

    def tiempo(self, time:str):
        return Tiempo().hora_fecha()
    
    def clima(self, temperatura:str, descripcion:str):
        return Clima().obtener_clima()
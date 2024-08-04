from tiempo import Tiempo
from clima import Clima
from abrirprogramas import Programas

class Funciones:
    def funciones(self):
        functions = {
            "tiempo": self.tiempo,
            "clima": self.clima,
            "abrir": self.abrir
        }
        return functions

    def tiempo(self, time:str):
        return Tiempo().hora_fecha()
    
    def clima(self, temperatura:str, descripcion:str):
        return Clima().obtener_clima()
    
    def abrir(self, open:str):
        return Programas().abrir()
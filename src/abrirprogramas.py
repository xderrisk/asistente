import subprocess
class Programas:
    def abrir(self, programa):
        try:
            subprocess.run([programa])
            return f"abriendo {programa}"
        except FileNotFoundError:
            return f"El programa {programa} no se encontró."

if __name__ == "__main__":
    programa = "firefox"
    abrir = Programas().abrir(programa)
    print(abrir)
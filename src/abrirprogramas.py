import subprocess
class Programas:
    def __init__(self) -> None:
        pass
    def abrir(self):
        subprocess.run([programa])

if __name__ == "__main__":
    programa = "gnome-terminal"
    Programas.abrir(programa)
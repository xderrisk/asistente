import subprocess
class Programas:
    def abrir(self, programa):
        subprocess.run([programa])
        abriendo = f"abriendo {programa}"
        return abriendo

if __name__ == "__main__":
    programa = "gnome-terminal"
    Programas().abrir(programa)
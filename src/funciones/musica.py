import pywhatkit as kit

class Reproducir():
    # Función para reproducir una canción en YouTube Music
    def youtube_music(self, cancion):
        # Buscar y reproducir la canción en YouTube
        kit.playonyt(cancion)
        abriendo = "Ok, reproduciendo"
        return abriendo

if __name__ == "__main__":
    cancion = "I Gotta Feeling"
    Reproducir().youtube_music(cancion)

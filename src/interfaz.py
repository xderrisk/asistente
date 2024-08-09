import tkinter as tk
from PIL import Image, ImageTk
from grabadora import GrabadoraVoz
from aat import AudioATexto
from ia import ChatIAGenerativa
from voz import TextoAVoz
import threading
import os

def ejecutar_proceso():
    def proceso_largo():
        # grabacion de voz
        grabadora = GrabadoraVoz()

        # voz a texto
        audio = AudioATexto()
        texto = audio.convertir()

        # Usar el método after para actualizar la interfaz en el hilo principal
        root.after(0, lambda: mensaje.config(text=texto))

        # chat ia de google
        chat = ChatIAGenerativa()
        respuesta = chat.send_message(texto)

        # Actualizar la interfaz de usuario en el hilo principal
        root.after(0, lambda: mensaje.config(text=respuesta))

        # texto a voz
        voz = TextoAVoz(respuesta)

    # Ejecutar el proceso largo en un hilo separado
    threading.Thread(target=proceso_largo, daemon=True).start()

# Crear la ventana principal
root = tk.Tk()
root.title("Botón con Imagen")
root.geometry("300x200")
root.resizable(False, False)  # Evitar que la ventana se pueda redimensionar

# Cargar la imagen con Pillow
directorio_madre = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ruta_media = os.path.join(directorio_madre, 'media', 'microfono.jpg')
imagen = Image.open(ruta_media)
imagen = imagen.resize((50, 50), Image.Resampling.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un botón con imagen
boton = tk.Button(root, image=imagen_tk, command=ejecutar_proceso)
boton.pack(pady=20)

# Crear una etiqueta para mostrar el mensaje
mensaje = tk.Label(root, text="")
mensaje.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()

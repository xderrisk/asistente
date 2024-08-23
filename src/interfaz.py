from grabadora import GrabadoraVoz
from aat import AudioATexto
from ia import ChatIAGenerativa
from voz import TextoAVoz
import tkinter as tk
import threading
import os

def asistente():
    def proceso():
        # grabacion de voz
        texto = "Grabando..."
        root.after(0, lambda: mensaje.config(text=texto))
        grabadora = GrabadoraVoz()

        # voz a texto
        texto = AudioATexto().convertir()

        # Usar el método after para actualizar la interfaz en el hilo principal
        root.after(0, lambda: mensaje.config(text=texto))

        if texto != "No se pudo entender el audio" and "No se pudo conectar con el servicio":
            # chat ia de google
            respuesta = ChatIAGenerativa().send_message(texto)

            # Actualizar la interfaz de usuario en el hilo principal
            root.after(0, lambda: mensaje.config(text=respuesta))

            # texto a voz
            voz = TextoAVoz(respuesta)

    # Ejecutar el proceso largo en un hilo separado
    threading.Thread(target=proceso, daemon=True).start()

# Crear la ventana principal
root = tk.Tk()
root.title("Asistente")
icono = tk.PhotoImage(file='media/bot.png')
root.iconphoto(False, icono)
root.geometry("500x150")
root.configure(bg='#383838')
root.resizable(False, False)

# Cargar la imagen en formato
directorio_madre = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ruta_media = os.path.join(directorio_madre, 'media')
ruta_imagen = os.path.join(ruta_media, 'microfono.png')
imagen = tk.PhotoImage(file=ruta_imagen)
imagen = imagen.subsample(7, 7)

# Crear un widget de etiqueta para mostrar la imagen
etiqueta_imagen = tk.Button(root, image=imagen, relief='flat', command=asistente, bg='#383838')
etiqueta_imagen.place(relx=0.02, rely=0.5, anchor=tk.W)

# Crear una etiqueta para mostrar el mensaje
mensaje = tk.Label(root, text="",  font=("Arial", 20), wraplength=300, fg='white', bg='#383838')
mensaje.pack(side=tk.RIGHT, padx=10)

# Ejecutar el bucle principal de Tkinter
root.mainloop()

from grabadora import GrabadoraVoz
from ia import ChatIAGenerativa
from voz import TextoAVoz
from rutas import ruta
import tkinter as tk
import threading

def asistente():
    def proceso():
        # grabacion de voz
        texto = "Grabando..."
        root.after(0, lambda: mostrar_texto(texto, mensaje))

        # graba la voz y la convierte a texto
        texto = GrabadoraVoz().texto

        # Usar el método after para actualizar la interfaz en el hilo principal
        root.after(0, lambda: mostrar_texto(texto, mensaje))

        if texto != "No se pudo entender el audio" and texto != "No se pudo conectar con el servicio":
            # chat ia de google
            respuesta = ChatIAGenerativa().send_message(texto)

            # Actualizar la interfaz de usuario en el hilo principal
            root.after(0, lambda: mostrar_texto(respuesta, mensaje))

            # texto a voz
            voz = TextoAVoz(respuesta)
        else:
            voz = TextoAVoz(texto)

    # Ejecutar el proceso largo en un hilo separado
    threading.Thread(target=proceso, daemon=True).start()

def mostrar_texto(texto, widget, velocidad=50):
    widget.config(text="")  # Limpiar el texto anterior
    def generador_de_texto(indice=0):
        if indice < len(texto):
            widget.config(text=widget.cget("text") + texto[indice])
            widget.after(velocidad, generador_de_texto, indice+1)
    generador_de_texto()

# Crear la ventana principal
root = tk.Tk()
root.title("Asistente")
ruta_imagen = ruta('media/bot.png')
icono = tk.PhotoImage(file=ruta_imagen)
root.iconphoto(False, icono)
root.geometry("500x150")
root.configure(bg='#383838')
root.resizable(False, False)

# Cargar la imagen en formato
ruta_imagen = ruta('media/microfono.png')
imagen = tk.PhotoImage(file=ruta_imagen)
imagen = imagen.subsample(7, 7)

# Crear un widget de etiqueta para mostrar la imagen
etiqueta_imagen = tk.Button(root, image=imagen, relief='flat', command=asistente, bg='#383838')
etiqueta_imagen.place(relx=0.02, rely=0.5, anchor=tk.W)

# Crear una etiqueta para mostrar el mensaje
mensaje = tk.Label(root, text="",  font=("Arial", 15), wraplength=300, fg='white', bg='#383838')
mensaje.pack(side=tk.RIGHT, padx=10)

# Ejecutar el bucle principal de Tkinter
root.mainloop()
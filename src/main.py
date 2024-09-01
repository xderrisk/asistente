from grabadora import GrabadoraVoz
from ia import ChatIAGenerativa
from voz import TextoAVoz
from rutas import ruta
import tkinter as tk
import configparser
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

def mostrar_frame(frame_a_mostrar):
    # Oculta todos los frames
    for frame in [main_frame, config_frame]:
        frame.pack_forget()
    
    # Muestra el frame seleccionado
    frame_a_mostrar.pack(fill=tk.BOTH, expand=True)

def abrir_inicio():
    mostrar_frame(main_frame)

def abrir_configuracion():
    mostrar_frame(config_frame)
    if not text_gemini.get().strip():
        config = configparser.ConfigParser()
        config.read(ruta('config.ini'))
        gemini_api_key = config.get('API', 'geminiapikey', fallback='')
        if gemini_api_key:
            text_gemini.insert(tk.END, gemini_api_key)

def guardar_configuracion():

    nuevo_gemini_api_key = text_gemini.get().strip()  # Obtener todo el texto y eliminar espacios en blanco

    # Leer el archivo de configuración actual
    config = configparser.ConfigParser()
    config.read(ruta('config.ini'))
    
    # Actualizar la clave geminiapikey con el nuevo valor
    if 'API' not in config:
        config.add_section('API')
    config.set('API', 'geminiapikey', nuevo_gemini_api_key)
    
    # Guardar los cambios en el archivo de configuración
    with open(ruta('config.ini'), 'w') as configfile:
        config.write(configfile)

# Crear la ventana principal
root = tk.Tk()
root.title("Asistente")
ruta_imagen = ruta('media/bot.png')
icono = tk.PhotoImage(file=ruta_imagen)
root.iconphoto(False, icono)
root.geometry("500x150")
root.configure(bg='#383838')
root.resizable(False, False)

# Crear el menú principal
menubar = tk.Menu(root, bg='#565656', fg='white', activebackground='#4E4E4E', activeforeground='white')
config_menu = tk.Menu(menubar, tearoff=0)
menubar.add_command(label="Inicio", command=abrir_inicio)
menubar.add_command(label="Opciones", command=abrir_configuracion)
root.config(menu=menubar)

# pantalla de inicio
main_frame = tk.Frame(root, bg='#383838')
ruta_imagen = ruta('media/microfono.png')
imagen = tk.PhotoImage(file=ruta_imagen)
imagen = imagen.subsample(7, 7)

# Crear un widget de etiqueta para mostrar la imagen
microfono = tk.Button(main_frame, image=imagen, relief='flat', command=asistente, bg='#383838')
microfono.place(relx=0.02, rely=0.5, anchor=tk.W)
root.bind("<space>", lambda event: microfono.invoke())

# Crear una etiqueta para mostrar el mensaje
mensaje = tk.Label(main_frame, text="",  font=("Arial", 15), wraplength=300, fg='white', bg='#383838')
mensaje.pack(side=tk.RIGHT, padx=10)


# pantalla de configuracion
config_frame = tk.Frame(root, bg='#383838')
label_gemini = tk.Label(config_frame, text="Ingrese su API de Gemini:")
label_gemini.pack(pady=5)
text_gemini = tk.Entry(config_frame, width=40)
text_gemini.pack(pady=5)
guardar_btn = tk.Button(config_frame, text="Guardar", command=guardar_configuracion, bg='#565656', fg='white')
guardar_btn.pack(pady=10)

mostrar_frame(main_frame)

# Ejecutar el bucle principal de Tkinter
root.mainloop()
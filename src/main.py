import tkinter as tk
import configparser
import threading
from grabadora import GrabadoraVoz
from ia import ChatIAGenerativa
from voz import TextoAVoz
from rutas import ruta

class AsistenteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Asistente")
        self.root.geometry("500x150")
        self.root.configure(bg='#383838')
        self.root.resizable(False, False)

        self.bienvenida_frame = None
        self.main_frame = None
        self.config_frame = None

        self.config = configparser.ConfigParser()
        self.config.read(ruta('config.ini'))

        ruta_imagen = ruta('media/bot.png')
        icono = tk.PhotoImage(file=ruta_imagen)
        self.root.iconphoto(False, icono)

        self.crear_menu()

        # Determinar la pantalla inicial
        if 'API' not in self.config:
            self.abrir_bienvenida()
        else:
            self.abrir_inicio()

        # Bind para la tecla espacio
        self.root.bind("<space>", self.manejar_espacio)

    def crear_menu(self):
        menubar = tk.Menu(self.root, bg='#565656', fg='white', activebackground='#4E4E4E', activeforeground='white')
        menubar.add_command(label="Inicio", command=self.abrir_inicio)
        menubar.add_command(label="Opciones", command=self.abrir_configuracion)
        self.root.config(menu=menubar)

    def mostrar_frame(self, frame_a_mostrar):
        for frame in [self.bienvenida_frame, self.main_frame, self.config_frame]:
            if frame:
                frame.pack_forget()
        frame_a_mostrar.pack(fill=tk.BOTH, expand=True)

    def abrir_bienvenida(self):
        if not self.bienvenida_frame:
            self.bienvenida_frame = tk.Frame(self.root, bg='#383838')

            self.label = tk.Label(self.bienvenida_frame, text="¡Bienvenido!", font=("Helvetica", 16), fg='white', bg='#383838')
            self.label.pack(pady=5)

            self.label = tk.Label(self.bienvenida_frame, text="Ingresa tu API de Gemini", font=("Helvetica", 16), fg='white', bg='#383838')
            self.label.pack(pady=5)

            self.text_gemini = tk.Entry(self.bienvenida_frame, width=50)
            self.text_gemini.pack(pady=5)
            
            self.button = tk.Button(self.bienvenida_frame, text="Guardar", command=self.finalizar_bienvenida, bg='#565656', fg='white', state=tk.DISABLED)
            self.button.pack(pady=10)

            self.text_gemini.bind("<KeyRelease>", self.verificar_entrada)

            self.bienvenida_frame.pack(fill=tk.BOTH, expand=True)

        self.mostrar_frame(self.bienvenida_frame)

    def verificar_entrada(self, *args):
        if self.text_gemini.get().strip() or self.text_ubicacion.get().strip():
            self.button.config(state=tk.NORMAL)
        else:
            self.button.config(state=tk.DISABLED)

    def finalizar_bienvenida(self):
        self.guardar_configuracion()
        self.abrir_inicio()

    def abrir_inicio(self):
        if not self.main_frame:
            self.main_frame = tk.Frame(self.root, bg='#383838')

            ruta_imagen = ruta('media/microfono.png')
            imagen = tk.PhotoImage(file=ruta_imagen)
            imagen = imagen.subsample(7, 7)

            self.microfono = tk.Button(self.main_frame, image=imagen, relief='flat', command=self.asistente, bg='#383838')
            self.microfono.image = imagen  # Necesario para evitar que la imagen sea recolectada por el GC
            self.microfono.place(relx=0.02, rely=0.5, anchor=tk.W)

            self.mensaje = tk.Label(self.main_frame, text="", font=("Arial", 15), wraplength=300, fg='white', bg='#383838')
            self.mensaje.pack(side=tk.RIGHT, padx=10)

        self.mostrar_frame(self.main_frame)

    def manejar_espacio(self, event):
        if self.main_frame and self.main_frame.winfo_ismapped():
            self.microfono.invoke()

    def asistente(self):
        threading.Thread(target=self.proceso, daemon=True).start()

    def proceso(self):
        # grabacion de voz
        texto = "Grabando..."
        self.root.after(0, lambda: self.mostrar_texto(texto, self.mensaje))

        # graba la voz y la convierte a texto
        texto = GrabadoraVoz().texto

        self.root.after(0, lambda: self.mostrar_texto(texto, self.mensaje))

        if texto not in ["No se pudo entender el audio", "No se pudo conectar con el servicio"]:
            # chat ia de google
            respuesta = ChatIAGenerativa().send_message(texto)

            self.root.after(0, lambda: self.mostrar_texto(respuesta, self.mensaje))

            # texto a voz
            TextoAVoz(respuesta)
        else:
            TextoAVoz(texto)

    def mostrar_texto(self, texto, widget, velocidad=50):
        widget.config(text="")  # Limpiar el texto anterior

        def generador_de_texto(indice=0):
            if indice < len(texto):
                widget.config(text=widget.cget("text") + texto[indice])
                widget.after(velocidad, generador_de_texto, indice + 1)

        generador_de_texto()

    def abrir_configuracion(self):
        if not self.config_frame:
            self.config_frame = tk.Frame(self.root, bg='#383838')
            
            label_gemini = tk.Label(self.config_frame, text="Ingrese su API de Gemini:")
            label_gemini.pack(pady=3)

            self.text_gemini = tk.Entry(self.config_frame, width=50)
            self.text_gemini.pack(pady=3)

            label_ubicacion = tk.Label(self.config_frame, text="Ingrese su ubicación:")
            label_ubicacion.pack(pady=3)

            self.text_ubicacion = tk.Entry(self.config_frame, width=50)
            self.text_ubicacion.pack(pady=3)

            self.button = tk.Button(self.config_frame, text="Guardar", command=self.guardar_configuracion, bg='#565656', fg='white', state=tk.DISABLED)
            self.button.pack(pady=3)

            self.text_gemini.bind("<KeyRelease>", self.verificar_entrada)
            self.text_ubicacion.bind("<KeyRelease>", self.verificar_entrada)

        self.mostrar_frame(self.config_frame)

        if not self.text_gemini.get().strip():
            gem = self.config.get('API', 'geminiapikey', fallback='')
            if gem:
                self.text_gemini.insert(tk.END, gem)

        if not self.text_ubicacion.get().strip():
            ubi = self.config.get('DATA', 'ubicacion', fallback='')
            if ubi:
                self.text_ubicacion.insert(tk.END, ubi)

    def guardar_configuracion(self):
        nuevo_gemini = self.text_gemini.get().strip()
        nueva_ubicacion = self.text_ubicacion.get().strip()

        if 'API' not in self.config:
            self.config.add_section('API')
        self.config.set('API', 'geminiapikey', nuevo_gemini)
        if 'DATA' not in self.config:
            self.config.add_section('DATA')
        self.config.set('DATA', 'ubicacion', nueva_ubicacion)

        with open(ruta('config.ini'), 'w') as configfile:
            self.config.write(configfile)

        self.button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = AsistenteApp(root)
    root.mainloop()

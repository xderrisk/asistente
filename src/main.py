import tkinter as tk
import configparser
import webbrowser
import threading
from grabadora import GrabadoraVoz
from ia import ChatIAGenerativa
from voz import TextoAVoz
from rutas import ruta

class AsistenteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Asistente")
        self.root.geometry("500x200")
        self.root.configure(bg='#383838')
        self.root.resizable(False, False)

        self.bienvenida_frame = None
        self.main_frame = None
        self.config_frame = None
        self.help_frame = None
        self.about_frame = None

        self.config = configparser.ConfigParser()
        self.config.read(ruta('config.ini'))

        ruta_imagen = ruta('media/bot.png')
        icono = tk.PhotoImage(file=ruta_imagen)
        self.root.iconphoto(False, icono)


        ruta_imagen = ruta('media/microfono.png')
        imagen = tk.PhotoImage(file=ruta_imagen)
        self.imagen = imagen.subsample(7, 7)

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
        menubar.add_command(label="Ayuda", command=self.abrir_ayuda)
        menubar.add_command(label="Acerca", command=self.abrir_acerca)
        self.root.config(menu=menubar)

    def mostrar_frame(self, frame_a_mostrar):
        for frame in [self.bienvenida_frame,
                      self.main_frame,
                      self.config_frame,
                      self.help_frame,
                      self.about_frame]:
            if frame:
                frame.pack_forget()
        frame_a_mostrar.pack(fill=tk.BOTH, expand=True)

    def abrir_bienvenida(self):
        if not self.bienvenida_frame:
            from frames.bienvenida import crear_bienvenida_frame
            self.bienvenida_frame = crear_bienvenida_frame(self)
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
            from frames.inicio import crear_inicio_frame
            self.main_frame = crear_inicio_frame(self)
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
            from frames.configuracion import crear_config_frame
            self.config_frame = crear_config_frame(self)
        self.mostrar_frame(self.config_frame)

    def guardar_configuracion(self):
        from frames.configuracion import guardar_configuracion
        guardar_configuracion(self)

    def abrir_ayuda(self):
        if not self.help_frame:
            from frames.ayuda import crear_ayuda_frame
            self.help_frame = crear_ayuda_frame(self)
        self.mostrar_frame(self.help_frame)

    def web_api_gemini(self):
        webbrowser.open_new("https://aistudio.google.com/app/apikey")

    def abrir_acerca(self):
        if not self.about_frame:
            from frames.acerca import crear_acerca_frame
            self.about_frame = crear_acerca_frame(self)
        self.mostrar_frame(self.about_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = AsistenteApp(root)
    root.mainloop()

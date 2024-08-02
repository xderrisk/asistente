import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class AsistenteVirtualApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Asistente Virtual")

        # Configuración del tamaño de la ventana
        self.root.geometry("400x300")

        # Cuadro de texto para mostrar respuestas
        self.text_display = tk.Text(root, height=10, width=50, wrap='word')
        self.text_display.pack(pady=10)

        # Cargar imagen para el botón
        self.ruta_imagen = os.path.join('media', "microfono.jpg")
        self.image = Image.open(self.ruta_imagen)  # Reemplaza con la ruta a tu imagen
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_button = tk.Button(root, image=self.photo, command=self.on_image_button_click)
        self.image_button.pack(pady=10)

        # Botón de configuración
        self.config_button = tk.Button(root, text="Configuración", command=self.open_config_dialog)
        self.config_button.pack(pady=10)

    def on_image_button_click(self):
        # Aquí puedes agregar el código para manejar el clic en el botón de imagen
        self.text_display.insert(tk.END, "¡Botón de imagen clickeado!\n")

    def open_config_dialog(self):
        # Aquí puedes agregar el código para abrir el diálogo de configuración
        messagebox.showinfo("Configuración", "Aquí puedes configurar el asistente virtual.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AsistenteVirtualApp(root)
    root.mainloop()
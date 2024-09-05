import tkinter as tk

def crear_acerca_frame(app):
    frame = tk.Frame(app.root, bg='#383838')

    label = tk.Label(frame, text="Acerca del Asistente", font=("Helvetica", 16), fg='white', bg='#383838')
    label.pack(pady=10)

    texto_acerca = tk.Label(frame, text="Este asistente ha sido desarrollado por [Tu Nombre].", fg='white', bg='#383838', wraplength=400)
    texto_acerca.pack(pady=10)

    return frame

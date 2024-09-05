import tkinter as tk

def crear_ayuda_frame(app):
    frame = tk.Frame(app.root, bg='#383838')

    label = tk.Label(frame, text="Ayuda", font=("Helvetica", 16), fg='white', bg='#383838')
    label.pack(pady=10)

    texto_ayuda = tk.Label(frame, text="Aquí puedes incluir la información de ayuda para el asistente.", fg='white', bg='#383838', wraplength=400)
    texto_ayuda.pack(pady=10)

    return frame

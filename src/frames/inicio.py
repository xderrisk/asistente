import tkinter as tk

def crear_inicio_frame(app):
    frame = tk.Frame(app.root, bg='#383838')

    microfono = tk.Button(frame,
                          image=app.imagen,
                          relief='flat',
                          command=app.asistente,
                          bg='#383838')
    microfono.image = app.imagen
    microfono.place(relx=0.02, rely=0.5, anchor=tk.W)

    mensaje = tk.Label(frame,
                       text="",
                       font=("Arial", 15), wraplength=300, fg='white', bg='#383838')
    mensaje.pack(side=tk.RIGHT, padx=10)

    app.microfono = microfono
    app.mensaje = mensaje

    return frame

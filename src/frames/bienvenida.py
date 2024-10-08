import tkinter as tk

def crear_bienvenida_frame(app):
    frame = tk.Frame(app.root, bg='#383838')

    tk.Label(frame,
             text="¡Bienvenido!",
             font=("bold"), fg='white', bg='#383838'
             ).pack(pady=5)

    tk.Label(frame,
             text="Ingresa tu API de Gemini",
             fg='white', bg='#383838').pack(pady=3)

    text_gemini = tk.Entry(frame, width=50)
    text_gemini.pack(pady=3)

    tk.Label(frame,
             text="Ingrese su ubicación actual",
             fg='white', bg='#383838').pack(pady=3)

    text_ubicacion = tk.Entry(frame, width=50)
    text_ubicacion.pack(pady=3)

    button = tk.Button(frame,
                       text="Guardar",
                       command=lambda: app.finalizar_bienvenida(),
                       bg='#565656', fg='white', state=tk.DISABLED)
    button.pack(pady=10)

    text_gemini.bind("<KeyRelease>", lambda event: app.verificar_entrada())
    text_ubicacion.bind("<KeyRelease>", lambda event: app.verificar_entrada())

    app.text_gemini = text_gemini
    app.text_ubicacion = text_ubicacion
    app.button = button

    return frame
    
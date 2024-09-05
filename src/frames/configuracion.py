import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rutas import ruta

def crear_config_frame(app):
    frame = tk.Frame(app.root, bg='#383838')

    label_gemini = tk.Label(frame, text="Ingrese su API de Gemini:", fg='white', bg='#383838')
    label_gemini.pack(pady=3)

    text_gemini = tk.Entry(frame, width=50, fg='white', bg='#383838')
    text_gemini.pack(pady=3)

    label_ubicacion = tk.Label(frame, text="Ingrese su ubicación:", fg='white', bg='#383838')
    label_ubicacion.pack(pady=3)

    text_ubicacion = tk.Entry(frame, width=50, fg='white', bg='#383838')
    text_ubicacion.pack(pady=3)

    button = tk.Button(frame, text="Guardar", command=lambda: app.guardar_configuracion(), bg='#565656', fg='white', state=tk.DISABLED)
    button.pack(pady=3)

    text_gemini.bind("<KeyRelease>", lambda event: app.verificar_entrada())
    text_ubicacion.bind("<KeyRelease>", lambda event: app.verificar_entrada())

    app.text_gemini = text_gemini
    app.text_ubicacion = text_ubicacion
    app.button = button

    if not app.text_gemini.get().strip():
        gem = app.config.get('API', 'geminiapikey', fallback='')
        if gem:
            app.text_gemini.insert(tk.END, gem)

    if not app.text_ubicacion.get().strip():
        ubi = app.config.get('DATA', 'ubicacion', fallback='')
        if ubi:
            app.text_ubicacion.insert(tk.END, ubi)

    return frame

def guardar_configuracion(app):

    app.config['API'] = {
        'geminiapikey': app.text_gemini.get().strip()  # Cambiado 'gemini' a 'geminiapikey'
    }

    app.config['DATA'] = {
        'ubicacion': app.text_ubicacion.get().strip()
    }

    with open(ruta('config.ini'), 'w') as configfile:
        app.config.write(configfile)
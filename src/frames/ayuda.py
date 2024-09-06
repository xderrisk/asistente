import tkinter as tk

def crear_ayuda_frame(app):
    frame = tk.Frame(app.root, bg='#383838')

    tk.Label(frame,
             text="Donde consigo la API de Gemini?",
             font=("bold"), fg='white', bg='#383838'
             ).pack(padx=10, pady=10, anchor='w')
    
    tk.Button(frame,
              text="Consigue tu api aquí",
              command=app.web_api_gemini
              ).pack(padx=10, pady=10, anchor='w')

    return frame

import tkinter as tk

def crear_acerca_frame(app):
    frame = tk.Frame(app.root, bg='#383838')

    tk.Label(frame,
             text="Asistente que usa la API de Gemini",
             font=("bold"), fg='white', bg='#383838'
             ).pack(padx=10, pady=10, anchor='w')

    tk.Label(frame,
             text="Este asistente ha sido desarrollado por Sergio Galarza.",
             fg='white', bg='#383838'
             ).pack(padx=10, pady=10, anchor='w')
    
    tk.Button(frame,
              text="Repositorio de GitHub",
              command=app.github_repo
              ).pack(padx=10, pady=10, anchor='w')

    return frame

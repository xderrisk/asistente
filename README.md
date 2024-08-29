## Asistente
Asistente virtual que funciona con la voz y que obedece a comandos
como decir la hora, dar información del clima, abrir páginas web,
abrir aplicaciones, dar respuesta a preguntas, reproducir música.

### APIs:
- Gemini
- OpenWeatherMap

### Bibliotecas PIP:
- tkinter
- google-generativeai
- speechrecognition
- gtts
- sounddevice
- wavio
- playsound
- pywhatkit
- distro
- pyinstaller

### Requerimientos en Linux:
- python3-venv
- python3-tk
- mpg321

### Requerimientos en Windows:
- Instalar Python

## Como usarlo?
Crea un entorno virtual Python en la carpeta raíz del proyecto
```bash
python3 -m venv .venv
```
Activa el entorno virtual Python
```bash
# en Linux
source .venv/bin/activate
```
```bash
# en Windows
.venv\Scripts\activate.bat
```
Instala los requerimientos pip
```bash
pip install -r requirements.txt
```
Crea un script llamado ```apis.py``` en la carpeta ```src``` y agrega tu api key de Gemini y OpenWeatherMap
```python
Gemini_API = ""
Weather_API = ""
```

## Como funciona?
1. El programa inicia en la carpeta ```src``` con el script [main.py](src/main.py) donde se muestra un botón de micrófono y un label para mostrar los resultados del asistente

2. Al tocar el micrófono se inicia [grabadora.py](src/grabadora.py) que guarda la grabación en la carpeta ```media``` y lo convierte a texto

3. Si se reconoce lo que dice el audio grabado se lleva el texto a [ia.py](src/ia.py) que usa la api de Gemini ubicada en ```src/apis.py```

4. Según lo solicitado gracias a las funciones de Gemini podrá [decir la hora y fecha actual](src/tiempo.py), [decir el clima](src/clima.py), [abrir programas](src/programas.py), [abrir paginas web](src/web.py), [reproducir música](src/musica.py) o simplemente responder a preguntas

5. Finalmente [voz.py](src/voz.py) se encarga de convertir la respuesta del asistente en voz

## Como creo el ejecutable?
Ejecuta este comando en tu entorno virtual Python
```bash
pyinstaller --onefile --windowed --icon=media/bot.png --name=asistente --add-data=media/bot.png:media --add-data=media/microfono.png:media --add-data=media/iniciar-grabacion.mp3:media --add-data=media/acabar-grabacion.mp3:media src/main.py
```

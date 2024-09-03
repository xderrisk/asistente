## Asistente
Asistente virtual que funciona con la voz y que obedece a comandos
como decir la hora, dar información del clima, abrir páginas web,
abrir aplicaciones, dar respuesta a preguntas, reproducir música.

### APIs:
- Gemini

### Bibliotecas PIP:
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

## Como funciona?
1. El programa inicia en la carpeta ```src``` con el script [main.py](src/main.py) donde deberá ingresar por primera vez su API de Gemini y su ubicación y guardar, en el inicio se muestra un botón de micrófono y un label para mostrar los resultados del asistente

2. Al tocar el micrófono se inicia [grabadora.py](src/grabadora.py) que guarda la grabación en la carpeta ```media``` y lo convierte a texto

3. Si se reconoce lo que dice el audio grabado se lleva el texto a [ia.py](src/ia.py) que usa la api de Gemini

4. Según lo solicitado gracias a las funciones de Gemini podrá [decir la hora y fecha actual](src/tiempo.py), [decir el clima](src/clima.py), [abrir programas](src/programas.py), [abrir paginas web](src/web.py), [reproducir música](src/musica.py) o simplemente responder a preguntas

5. Finalmente [voz.py](src/voz.py) se encarga de convertir la respuesta del asistente en voz

## Como creo el ejecutable?
Ejecuta este comando en tu entorno virtual Python
```bash
pyinstaller --windowed --icon=media/bot.png --name=asistente --add-data=media/bot.png:media --add-data=media/microfono.png:media --add-data=media/run.mp3:media --add-data=media/stop.mp3:media src/main.py
```
## Empaquetar a .deb
Mover el ejecutable
```bash
mv dist/asistente/asistente dist/asistente/_internal /deb/asistente/opt/asistente
```
Crear deb
```bash
dpkg-deb --build deb/asistente
```
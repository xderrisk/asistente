## Asistente
Asistente virtual que funciona con la voz y que obedece a comandos
como decir la hora, dar información del clima, abrir páginas web,
abrir aplicaciónes, dar respuesta a preguntas, reproducir música.

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

### Requerimientos en Linux:
- mpg321

Requerimientos en windows:
- aún no ha sido probado

## Como usarlo?
En el script ```src/apis.py``` agrega tu api key de Gemini y OpenWeatherMap

## Como funciona?
1. El programa inicia en la carpeta ```src``` con el script [interfaz.py](src/interfaz.py) donde se muestra un boton de microfono y un label para mostrar los resultados del asistente
2. Al tocar el microfono se inicia [grabadora.py](src/grabadora.py) que guarda la grabacion en la carpeta ```media```
3. Cuando termina la grabacion se inicia [aat.py](src/aat.py) que convierte el audio grabado a texto
4. Si se reconoce lo que dice el audio grabado se lleva el texto a [ia.py](src/ia.py)
5. Según lo solicitado gracias a las funciones de Gemini podra [decir la hora y fecha actual](src/tiempo.py), [decir el clima](src/clima.py), [abrir programas](src/abrirprogramas.py), [abrir paginas web](src), [reproducir música](src) o simplemente responder a la pregunta
6. Finalmente [voz.py](src/voz.py) se encarga de convertir la respuesta del asistente en voz

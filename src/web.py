import webbrowser

class abrir():    
    def web(self, url):
        webbrowser.open(url)
        abriendo = "abriendo la pagina"
        return abriendo

if __name__ == "__main__":
    # URL de la página web que deseas abrir
    url = 'https://www.example.com'
    abrir().web(url)
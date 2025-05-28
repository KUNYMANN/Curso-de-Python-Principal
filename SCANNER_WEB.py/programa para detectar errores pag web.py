import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import pdfkit

def analizar_html(url):
    errores = []
    soluciones = []
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')

        if soup.find_all('html') == []:
            errores.append("No se encontró la etiqueta <html>")
            soluciones.append("Agregar la etiqueta <html> para una estructura válida")

        if soup.find_all('title') == []:
            errores.append("No se encontró una etiqueta <title>")
            soluciones.append("Agregar un título a la página con <title>")

        if len(soup.find_all('img')) > 0:
            for img in soup.find_all('img'):
                if not img.get('alt'):
                    errores.append(f"Imagen sin atributo alt: {img.get('src')}")
                    soluciones.append("Agregar atributo alt a todas las imágenes")

    except Exception as e:
        errores.append(f"Error al obtener la página: {str(e)}")
        soluciones.append("Verificar la URL o la conexión")

    return errores, soluciones

def analizar_renderizado(url):
    errores = []
    soluciones = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        try:
            page.goto(url)
            # Esperamos a que cargue todo
            page.wait_for_load_state('networkidle')

            # Errores de consola JS
            console_logs = []

            def log_error(msg):
                if msg.type == "error":
                    console_logs.append(msg.text)

            page.on("console", log_error)

            page.reload()
            page.wait_for_timeout(3000)

            errores += [f"JS Error: {msg}" for msg in console_logs]
            soluciones += ["Revisar el código JS que causa errores en consola"]

            # Revisar recursos cargados (status 404 o 500)
            bad_responses = []
            def check_response(resp):
                if resp.status >= 400:
                    bad_responses.append(f"{resp.status} en {resp.url}")

            page.on("response", check_response)
            page.reload()
            page.wait_for_timeout(3000)

            errores += bad_responses
            soluciones += ["Verificar que todos los recursos estén disponibles (no 404/500)"]

        except Exception as e:
            errores.append(f"Error al renderizar página: {str(e)}")
            soluciones.append("Verificar errores de conexión o estructura del sitio")
        finally:
            browser.close()

    return errores, soluciones

def generar_reporte_pdf(url, errores, soluciones, nombre_archivo="reporte_errores.pdf"):
    contenido_html = f"""
    <html>
    <head><meta charset='utf-8'><style>
    body {{ font-family: Arial; }}
    h1 {{ color: #d9534f; }}
    h2 {{ color: #5bc0de; }}
    </style></head>
    <body>
        <h1>Reporte de errores - {url}</h1>
        <h2>Errores detectados:</h2>
        <ul>
            {''.join(f"<li>{e}</li>" for e in errores)}
        </ul>
        <h2>Posibles soluciones:</h2>
        <ul>
            {''.join(f"<li>{s}</li>" for s in soluciones)}
        </ul>
    </body>
    </html>
    """
    pdfkit.from_string(contenido_html, nombre_archivo)
    print(f"Reporte guardado como: {nombre_archivo}")

def analizar_pagina(url):
    print("Analizando estructura HTML...")
    errores_html, soluciones_html = analizar_html(url)

    print("Analizando renderizado y errores JS...")
    errores_render, soluciones_render = analizar_renderizado(url)

    errores = errores_html + errores_render
    soluciones = soluciones_html + soluciones_render

    generar_reporte_pdf(url, errores, soluciones)

# === EJECUCIÓN ===
if __name__ == "__main__":
    url = input("Ingresa la URL a analizar (con http/https): ")
    analizar_pagina(url)

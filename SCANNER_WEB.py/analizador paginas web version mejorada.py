import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import pdfkit
import argparse
import shutil
import os

def verificar_dependencias():
    if shutil.which("wkhtmltopdf") is None:
        print("⚠️  Advertencia: wkhtmltopdf no está instalado. La generación del PDF podría fallar.")
        print("Descárgalo desde: https://wkhtmltopdf.org/downloads.html\n")

def analizar_html(url):
    errores = []
    soluciones = []

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')

        if not soup.find('html'):
            errores.append("No se encontró la etiqueta <html>")
            soluciones.append("Agregar la etiqueta <html> para una estructura válida")

        if not soup.find('title'):
            errores.append("No se encontró una etiqueta <title>")
            soluciones.append("Agregar un título a la página con <title>")

        if not soup.find('meta', attrs={'name': 'description'}):
            errores.append("Falta la meta descripción")
            soluciones.append("Agregar <meta name='description' content='...'> para SEO")

        if not soup.find('h1'):
            errores.append("Falta una etiqueta <h1>")
            soluciones.append("Agregar una etiqueta <h1> que describa el contenido principal")

        html_tag = soup.find('html')
        if html_tag and not html_tag.get('lang'):
            errores.append("Etiqueta <html> sin atributo 'lang'")
            soluciones.append("Agregar el atributo lang='es' (o el idioma correspondiente) en <html>")

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
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        console_logs = []
        def log_error(msg):
            if msg.type == "error":
                console_logs.append(msg.text)

        bad_responses = []
        def check_response(resp):
            if resp.status >= 400:
                bad_responses.append(f"{resp.status} en {resp.url}")

        page.on("console", log_error)
        page.on("response", check_response)

        try:
            page.goto(url, timeout=30000)
            page.wait_for_load_state('networkidle')
            page.wait_for_timeout(3000)  # Espera extra por si hay JS tardío

            errores += [f"JS Error: {msg}" for msg in console_logs]
            if console_logs:
                soluciones.append("Revisar el código JavaScript que lanza errores en la consola")

            errores += bad_responses
            if bad_responses:
                soluciones.append("Verificar que todos los recursos (imágenes, scripts, etc.) estén disponibles (no 404/500)")

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
    li {{ margin-bottom: 5px; }}
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
    try:
        pdfkit.from_string(contenido_html, nombre_archivo)
        print(f"\n✅ Reporte guardado como: {nombre_archivo}")
    except Exception as e:
        print(f"❌ Error al generar el PDF: {str(e)}")
        print("Asegúrate de tener wkhtmltopdf instalado y accesible en tu PATH.")

def analizar_pagina(url):
    print("🔍 Analizando estructura HTML...")
    errores_html, soluciones_html = analizar_html(url)

    print("💻 Analizando renderizado y errores JS...")
    errores_render, soluciones_render = analizar_renderizado(url)

    errores = errores_html + errores_render
    soluciones = soluciones_html + soluciones_render

    generar_reporte_pdf(url, errores, soluciones)

if __name__ == "__main__":
    verificar_dependencias()

    parser = argparse.ArgumentParser(description="Analiza una página web y genera un reporte de errores en PDF.")
    parser.add_argument("url", help="URL a analizar (con http o https)")
    parser.add_argument("--output", help="Nombre del archivo PDF de salida", default="reporte_errores.pdf")
    args = parser.parse_args()

    analizar_pagina(args.url)

import streamlit as st
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import pdfkit
import shutil
import os

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
            soluciones.append("Agregar el atributo lang='es' (o el idioma correspondiente)")

        for img in soup.find_all('img'):
            if not img.get('alt'):
                errores.append(f"Imagen sin atributo alt: {img.get('src')}")
                soluciones.append("Agregar atributo alt a todas las imágenes para accesibilidad")

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
            page.wait_for_timeout(3000)

            errores += [f"JS Error: {msg}" for msg in console_logs]
            if console_logs:
                soluciones.append("Revisar el código JavaScript que lanza errores en consola")

            errores += bad_responses
            if bad_responses:
                soluciones.append("Verificar que todos los recursos estén disponibles (no 404/500)")

        except Exception as e:
            errores.append(f"Error al renderizar página: {str(e)}")
            soluciones.append("Verificar errores de red o estructura del sitio")

        finally:
            browser.close()

    return errores, soluciones

def generar_reporte_pdf(url, errores, soluciones, nombre_archivo="reporte.pdf"):
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
    pdfkit.from_string(contenido_html, nombre_archivo)

# === INTERFAZ STREAMLIT ===
st.title("🔍 Analizador de Sitios Web")
st.write("Introduce una URL para analizar la estructura HTML y errores de JavaScript.")

url = st.text_input("URL (incluye http o https):", "https://www.example.com")
if st.button("Analizar"):
    if not url.startswith("http"):
        st.warning("La URL debe comenzar con http o https")
    else:
        st.info("Analizando HTML...")
        errores_html, soluciones_html = analizar_html(url)

        st.info("Analizando JavaScript y recursos...")
        errores_render, soluciones_render = analizar_renderizado(url)

        errores = errores_html + errores_render
        soluciones = soluciones_html + soluciones_render

        if errores:
            st.error("Errores detectados:")
            for e in errores:
                st.write("- " + e)

            st.success("Posibles soluciones:")
            for s in soluciones:
                st.write("- " + s)
        else:
            st.success("¡No se encontraron errores!")

        reporte_pdf = "reporte_errores.pdf"
        generar_reporte_pdf(url, errores, soluciones, reporte_pdf)

        with open(reporte_pdf, "rb") as file:
            st.download_button("📄 Descargar reporte PDF", data=file, file_name=reporte_pdf, mime="application/pdf")

from selenium import webdriver
from bs4 import BeautifulSoup
import time

def analizar_pagina(url):
    # Configuración del WebDriver
    driver = webdriver.Chrome(executable_path='/ruta/a/chromedriver')
    driver.get(url)
    time.sleep(5)  # Esperar a que la página cargue completamente

    # Obtener el contenido HTML
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Cerrar el navegador
    driver.quit()

    return soup
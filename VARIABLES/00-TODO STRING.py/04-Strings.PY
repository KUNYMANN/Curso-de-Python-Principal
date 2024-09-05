#STRING: ES LA UNION DE VARIOS CARACTERES, PUEDEN SER ORDENADOS O DESORDENADOS
#para PYTHON un STRING siempre va entre comillas simples o dobles
'con print ("nosotros podemos crear nuestros propios mensajes o string")'
"siempre que cumpla con la caracteristica de estar entre comillas es un STRING"
#Ejemplo
print("buenas tardes")
print("STP")
print("1980")
#para categorizar a un strigs tiene que estar dentro de una variable
cadena='Esto es un ejemplo de cadena de texto' #comillas simples
cadena1="Esto es un ejemplo de cadena de texto" #comillas dobles
print(cadena)
print(cadena1)

#si yo quiero destacar algun carater, palabra o texto dento de una cadena debo alternar las comillas
#Ejemplo
cadena3='Esto lo quiero "resaltar"'
print(cadena3) #'Esto lo quiero "resaltar"'
cadena4="Esto lo quiero 'resaltar'"
print(cadena4) #"Esto lo quiero 'resaltar'"
'''Si yo no alterno las comillas va a dar Error, salvo en el metodo siguiente llamado: ESCARPAR CARACTERES'''

#ESCARPAR CARACTERES (Para la documentacion de PYTHON, o sea lo formal, se lo llama STRING LITERALS)
#para "ESCAPAR CARACTERES O STRING LITERALS" utilizamos LA BARRA "\" (SLASH INVERTIDO)
# esta barra "\" va ha hacer que nuestro string tenga un comportamiento diferente
'''vemos que si al usar en una cadena de texto las mismas comillas "para encerrar el strig" y "para resaltar",  
nos daba un error, en cambio,  si utilizamos el slash invertido \ no nos va a devolver un error'''
#por que??? porque python detecta que no estas cerrando el string, sino que estas colocando comillas para destarcar algo en el texto
#Ejemplo
literal="Esto es un \"ejemplo\" de cadena de texto" # en ambos casos aqui usamos las comillas dobles, pero ocurre lo mismo para comillas simples
literals='Esto es un \'ejemplo\' de cadena de texto' # la diferencia esta en que colocamos el slash invertido \ para que no arroje error
print(literal) # Esto es un "ejemplo" de cadena de texto
print(literals) # Esto es un 'ejemplo' de cadena de texto

#SALTOS DE LINEA para realizarlo se utiliza "\n" (slash invertido n)
salto_de_linea='quiero que se muestre \n"este texto", \nen varias lineas \no renglones'
print(salto_de_linea) # quiero que se muestre
                      # "este texto",
                      # en varias lineas
                      # o renglones

#TABULACION se utiliza "\t" (slash invertido t)
tabular='quiero que realize una "tabulacion" \taqui'
print(tabular)#quiero que realize una "tabulacion" ----aqui

#ELIMINAR ESPACIO se utiliza "\b" (slash invertido b)
# 1. \b (Backspace)
'La secuencia \b se usa para eliminar el carácter inmediatamente anterior a donde se coloca la secuencia. Es útil cuando quieres simular la eliminación de texto en la terminal.'
#*Ejemplo:*
print("Hola Mundo\b!")
#*Salida:*
'''Hola Mund!
En este caso, el carácter "o" en "Mundo" es eliminado y reemplazado por el signo de exclamación.'''

eliminar_espacio="quiero eliminar el espacio entre esta \bpalabra y la \botra"
print(eliminar_espacio)#quiero eliminar el espacio entre estapalabra y laotra

#PARA COLOCAR SIMBOLO DE SEXO femenino se utiliza "\f" (slash invertido \ f)
simbolo="muestra el simbolo para sexo '\f' femenino"
print(simbolo) #muestra el simbolo para sexo femenino '♀'
#Para SEXO masculino (varon) se utiliza "\v" (slash invertido \ v)
simbolo="muestra el simbolo para sexo '\v'masculino"
print(simbolo) #muestra el simbolo para sexo masculino '♂'

#Longitud de una cadena en Python
'para obtener la longitud de una cadena se debe utilizar la función de Python len()'
cadena="motocicleta"
print(len(cadena))

#para resaltar un string dentro de otro string
'en un solo renglon si usas comillas simples para crear el string, para resaltar se utilizan las dobles o viseversa tantas veces como las necesites'
s='Hola "rey" ¿Te gusta Python?'
print(s)
s="Hola 'genio' ¿Te gusta Python?"
print(s)

'si el texto esta en varios renglones para lo cual se utilizan tres comillas dobles """ """ asi que solo se utilizara para resaltar comillas simples'
s=("""'Hola'
 'kuny'
 '¿Te gusta Python?'""")
print(s)

'si queremos que el texto salga impreso en un solo renglon utilizamos el slash "\"'
t=("""'Hola\
 'santi'\
  ¿Te gusta Python?'""")
print(t)
'si el texto esta en un solo renglon y queremos que lo imprima en varios renglones utilizamos"\n"'
n="\neste\nstring\nocupa\nmuchos\n lugares" #si aplico un espacio entre n\ y la palabra lo imprimira tambien por consola
print(n)  # este
          # string
          # ocupa
          # muchos
          #  lugares"

'''Además del carácter ' y ", hay otros caracteres especiales que para ser usados dentro de una cadena necesitan ser «escapados» con el carácter \.
Son, entre otros, los siguientes: tabulador (\t), barra invertida (\\), retroceso (\b), nueva línea (\n) o retorno de carro (\r).'''
# Ejemplo para declarar una ruta en Windows
s = 'C:\\Users\\Documents\\'
print(s)
#C:\Users\Documents\

# Nueva línea más tabulador
s = 'Hola\n\tPythonista'
print(s)
#Hola
    #Pythonista

print()# de esta maneta con el print vacio genera un renglon vacio en la consola

#Las secuencias de escape \b (backspace) y \r (carriage return) en Python se utilizan para controlar el formato del texto en la salida, 
# generalmente para modificar lo que se muestra en la terminal. Aquí te explico cómo y cuándo podrías usarlas:

### 1. \b (Backspace)
'La secuencia \b se usa para eliminar el carácter inmediatamente anterior a donde se coloca la secuencia. Es útil cuando quieres simular la eliminación de texto en la terminal.'
#*Ejemplo:*
print("Hola Mundo\b!")
#*Salida:*
'''Hola Mund!
En este caso, el carácter "o" en "Mundo" es eliminado y reemplazado por el signo de exclamación.'''

### 2. \r (Carriage Return)
'''La secuencia \r mueve el cursor de la terminal al inicio de la línea sin avanzar a la siguiente. 
Esto significa que cualquier texto escrito después de \r sobrescribirá el texto existente en esa línea.'''
#*Ejemplo:*
print("Hola Mundo\rPython")
#*Salida:*
'''Pythono Mundo
En este caso, "Python" sobrescribe los primeros caracteres de "Hola Mundo", resultando en "Pythono Mundo".'''

### ¿Cuándo se usarían?
'*\b*: Si estás simulando una barra de progreso o deseas corregir un texto sin borrar toda la línea, como en interfaces de consola interactivas.'
  
''' *\r*: Es común en la implementación de barras de progreso donde quieres actualizar el estado en la misma línea en lugar de crear una nueva línea cada vez. 
También se usa para sobrescribir mensajes en la consola.'''

#*Ejemplo de barra de progreso:*

import time

for i in range(10):
    print(f"\rProgreso: {i+1}/10", end="")
    time.sleep(0.5)
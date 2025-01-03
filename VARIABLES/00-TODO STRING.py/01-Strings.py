#STRING
'La clase str en Python se utiliza para representar "texto", más conocido en el mundo de la programación como string o cadena de caracteres'
'''el tipo str es una secuencia inmutable de caracteres Unicode. Por tanto, al igual que "list", "tuple" o "range", es un tipo secuencial y como es inmutable, 
un objeto de este tipo no se puede modificar después de haber sido creado.'''

#Crear una cadena de texto en Python es muy sencillo. Simplemente encierra una secuencia de caracteres entre comillas simples '' o dobles "".
string="texto"
print(string)
texto="Hola Mundo" #dato STRING
#      0123456789 cada caracter dentro de un dato tiene asignado un indice y este comienza desde 0 
#      tambien se cuenta como caracter a los espacios vacios
print(texto) #con Shift + Alt mas flecha hacia abajo se duplica la linea 

'para saber en que posicion esta un elemento'
print(string[0])
print(string[-1])


#for str Python – se utiliza "for c in" y el nombre de la variable  en el print va a recorrer los caracteres de una cadena
saludos="HOLA"
for c in saludos:
   print(c)
# con la funcion "in" podemos saber si algun caracter esta contenido dentro del string o cadena 
# y al ser una comparacion arrojara un booleano
saludo="hola"
print ("o" in saludo)
print("r" in saludo)
#y negando lo falso con "not in" (no es cierto) que tal caracter este dentro del valor de la variable 
print("p" not in saludo)#es verdadero, porque en este caso la "p" no esta dentro de la variable "hola", 
                        #o lo que es lo mismo decir 'si, "p" no esta dentro de la palabra "hola"'

#Comprobar si dos strings son iguales en Python, como es una comparacion arrojara un booleano
'para comparar si dos cadenas de caracteres son iguales, se utiliza el operador de igualdad =='

a="hola"
b="hola"
print(a==b) #True
'''Dos strings son iguales "si y solo si" ambas cadenas contienen la misma secuencia de caracteres
 (se distingue entre mayúsculas y minúsculas).'''
c="holA"
print(a==c) #False (porque la A del final de la palabra esta en mayusculas)

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
 'Santi'\
  ¿Te gusta Python?'""")
print(t)
'si el texto esta en un solo renglon y queremos que lo imprima en varios renglones utilizamos"\n"'
n="\neste\nstring\nocupa\nmuchos\n renglones" #() luego del \n hay un espacio y luego la palabra renglones
print(n)  # este
          # string
          # ocupa
          # muchos
          #  renglones"  ()aqui la palabra esta separada del margen y no como lo esta el resto porque?
                          #porque si aplico un espacio entre n\ y la palabra lo imprimira tambien por consola
'''Además del carácter ' y ", hay otros caracteres especiales que para ser usados dentro de una cadena necesitan ser «escapados» con el carácter \.
Son, entre otros, los siguientes: tabulador (\t), doble barra invertida (\\), retroceso (\b), nueva línea (\n) o retorno de carro (\r).'''
# Ejemplo para declarar una ruta en Windows
s = 'C:\\Users\\Documents\\'
print(s) #C:\Users\Documents\

# Nueva línea más tabulador
s = 'Hola\n\tPythonista'
print(s)
#Hola
    #Pythonista

print()# de esta maneta con el print vacio genera un renglon vacio en la consola

# Aquí, \n es interpretado como nueva línea
s = 'C:\python\noticias' 
print(s)
#C:\python
#oticias
'como deberiamos hacer para que no se reconozca \n como un salto de linea'
# hay que incertar una "r" al comienzo del valor de la variable
# En una raw string no se interpreta el carácter \
s = r'C:\python\noticias'
print(s)
#C:\python\noticias
str()
print(str)


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
'''La secuencia \r mueve el cursor de la terminal al inicio de la línea sin avanzar ni hacer un salto de renglon, solo que va a sobreescribir el texto que estaba anteriormente escrito
por el que se encuentra despues de \r .'''
#*Ejemplo:*
print("EL Texto viejo va a ser reemplazado por \r EL TEXTO NUEVO")
#*Salida:*
'''"EL Texto viejo va a ser reemplazado por EL NUEVO TEXTO
En este caso, "Python" sobrescribe los primeros caracteres de "EL Texto viejo va a ser reemplazado por", resultando en "EL TEXTO NUEVOva a ser reemplazado por".'''

### ¿Cuándo se usarían?
'*\b*: Si estás simulando una barra de progreso o deseas corregir un texto sin borrar toda la línea, como en interfaces de consola interactivas.'
  
''' *\r*: Es común en la implementación de barras de progreso donde quieres actualizar el estado en la misma línea en lugar de crear una nueva línea cada vez. 
También se usa para sobrescribir mensajes en la consola.'''

'''#*Ejemplo de barra de progreso:*
import time
for i in range(10):
    print(f"\rProgreso: {i+1}/10", end="")
    time.sleep(0.5)
print()'''
#*Salida (sobrescribiéndose en la misma línea):*
'''Progreso: 1/10,
Progreso: 2/10 y asi sucesivamene hasta llegar a
Progreso: 10/10
Aquí, el cursor regresa al inicio de la línea y sobrescribe el texto sin crear nuevas líneas.'''


#Aquí tienes una lista de los métodos más comunes que puedes utilizar con cadenas (str) en Python:

'''Métodos de str
Métodos de modificación de texto:

str.lower(): Convierte todos los caracteres a minúsculas.
str.upper(): Convierte todos los caracteres a mayúsculas.
str.title(): Convierte la primera letra de cada palabra a mayúscula.
str.capitalize(): Convierte la primera letra a mayúscula y el resto a minúsculas.
str.strip(): Elimina espacios en blanco al inicio y al final.
str.lstrip(): Elimina espacios en blanco a la izquierda.
str.rstrip(): Elimina espacios en blanco a la derecha.
Métodos de búsqueda y reemplazo:

str.find(sub): Devuelve el índice de la primera aparición de sub, o -1 si no se encuentra.
str.rfind(sub): Devuelve el índice de la última aparición de sub, o -1 si no se encuentra.
str.replace(old, new): Reemplaza todas las apariciones de old por new.
str.count(sub): Cuenta cuántas veces aparece sub en la cadena.
Métodos de partición y unión:

str.split(sep=None): Divide la cadena en una lista utilizando sep como delimitador.
str.join(iterable): Une los elementos de iterable en una sola cadena, separándolos con la cadena original.
Métodos de formato:

str.format(): Formatea la cadena utilizando marcadores de posición.
str.fstring(): Permite formatear cadenas usando literales de cadena f.
Métodos de verificación:

str.isalpha(): Devuelve True si todos los caracteres son letras.
str.isdigit(): Devuelve True si todos los caracteres son dígitos.
str.isalnum(): Devuelve True si todos los caracteres son alfanuméricos.
str.isspace(): Devuelve True si todos los caracteres son espacios en blanco.
str.startswith(prefix): Devuelve True si la cadena comienza con prefix.
str.endswith(suffix): Devuelve True si la cadena termina con suffix.
Métodos de conversión:

str.encode(encoding='utf-8'): Convierte la cadena a bytes usando el encoding especificado.
str.strip() o str.lstrip() o str.rstrip(): Elimina espacios en blanco.'''

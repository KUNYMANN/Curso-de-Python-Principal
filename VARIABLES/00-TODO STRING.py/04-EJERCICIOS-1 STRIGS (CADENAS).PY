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
print(cadena4) #"Esto lo quiero 'resaltar'""
'''Si yo no alterno las comillas va a dar Error, salvo en el metodo siguiente llamado: ESCARPAR CARACTERES'''

#ESCARPAR CARACTERES (Para la documentacion de PYTHON, o sea lo formal, se lo llama STRING LITERALS)
#para "ESCAPAR CARACTERES O STRING LITERALS" utilizamos LA BARRA "\" (SLASH INVERTIDO)
# esta barra "\" va ha hacer que nuestro estring tenga un comportamiento diferente
'''vemos que si al usar en una cadena de texto las mismas comillas "para encerrar el strig" y "para resaltar",  
nos daba un error, en cambio,  si utilizamos el slash invertido \ no nos va a devolver un error'''
#por que??? porque python detecta que no estas cerrando el string, sino que estas colocando comillas para destarcar algo en el texto
#Ejemplo
literal="Esto es un \"ejemplo\" de cadena de texto" # en ambos casos aqui usamos las comillas dobles, pero ocurre lo mismo para comillas simples
literals='Esto es un \'ejemplo\' de cadena de texto' # la diferencia esta en que colocamos el slash invertido \ para que no arroje error
print(literal) # Esto es un "ejemplo" de cadena de texto
print(literals) # Esto es un 'ejemplo' de cadena de texto

#SALTOS DE LINEA para realizarlo se utiliza "\n" (slahs invertido n)
salto_de_linea='quiero que se muestre \n"este texto", \nen varias lineas \no renglones'
print(salto_de_linea)

#TABULACION se utiliza "\t" (slahs invertido t)
tabular='quiero que realize una \ttabulacion entre "una y tabulacion"'
print(tabular)
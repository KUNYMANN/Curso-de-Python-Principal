'UN METODO va aser una nueva funcion que nos va a permitir crear nuevas utilidadades o que va acambiar el comportamiento de la string'
'cuando hablamos de metodos hablamos de palabras ya reservadas del lenguaje'
'algunos son Metodos que se repiten lenguaje con lenguaje, pero otros son propios de Python'

#METODOS DE CARACTERES
cadena='Estoy utilizando los Metodos de Python'
print(cadena) #con Shift + Alt mas flecha hacia abajo se duplica la linea 

#primero tengo que identificar a que variabe le voy a aplicar un metodo, luego un punto, recordemos que  cada metodo lleva sus propios ()
texto='Estoy utilizando los Metodos de Python' #dato STRING
#      0123456789 cada caracter dentro de un dato tiene asignado un indice y este comienza desde 0 
#      tambien se cuenta como caracter a los espacios vacios

print(texto.upper()) #si elegimos el metodo UPPER()automaticamente pasa todo el texto a MAYUSCULAS
print(texto.lower()) #si elegimos el metodo LOWER()automaticamente pasa todo el texto a minusculas
print(texto.capitalize()) #con capitalize coloca en mayusculas la primera letra de la primer palabra solamente, el resto quedara igual
print(texto.title()) # si elegimo el metodo TITLE()automaticamente pasa a mayuscula las primera letra de cada palabra Del Texto
print(cadena.swapcase())#cambia las MAYUSCULAS a minusculas y las minusculas a MAYUSCULAS
print(texto.find("M")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el caracter solicitado
print(texto.find("zando")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el 1er. caracter solicitado
print(texto.find("metodo")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el 1er. caracter solicitado, pero ATENCION!!! que
# si colocamos mal el texto va a dar error (-1) porque la busqueda se realiza colocando exactamente como esta escrito, respetando si esta en mayuscula o minuscula

'''es posible dividir un string con la funcion "split()". Un ejemplo sencillo de división es el siguiente:'''
text = "Esto es un ejemplo"
print(type(text)) # es un string
print(text.split()) #aqui el metodo split me divide a la frase en elementos de una la lista, utilizando para dividirla los espacios vacios
#El resultado quedaria asi:  ["Esto", "es", "un", "ejemplo"] en text ha sido dividida en todos sus espacios y se devolvió una lista de subcadenas
print(type(text.split())) # es una lista
mi_cadena="soy Hector, mi apodo es kuny, tengo 58 años, juego al basquet"
print(type(mi_cadena))# es un string
print(mi_cadena.split(",")) #aqui el método split() usando el parametro de division la "," devuelve una lista de mi cadena, donde cada parte de la frase 
#hasta la coma, es un elemento de la lista. ejemplo: "soy Hector" es un elemento, "mi apodo es kuny" es otro elemento, y asi sucesivamente
print(type(mi_cadena.split())) # es una lista
print("".join(mi_cadena)) #con el metodo .join() vuelvo a unir los elementos y los transforma en un solo elemento
mi_cadena1=["Manzanas","Naranjas","Peras","Platanos","Bayas"]
'dentro de las comillas puedo colocar con que caracter quiero que me los separe'
print("---".join(mi_cadena1)) 
print("***".join(mi_cadena1)) 
print(type(mi_cadena1))# es una lista
print(type("---".join(mi_cadena1)))# es un string
print(texto.replace("Python","Kuny//"))#de esta manera se reemplaza al nuevo texto o parte del nuevo texto, los Slahs solo los coloque para identificar donde esta el cambio
nuevo_texto=texto.replace("utili","Calzada//") # los Slahs solo los coloque para identificar donde esta el cambio en consola, no cumplen ninguna funcion
print(texto,nuevo_texto)
print(texto.replace("e","X"))#Estoy utilizando los MXtodos dX Python (aqui no rremplazo la primer E porque esta en mayusculas y Python la otoma como otro caracter diferente al de la "e" minuscula)
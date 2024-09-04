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


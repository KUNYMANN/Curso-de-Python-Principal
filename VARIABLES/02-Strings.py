texto="Hola Mundo" #dato STRING
#      0123456789 cada caracter dentro de un dato tiene asignado un indice y este comienza desde 0 
#      tambien se cuenta como caracter a los espacios vacios
print(texto) #con Shift + Alt mas flecha hacia abajo se duplica la linea 
print(texto.upper()) #si elegimos el metodo UPPER()automaticamente pasa todo el texto a MAYUSCULAS
print(texto.lower()) #si elegimos el metodo LOWER()automaticamente pasa todo el texto a minusculas
print(texto.find("M")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el caracter solicitado
print(texto.find("Mun")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el 1er. caracter solicitado
print(texto.find("mun")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el 1er. caracter solicitado
#si colocamos mal va a dar error (-1) porque la busqueda se realiza colocando exactamente como esta escrito, respetando si esta en mayuscula o minuscula
print(texto.replace("Mun","chanchito feliz"))#reemplaza al nuevo texto o parte del nuevo texto
nuevo_texto=texto.replace("Mun","chanchito feliz")
print(texto,nuevo_texto)
print("Mundo"in texto)
print(type(texto)) #con la palabra type () me esta diciendo que tipo de dato es el que estoy solicitando, en este caso me dice que es un string o sea un texto
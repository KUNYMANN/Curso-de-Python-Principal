texto="Hola Mundo" #dato STRING
#      0123456789 cada caracter dentro de un dato tiene asignado un indice y este comienza desde 0 
#      tambien se cuenta como caracter a los espacios vacios
print(texto) #con Shift + Alt mas flecha hacia abajo se duplica la linea 
print(texto.upper()) #si elegimos el metodo UPPER()automaticamente pasa todo el texto a MAYUSCULAS
print(texto.lower()) #si elegimos el metodo LOWER()automaticamente pasa todo el texto a minusculas
print(texto.title()) # si elegimo el metodo TITLE()automaticamente pasa a mayuscula las primera letra de cada palabra Del Texto
print(texto.find("M")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el caracter solicitado
print(texto.find("Mun")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el 1er. caracter solicitado
print(texto.find("mun")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el 1er. caracter solicitado
#si colocamos mal va a dar error (-1) porque la busqueda se realiza colocando exactamente como esta escrito, respetando si esta en mayuscula o minuscula
print(texto.replace("Mun","chanchito feliz"))#reemplaza al nuevo texto o parte del nuevo texto
nuevo_texto=texto.replace("Mun","chanchito feliz")
print(texto,nuevo_texto)
print("Mundo"in texto)
print(type(texto)) #con la palabra type () me esta diciendo que tipo de dato es el que estoy solicitando, en este caso me dice que es un string o sea un texto
print(texto.capitalize()) #con capitalize coloca en mayusculas la primera letra de la primer palabra solamente, el resto quedara igual


nombre=input("Coloque aqui su nombre ")
edad=input("Coloque aqui su edad ")
significado=("TE AMO")
print(f"Sabe que su nombre {nombre} y su edad {edad} tienen un significado ")
print("quieres saber cual es?")
quiero=input ("Diga Si o No si desea saberlo ").lower()


if quiero=='si':
    print("TE AMO")
else:
    print("Lo lamento TE AMO igual jajajajaja")

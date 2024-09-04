texto="Hola Mundo" #dato STRING
#      0123456789 cada caracter dentro de un dato tiene asignado un indice y este comienza desde 0 
#      tambien se cuenta como caracter a los espacios vacios
print(texto) #con Shift + Alt mas flecha hacia abajo se duplica la linea 
print(texto.upper()) #si elegimos el metodo UPPER()automaticamente pasa todo el texto a MAYUSCULAS
print(texto.lower()) #si elegimos el metodo LOWER()automaticamente pasa todo el texto a minusculas
print(texto.capitalize()) #con capitalize coloca en mayusculas la primera letra de la primer palabra solamente, el resto quedara igual
print(texto.title()) # si elegimo el metodo TITLE()automaticamente pasa a mayuscula las primera letra de cada palabra Del Texto
print(texto.find("M")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el caracter solicitado
print(texto.find("Mun")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el 1er. caracter solicitado
print(texto.find("mun")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el 1er. caracter solicitado, ATENCION!!! que
# si colocamos mal el texto va a dar error (-1) porque la busqueda se realiza colocando exactamente como esta escrito, respetando si esta en mayuscula o minuscula

correo=input("Ingrese su correo electronico: ") 
print(correo[:correo.find("@")] + "@ceu.es.com") #de esta manera find busca el indice en que esta ubicado el caracter solicitado "@" y a partir de ahi 
                                                 # con el + se ejecuta en consola el reemplazo por el texto que querramos introducir
precio = input("Introduce el precio del producto con dos decimales: ")
print(precio[:precio.find(".")], "euros y", precio[precio.find(".")+1:], "centimos.") # aqui toma en el valor de la variable "precio" 
#desde el indice 0 por eso no hay nada escrito antes de los ":"  hasta el punto (.) en el valor colocado, ya que pide un valor con decimales, y lo separa
#en dos cadenas. que nos permiten introducir el "string" que querramos, asi que incertamos lo que queremos que aparezca en consola en este caso "euros y" 
# despues colocamos "," para concatenar con la segunda parte del valor que resta a partir del punto (.) por eso se pide del valor introducido en la variable 
# "precio" a partir del (.) en adelante por eso se de ahi que se coloca "+ 1" lo cual sera el siguiente indice que quiero utilizar, 
# si coloco los ":" sin nada detras quiere decir que es hasta el final de la variable que va a imprimir la consola
frase=input("Ingrese una frase: ")
print(frase[::-1]) #colocando de esta manera se invierte la frase letra por letra o lo que se haya ingresado como valor en la variante                                         

print(texto.replace("Mun","Kuny//"))#de esta manera se reemplaza al nuevo texto o parte del nuevo texto los Slahs solo estan para identificar donde esta el cambio
nuevo_texto=texto.replace("Mun","Calzada//") # los Slahs solo estan para identificar donde esta el cambio en consola, no cumplen ninguna funcion
print(texto,nuevo_texto)
print("Mundo"in texto)
print(type(texto)) #con la palabra type () me esta diciendo que tipo de dato es el que estoy solicitando, en este caso me dice que es un string o sea un texto


#PROGRAMA CREADO ESPECIALMENTE PARA MARITA
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

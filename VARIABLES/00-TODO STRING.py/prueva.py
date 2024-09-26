texto=" JeHoVa Mi DioS"
print(texto)
print(texto.split())#crea una lista
print("|".join(texto))#incerta el caracter seleccionado
print(texto.lower())#minuscula
print(texto.upper())#MAYUSCULA
print(texto.title())#Mayusculas Solo al inicio y despues en cada palabra que al que se le antepone un espcio vacio
print(texto.swapcase())#cambia las letras que estaban en MAYUSCULAS a minusculas y viceversa    
print(texto.find("i"))#indica en que posicion se encuentra el primer caracter solicitado dentro de la cadena 
print(texto.strip())#quita espacios vacios al comienzo y al final de la cadena

print()

listado="cafe, te, leche, agua"
print(listado)
print(len(listado))#cantidad de espacios utilizados, incluidos los espacios vacios y los caracteres especiales(,)
print("*".join(listado))#incerta entre caracter y caracter incluidos los espacios vacios el caracter seleccionado 
print(len("*".join(listado)))#cuenta espacios utilizados por la cadena comenzando de 0 incluidos los caracteres incertados en el join "c*a*f*e*,***t*e*,***l*e*c*h*e*,***a*g*u*a*" (cantidad 41)
print("*".join(listado).index("u"))#muestra en que ubicacion se encuentra el por primera vez el caracter solicitado incluidos los caracteres incertados en el join (ubicacion 38)
print(listado.split())#transforma una cadena en una lista utilizando los espacios vacios 
print(len(listado.split()))#cuenta la cantidad de elementos de la lista
print(listado.index("a")) #muestra en que ubicacion se encuentra el por primera vez el caracter solicitado
print(listado.index("agua"))#cuanto mas especifiquemos que estamos buscando mas certera sera la informacion y por ende va a modificar el indice que nos arroje
print(listado.index("e"))#muestra en que ubicacion se encuentra el por primera vez el caracter solicitado
print(listado.index("te"))#cuanto mas especifiquemos que estamos buscando mas certera sera la informacion y por ende va a modificar el indice que nos arroje

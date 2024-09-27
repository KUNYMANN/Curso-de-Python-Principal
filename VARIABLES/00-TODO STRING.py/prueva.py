texto=" JeHoVa Mi DioS"
print(texto)
print(texto.split())#crea una lista
print("|".join(texto))#incerta el caracter seleccionado
print(texto.lower())#minuscula
print(texto.upper())#MAYUSCULA
print(texto.title())#Mayusculas Solo al inicio y despues en cada palabra que al que se le antepone un espcio vacio
print(texto.swapcase())#cambia las letras que estaban en MAYUSCULAS a minusculas y viceversa    
print(texto.find("i"))#indica en que posicion se encuentra el primer caracter solicitado dentro de la cadena 
print(texto.find("r"))#indica en que posicion se encuentra el primer caracter solicitado dentro de la cadena si no lo encuentra arroja un valor -1 
print(texto.strip())#quita espacios vacios al comienzo y al final de la cadena

print()

listado="cafe, te, leche, agua"
print(listado)
print(len(listado))#cantidad de espacios utilizados, incluidos los espacios vacios y los caracteres especiales(,) TOTAL 21
print("*".join(listado))#incerta entre caracter y caracter incluidos los espacios vacios el caracter seleccionado c*a*f*e*,* *t*e*,* *l*e*c*h*e*,* *a*g*u*a
print(len("*".join(listado)))#cuenta espacios utilizados por la cadena comenzando de 0 incluidos los caracteres incertados con JOIN "c*a*f*e*,***t*e*,***l*e*c*h*e*,***a*g*u*a*" (TOTAL 41)
print("*".join(listado).index("u"))#muestra en que ubicacion se encuentra el por primera vez el caracter solicitado, incluidos los caracteres incertados con JOIN (UBICACION 38)
print(listado.split())#transforma una cadena en una lista utilizando los espacios vacios ['cafe,', 'te,', 'leche,', 'agua']
print(len(listado.split()))#cuenta la cantidad de elementos de la lista (TOTAL 4)
print(listado.index("a")) #muestra en que ubicacion se encuentra el por primera vez el caracter solicitado en este caso la "a" de c"a"fe
print(listado.index("agua"))#cuanto mas especifiquemos que estamos buscando mas certera sera la informacion y por ende va a modificar el indice que nos arroje
print(listado.index("e"))#muestra en que ubicacion se encuentra el por primera vez el caracter solicitadoen este caso la "e" de caf"e"
print(listado.index("te"))#cuanto mas especifiquemos que estamos buscando mas certera sera la informacion y por ende va a modificar el indice que nos arroje
'En el metodo INDEX si un valor solicitado no se encuentra, arroja error por consola, a diferencia del metodo FIND que arroja un valor -1 por consola'
print(listado.split()[2])#arroja los objetos que se encuentran EN la posicion solicitada dentro de la lista creada con SPLIT ['leche'] contando desde 0
print(listado.split()[0:2])#arroja los objetos que se encuentran desde / "hasta" la posicion solicitada dentro de la lista creada con SPLIT 
                           #['cafe,', 'te,'] "sin incluir" el objeto solicitado en la segunda peticion [:02]
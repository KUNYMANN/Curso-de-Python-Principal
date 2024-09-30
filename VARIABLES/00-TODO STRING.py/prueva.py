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
print(texto.count("o"))#muestra cuantas veces aparece la letra "o" (TOTAL 2)
print(texto.count("Mi"))#muestra cuantas veces aparece la palabra "Mi" (TOTAL 1)
print(texto.replace("e","X"))#para realizar un reemplazo en este caso la "e" por la "X"  JXHoVa Mi DioS
print(texto.strip().replace("Mi","Amado").swapcase())#tambien para realizar un reemplazo de una palabra "Mi" por la "Amado" y quitando los espacios de inicio y final
                                                     #e intercambiando mayusculas por minusculas y viceversa. jEhOvA aMADO dIOs
print(texto.strip().replace("Mi","Amado").swapcase().count("A")) #muestra de los cambios que sufrio la cadena cuantas letras "A" hay, en este caso (2) jEhOvA aMADO dIOs


print()


listado="cafe, te, leche, agua"
print(listado)
print(len(listado))#cantidad de espacios utilizados, incluidos los espacios vacios y los caracteres especiales(,) TOTAL 21
print("*".join(listado).upper())#incerta entre caracter y caracter incluidos los espacios vacios el caracter seleccionado c*a*f*e*,* *t*e*,* *l*e*c*h*e*,* *a*g*u*a
print(len("*".join(listado)))#cuenta espacios utilizados por la cadena comenzando de 0 incluidos los caracteres incertados con JOIN "c*a*f*e*,***t*e*,***l*e*c*h*e*,***a*g*u*a*" (TOTAL 41)
print("*".join(listado).index("u"))#muestra en que ubicacion se encuentra por primera vez el caracter solicitado, incluidos los caracteres incertados con JOIN (UBICACION 38)
print(listado.split())#transforma una cadena en una lista utilizando los espacios vacios ['cafe,', 'te,', 'leche,', 'agua']
print(len(listado.split()))#cuenta la cantidad de elementos de la lista (TOTAL 4)
print(listado.index("a")) #muestra en que ubicacion se encuentra el por primera vez el caracter solicitado en este caso la "a" de c"a"fe
print(listado.index("agua"))#cuanto mas especifiquemos que estamos buscando mas certera sera la informacion y por ende va a modificar el indice que nos arroje
print(listado.index("e"))#muestra en que ubicacion se encuentra el por primera vez el caracter solicitadoen este caso la "e" de caf"e"
print(listado.index("te"))#cuanto mas especifiquemos que estamos buscando mas certera sera la informacion y por ende va a modificar el indice que nos arroje
'En el metodo INDEX si un valor solicitado no se encuentra, arroja error por consola, a diferencia del metodo FIND que arroja un valor -1 por consola'
print(listado.split()[2])#arroja los objetos que se encuentran EN la posicion solicitada dentro de la lista creada con SPLIT ['leche'] contando desde 0
print(listado.split()[0:2])#arroja los objetos que se encuentran desde / "hasta" la posicion solicitada dentro de la lista creada con SPLIT 
                           #['cafe,', 'te,'] "sin incluir" el objeto solicitado en la segunda peticion [:02] ya que como dijimos es "hasta" no "inclusive"
print(listado.count("e"))#muestra cuantas veces aparece la letra "e" (TOTAL 4)
print(listado.count("te"))#muestra cuantas veces aparece la palabra "te" (TOTAL 1)

"Cuando hay que realizar muchos cambios con metodos conviene generar una nueva variable con todos los cambios"

nueva_variable="*".join(listado).replace("*","|").replace("e","x").upper()#sobre los caracteres incertados con join, se pueden reemplazar con replace e inclusive si tambien se necesita 
                                                          #cambiar un caracter en los restantes. C|A|F|X|,| |T|X|,| |L|X|C|H|X|,| |A|G|U|A
print(nueva_variable)
#Ejemplo
#para no tener que hacer todos los cambios dentro de un print es conveniente crear una nueva variable con los cambios a realizar y solo imprimir la variale final (punto de guardado)
cambios="Lechuga, tomate, apio, cebolla"
print(cambios.replace(",",""))
punto_de_guardado=cambios.replace(",","").split()
print(punto_de_guardado)

print()

lima=["agua azucar,limon" 'y demas ingredientes'] #esta es una lista con un solo objeto(cadena de texto)
limonada=["agua","azucar","limon"]#esta es una lista con varios objetos
print(type(lima))
print(len(lima))
print(lima[:1])

print()

print(type(limonada))
print(len(limonada))
print(limonada[0:2])
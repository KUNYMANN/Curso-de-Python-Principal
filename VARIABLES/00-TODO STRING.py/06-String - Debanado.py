# DEBANADO o SUBSTRING
'''Cuando nosotros tenemos una cadena, cada caracter de la cadena va a ocupar un puesto dentro de la misma,
quiere decir que esto en Python se aplica. Recordemos que cada uno de los caraceres que conforman una cadena 
(o tambien llamada conglomeracion de caracteres, o suma de caracteres), cada letra, cada caracter, 
va a ocupar un espacio, ese espacio va a estar determinado tanto en memoria, como para Python'''

cadena="Este es un ejemplo de substring o lo que es lo mismo Debanado de Cadenas"
print(len(cadena)) #72 caracteres incluido los espacios, asi con este metodo (len())sabemos el tamaño de la cadena

'El debanado o substring de una cadena toma como parte fundamental el espacio de cada caracter'
print(cadena[0]) # "E" aqui me va a mostrar que caracter se encuentra en  el espacio de indice 0 de la cadena. 
                 # recordamos que el primer espacio es el 0 y corresponde al primer caracter de la cadena
print(cadena[2]) # "t" se encuentra en el indice o espacio 2 de la cadena
print(cadena[4]) # aqui no hay caracter dado que el indice o espacio 4 corresponde a un espacio vacio 
print(cadena[50])# "m" se encuentra en el indice o espacio 50 de la cadena
'Como vimos cada caracter, includive los espacios vacios, tiene un espacio valga la redundancia o indice dentro de la cadena'

#AHORA VEAMOS EL DEBANADO
'''Cuando hablamos de debanado le tenemos que pasar dos parametros a la funcion en el print(xzxzx[_:_]), generalmente van a ser numeros
pero en otros casos pueden ser variables'''
print(cadena[0:9])  #"Este es u" aqui el caracter que corresponde al indice 9 es la "n" pero no lo muestra por que es "hasta" el indice 9, no inclusive.
#          indices   "012345678"
print(cadena[0:10]) #"Este es un" aqui vemos que el debanado me va a mostrar que caracteres, inclusive los espacios vacios, que se encuentran entre
                    # el indice 0 "hasta" el indice 10, en el ejemplo justo esta ocupado por un espacio vacio, pero no lo va a mostrar porque es hasta el 10, no inclusive.

print(cadena[0:11]) #"Este es un " aqui el caracter que corresponde al 11 es la "e" pero a este ultimo no lo muestra sino que es "hasta" el 11, no inclusive,    
                    # y como hay un espacio vacio anterior al indice 11 es el que a pesar que no se ve estaria mostrando            

'El debanado de una cadena es recorrer de un punto hacia otro mostrando lo que hay dentro'     
print(cadena[6:58]) #"s un ejemplo de substring o lo que es lo mismo Deban" 

'OTRAS FORMAS'
# Veamos que ocurre si dejo un espacio vacio para cualquiera de los parametros. 

"Primer caso"
# Cuando no colocamos un parametro de inicio, Python va a interpretar que queremos que nos muestre desde el primer indice en este caso el indice 0, aunque no lo exprese, hasta el indice indicado
print(cadena[:20])#"Este es un ejemplo d" 

"Segundo caso"
# Cuando indicamos desde que indice queremos que nos mestre pero no colocamos el segundo parametro,python entiende que va a mostrar hasta el ultimo indice de la cadena aunque no este expresado
print(cadena[10:])#"ejemplo de substring o lo que es lo mismo Debanado de Cadenas" 

'Tercer caso'
print(cadena[23:-5])#"ubstring o lo que es lo mismo Debanado de Ca" 
#Si coloco numeros negativos python interpreta ese numero negativo como primer condicion o parametro, asi que va a contar desde atras hacia adelante y va a mostrar desde el
#indice solicitado en negativo hasta el parametro consignado con numero positivo.
#Es lo mismo que pedirlo asi utilizando dos parametros positivos para el mismo ejemplo
print(cadena[23:67])#"ubstring o lo que es lo mismo Debanado de Ca"
print(cadena[-0])#"E" muestra el incice 0 por mas que este en negativo porque el cero es neutro
print(cadena[-6])#"a" de la palabra Cadenas, ya que estoy solicitando que solo me muestre que caracter hay en el espacio -6 contando de atras hacia adelante

frase="Cuantas veces voy a decir lo mismo"
print(frase[::-1]) #colocando de esta manera se invierte la frase letra por letra o lo que se haya ingresado como valor en la varianble       
print(frase[::2])#Imprime dicha cadena cada dos caracteres. 
print(frase[::5])#si variamos el numero tambien va a variar los saltos de impresion, en este caso lo hara cada 5 caracteres
texto="campeon"
texto2="fenomeno"
#como tambien se pueden sumar ambos textos
print(texto+texto2[::-1])#imprime el primer texto correctamente y sin salto de espacio imprime invertido el segundo texto
print(texto[::-1]+texto2)#imprime el primer texto invertido y sin salto de espacio imprime el segundo texto correctamente

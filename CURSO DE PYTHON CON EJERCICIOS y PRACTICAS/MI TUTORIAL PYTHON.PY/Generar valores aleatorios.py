'la funcion RANDINT(), viene definida dentro del modulo Random, nos permite generar numeros aleatorios'
#Básicamente, un módulo es un archivo o un conjunto de archivos que define una serie de funciones.
'En primer lugar el nombre es run int y va a recibir dos parámetros.'
#Básicamente los parámetros es la información que se necesita para que esta función pueda trabajar y
#necesita los parámetros de A y B para que pueda trabajar.
'randint(a,b) devuelve un numero aleatorioentre ay b, incluyendo estos valores (el de a y el de b)'
#Ahora, según hemos comentado, es necesario importar en primer lugar el módulo de Random.
'Antes de utilizar la función Randint y para importar un módulo utilizamos la sintaxis siguiente.'
#Simplemente ponemos la palabra import y posteriormente el nombre del módulo que vamos a utilizar.
import random #y cuando lo utilizamos debemos colocar .randint() entonces la funcion  quedaria asi: random.randint()
#o tambien podemos importarlo de la sig manera:  
from random import randint
#generar valores aleatorios con la funcion randint()
'QUE EN SI SON VALORES NUMERICOS'
#ejemplo
#Generar un numero aleatorio entre 1 y 10
numero=random.randint(1,10)#como estamos generando un rango de valores el primero no puede ser mayor al segundo
print(f"Valor aleatorio entre 1 y 10 es: {numero}")

#Simular un dado con seis caras
dado=randint(1,6)
print(f"El numero para esta tirada es: {dado}")
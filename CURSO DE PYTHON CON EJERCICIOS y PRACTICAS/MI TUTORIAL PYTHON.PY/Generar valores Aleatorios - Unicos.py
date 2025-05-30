#GENERAR VALKORES ALEATORIOS
'la funcion RANDINT(), que viene definida dentro del modulo Random, nos permite generar numeros aleatorios'
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
print()
#SISTEMA GENERADOR ID UNICO
'''se solicita crear un sistema para generar un ID unico para cada persona
el sistema debe solicitar al usuario lo siguiente:'''
print(" *** GENERADOR DE ID *** ")
nombre=input("Ingrese su Nombre: ")
apellido=input("Ingrese su Apellido: ")
año_nacimiento=input("Ingrese su Año de nacimiento (YYYY): ")
valor_aleatorio=randint(1000,9999)
nombre_usuario=nombre.strip().upper()[0:2]
apellido=apellido.strip().upper()[0:2]
año_nacimiento=año_nacimiento.strip()[2:]

'Colocando en el print de esta forma:'
print(f"La forma de concatenar es: {nombre_usuario}{apellido}{año_nacimiento}{valor_aleatorio} 'para que no aparezcan los espacios vacios entre las concatenaciones'")
#con los datos recibidos del usuario, el sistema debera realizar lo siguiente:
#Del valor recibido del Nombre, usar las dos primeras letras y convertirlas a mayusculas
#Del valor del Apellido, usar las las dos primeras letras y convertirlas a mayusculas
#Del valor del Año, tomar los ultimos dos digitos
#Ademas el sistema debera generar un valor aleatorio de cuatro digitos, con la ayuda de la funcion randint()
#finalmente con los datos obtenidos, generar un ID unico uniendo los valores de la siguiente manera:
     #Nombre: Juan...JU
     #Apellido: Perez ...PE
     #Año: 1986 ...86
     #Valor Aleatorio: randint ...7326
     #RESULTADO ID UNICO: JUPE957326


#abro con tres comillas para imprimir en varios renglones luego coloco \n hago para que  salto de renglon entre el ultimo codigo y este
print(f'''\nHola {nombre.title()},
    Tu nuevo ID generado por el sistema es:
    {nombre_usuario}{apellido}{año_nacimiento}{valor_aleatorio}     
    Felicidades!!!''')

print()

#Ejercicio

print("*** GENERADOR DE PATENTE VEHICULO ***")
nombre_completo=input("Ingrese su nombre completo: ")
vehiculo=input("Ingrese la marca de su vehiculo: ")
color=input("Coloque el color de su vehiculo: ")
dni=randint(100,999)
vehiculo1=vehiculo.strip().upper()[0:2]
color1=color.strip().upper()[0:2]
print(f'''\nSr. Usuario
      {nombre_completo.upper()} 
      Su Numero de Patente es: {vehiculo1}{dni}{color1}
      Gracias por su colaboracion''')
print()



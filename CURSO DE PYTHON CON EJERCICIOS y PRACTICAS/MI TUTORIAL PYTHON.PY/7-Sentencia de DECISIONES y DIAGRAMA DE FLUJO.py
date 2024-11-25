# Las sentencia de decision nos permiten controlar el flujo de ejecucion de un programa
#Las estructuras que se pueden utilizar son: if; else; elif
'''La sentencia if nos permite ejecutar un bloque de código. Si la condición a evaluar es verdadera.
Una condición es una expresión que evalúa a verdadero o falso.'''
#ejemplo: edad=30
   #sintaxis del ejemplo
   #if condicion :
         #bloque de codigo que se ejecuta si la condicion se cumple


edad=int(input("Ingrese su edad para saber si es mayor o menor de edad: "))
if edad>=18>100 : #si la condicion se cumple, en este caso si ingresa un numero mayor o igual a 18 y menor a 100
    print("Eres mayor de edad") #entonces imprimira la siguiente leyenda "Eres mayor de edad"
elif edad<18<0 : #si no se cumple la anterior pero SI esta, que el numero ingresado sea menor a 18 con un parametro minimo de 0 años
    print("eres menor de edad")#entonces imprimira la siguiente leyenda "Eres menor de edad"
else: #en caso que se ingrese un numero mayor a 100 o algun numero negarivo
    print("Dato invalido") #entonces imprimira la siguiente leyenda "Dato invalido"


'DIAGRAMA DE FLUJO'
#Un diagrama de flujo es una representacion grafica de los pasos a ejecutar para lograr un resultado especifico 
#sobre todo cuando estamos creando un algoritmo, un programa, un algoritmo o programa.
'''Como hemos visto hasta el momento, simplemente es la ejecución línea a línea de nuestro programa 
Para crear un diagrama de flujo se utilizan los siguientes símbolos estandarizados para representar
distintos tipos de acciones.
Por ejemplo, un OVALO representa el inicio o fin de un proceso.
En este caso puede ser el inicio de nuestro programa o el fin de nuestro programa.
Por otro lado, por ejemplo, un RECTANGULO muestra instrucciones o acciones a ejecutar, por ejemplo,
crear una variable, mandar a imprimir un resultado, etcétera 
Por otro lado, un ROMBO o DIAMANTE indica decisiones, con múltiples flujos, dependiendo de si la respuesta es verdadera o falsa.
Y entonces justamente vamos a empezar a utilizar este tipo de rombos o diamantes para poder indicar
si vamos a ejecutar un camino u otro, ya que precisamente las sentencias de decisión lo que hacen precisamente
es tomar una decisión para ejecutar solamente un camino u otro.
Y por otro lado, las FLECHAS dirigen el flujo del proceso mostrando la dirección en que se mueve la
secuencia de acciones.'''

#ejemplo: edad=30
   #sintaxis del ejemplo
   #if condicion :
         #bloque de codigo que se ejecuta si la condicion se cumple
'El diagrama de flujo para este ejemplo seria asi:'

#                    O   inicio       ovalo
#              [  edad=30  ]          rectangulo
#              <  edad>=18 >          diamante
#        true |             |false
# ["Eres mayor de edad"]    |         flechas
#             |_____________|
#                    O   fin
# Las sentencia de decision nos permiten controlar el flujo de ejecucion de un programa
#Las estructuras que se pueden utilizar son: if; else; elif

#    SENTENCIA IF

'''La sentencia if nos permite ejecutar un bloque de código. Si la condición a evaluar es verdadera.
"Una condición": es una expresión que evalúa a verdadero o falso.'''
#ejemplo: edad=30
   #sintaxis del ejemplo
   #if condicion :
         #bloque de codigo que se ejecuta si la condicion se cumple

edad=int(input("Ingrese desde el teclado numerico su edad para saber si eres mayor o menor de edad: "))
if 18<=edad<=100: #si la condicion se cumple, en este caso si ingresa un numero mayor o igual a 18 y menor a 100
    print("Eres Mayor de edad") #entonces imprimira la siguiente leyenda "Eres mayor de edad"
elif 18>edad>=0: #si no se cumple la anterior pero SI esta, que el numero ingresado sea menor a 18 con un parametro minimo de 0 años
    print("Eres menor de edad")#entonces imprimira la siguiente leyenda "Eres menor de edad"
else: #en caso que se ingrese un numero mayor a 100 o algun numero negarivo
    print("Dato invalido") #entonces imprimira la siguiente leyenda "Dato invalido"'''
print()


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
'El diagrama de flujo para este ejemplo if seria asi:'

#                    O        inicio         ovalo
#              [  edad=30  ]  variable   rectangulo
#             -<  edad>=18 >- condicion  diamante
#        True |             | False
# ["Eres mayor de edad"]    |         
#             |_____________|(flechas)
#                    |
#                    O   fin                 ovalo

edad=int(input("Ingrese desde el teclado numerico su edad para saber si eres mayor o menor de edad: "))
if edad>=18: #la condicion se cumple, en el caso que ingrese un numero mayor o igual a 18 y menor a 100
    print("Eres mayor de edad") #entonces imprimira la siguiente leyenda "Eres mayor de edad"      
print()

#   SENTENCIA IF - ELSE

"""La sentencia else se utiliza para ejecutar un bloque de código cuando la condición del if es falsa.
Así que tenemos la siguiente sintaxis.
Podemos observar que la sintaxis del bloque if es exactamente el mismo.
Si la condición es verdadera, entonces se va a ejecutar el bloque de código de la sentencia if.
Pero ahora con el nuevo bloque else podemos agregar un bloque de código en caso de que la condición
sea falsa y entonces, si la condición es falsa, se ejecuta el bloque de código else Y si revisamos
el ejemplo anterior, si el valor de edad es diez, entonces esta condición es falsa y si es falsa,
no entramos al bloque if.
Se omite este bloque de codigo y nos vamos directamente al bloque else, ya que la condición que estamos
evaluando es falsa.
Entonces solamente se ejecuta el bloque else y manda a imprimir el mensaje Eres menor de edad?"""
 #Sintaxis sentencia if else
 # if condicion:
    #bloque de codigo que se ejecuta si la condicion es verdadera
 # else:
    #bloque de codigo que se ejecuta si la  condicion anterior es falsa
#Ejemplo  
edad=int(input("Ingrese desde el teclado numerico su edad para saber si eres mayor o menor de edad: "))
if edad>=18:  #la condicion se cumple, en el caso que ingrese un numero mayor o igual a 18 y menor a 100
    print("Eres Mayor de edad") #entonces imprimira la siguiente leyenda "Eres mayor de edad"
else:  #si no se cumple la condicion anterior, pero para que se ejecute esta, el numero ingresado debe ser menor a 18 
    print("Eres menor de edad") #entonces imprimira la siguiente leyenda "Eres menor de edad"

'El diagrama de flujo para este ejemplo if - else seria asi:'

#                        O                           inicio     ovalo         O
#                        |   
#                   [  edad=  ]                      variable   rectangulo   []
#           if           |          else           
#              ----<  edad>=18 >----                 condicion  diamante     <>
#             |                     |
#            True                 False              evaluacion True/False/por dafault
#             |                     |
# ["Eres mayor de edad"]   ["Eres menor de edad"]    print                   ()       
#             |                     |
#             |_____________________|
#                        |   
#                        O                           fin                      O

print()
#SENTENCIA IF - ELIF - ELSE

''' la sentencia elif es una abreviatura de un bloque else if y se utiliza cuando necesitamos verificar
múltiples condiciones una tras otra, y se pueden agregar tantas nuevas condiciones de tipo Elif como
necesitemos. Sin embargo, deben ir después de un if y antes de un bloque else.'''

edad=int(input("Ingrese desde el teclado numerico su edad para saber si eres mayor o menor de edad: "))
if edad>=18 and edad<=100: #la condicion se cumple, en el caso que ingrese un numero mayor o igual a 18 y menor a 100
    print("Eres Mayor de edad") #entonces imprimira la siguiente leyenda "Eres mayor de edad"
elif 18>edad>=0: #si no se cumple la condicion anterior, pero para que se cumpla esta, el numero ingresado debe ser menor a 18 con un parametro minimo de 0 años
    print("Eres menor de edad")#entonces imprimira la siguiente leyenda "Eres menor de edad"
else: #en caso que se ingrese un numero mayor a 100 o algun numero negarivo
    print("Dato invalido") #entonces imprimira la siguiente leyenda "Dato invalido"'''

 #Sintaxis sentencia if else
 # if condicion1:   
 #    #bloque de codigo que se ejecuta si la condicion1 es verdadera
 #elif condicion2:
 #    #bloque de codigo que se ejecuta si la condicion2 es verdadera
 # else:    
 #    #bloque de codigo que se ejecuta si las comndiciones anteriores fueron falsas

'El diagrama de flujo para este ejemplo if - elif - else seria asi:'

#                        O     ...................................................... inicio      ovalo       O
#                        |   
#                    [edad=xx] ...................................................... variable    rectangulo  []
#           if           |               elif              
#              ----<  edad>=18 >----------- ......................................... condicion 1 diamante    <>
#             |                            |
#           True                         False ...................................... evaluacion True /False
#             |                            |                                       
#             |                       <18>edad>=0> .................................. condicion 2 diamante    <>
#             |
#             |                  True elif       False else ......................... evaluacion2 True/False
#             |                     |                 |
# ["Eres mayor de edad"] ["Eres menor de edad"]["Dato invalido"]..................... print                    ()
#             |_____________________|_________________|
#                        |   
#                        O   .......................................................  fin        ovalo        O   

'PARA TENER EN CUENTA, EN TODA EVALUACION IF-ELIF-ELSE SIEMPRE SE IMPRIME LA CONDICION TRUE, AUNQUE EL ELSE LO HAGA POR DEFAULT TAMBIEN ES TRUE'

numero=int(input("Ingrese un numero para saber si es positivo o negativo: "))
if numero>0:
    print("Es un numero positivo")
elif numero<0:
    print("Es un numero negatido")
else:
    print("El numero ingresado es el cero")

'el diagrama seria el siguiente'

#                           O inicio
#                           |
#                  [ingrese un numero]
#                           |
# IF condicion : ---------<numero >0>---------
#               |                             |
#            True                           False
#               |                             |
#        [es positivo]  ELIF condicion  --<numero <0>--
#               |                      |               |
#               |                    True            False 
#               |                      |               |
#               |               [es negativo]      [es cero] ELSE por default
#               |                      |_______________|
#               |______________________|
#                                      O fin

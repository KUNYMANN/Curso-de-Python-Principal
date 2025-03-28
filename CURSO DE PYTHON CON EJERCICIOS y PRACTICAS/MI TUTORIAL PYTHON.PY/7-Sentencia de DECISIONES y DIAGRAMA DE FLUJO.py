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
#                    |
#              [  edad=30  ]  variable   rectangulo
#                    |
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

#                              O inicio
#                              |
#                      [ingrese un numero]
#                              |
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


altura=float(input("Ingrese su altura para determinar su tamaño: "))
if altura>=1.90 and altura<=3:
    print(f"Mides {altura} Eres alto")
elif altura>3:
    print(f"Mides {altura} Eres gigante")    
elif altura<1.89 and altura>1:
    print(f"Mides {altura} Eres de estatura normal")
elif altura<1 and altura>0:
    print(f"Mides {altura} Eres petiso")
else:
    print("El dato ingresado es invalido")


'''Se les pide crear un sistema que ofrezca descuentos dependiendo del monto de la compra o también si
es miembro de la tienda.
Así que dependiendo de estos dos factores se puede ofrecer un descuento y entonces se deben de revisar
las siguientes condiciones.
Primero vamos a revisar si ha comprado más de 1.000 $ y además es miembro de la tienda.
Si cumple con ambas condiciones, entonces se le debe de ofrecer un descuento del 10% sobre el monto
total de su compra.

Ahora, si solo es miembro de la tienda, se le puede ofrecer un descuento del 5% ya que no realizó
compras superiores a mil, sino que solamente es miembro de la tienda.

Y por último, se va a revisar la condición si no es miembro de la tienda, ni tampoco compró más de
1.000 $, entonces el descuento que se le ofrece es del 0%.

No podemos ofrecer ningún descuento si no ha comprado más de 1.000 $ y además tampoco es miembro de
la tienda, así que se les deja realizar este ejercicio.
Obviamente ustedes de manera interna pueden definir las constantes que necesiten para indicar, por
ejemplo, el monto mínimo de compra, que en este caso es el valor de mil.
Posteriormente le deben de pedir al usuario el monto de la compra y también si es miembro de la tienda
y vamos a revisar cómo debe de funcionar el sistema.
Así que si ejecutamos nuestro sistema, el sistema de descuentos nos debe de preguntar cuál fue el monto
de tu compra, por ejemplo 1500.
Y además también nos pregunta si eres miembro de la tienda.
En este caso voy a indicar que sí y por lo tanto tiene que mandar el mensaje.
Felicidades, Has obtenido un descuento del 10% y mostramos el monto de la compra.
Posteriormente el monto del descuento que se va a aplicar y el monto final de la compra con descuento.
Así que lo que va a pagar es 1350.
Esto es lo que debe tener el programa y además también por ejemplo, revisamos otra condición si solamente
hemos comprado 800 $, pero si somos miembros de la tienda, entonces obtenemos un descuento del 5%.
Se realizan los cálculos respectivos, el monto de la compra, el descuento y el monto final de la compra
con descuento es de 760.
Y por último, si el monto fue menor a 1.000 $ y además no somos miembros de la tienda, entonces nos
manda el mensaje No obtuviste ningún tipo de descuento?
Te invitamos a hacerte miembro de la tienda.'''
print(   "****   SISTEMA DE DESCUENTO    ****")
monto_compra=float(input("Ingrese el monto total de su compra: "))
membresia=input("Indique si/no es cliente de la tienda: ").strip().lower()
if monto_compra>=1000 and membresia=="si":
    descuento=monto_compra*10/100
    descuento2=monto_compra-descuento
    print(f"""\nFelicidades!!! por ser cliente y tu compra superar los $ 1.000 
    Te has hecho acreedor al siguiente descuento
    Monto de la compra: ........$ {monto_compra:.2f} 
    Descuento otorgado del 10%: $  {descuento:.2f}
    Tu monto a pagar es ........$ {descuento2:.2f}""")
elif 1000>monto_compra>=500 and  membresia=="si":
    descuento1=monto_compra*5/100
    descuento3=monto_compra-descuento1
    print(f"""\nPor ser cliente pero tu compra no supera los $ 1.000 
    Te has hecho acreedor al siguiente descuento
    Monto de la compra:....... $ {monto_compra}
    Descuento otorgado del 5%: $  {descuento1:.2F} 
    Tu monto a pagar es ...... $ {descuento3:.2f}""")
elif monto_compra>1000 and membresia=="no":
    descuento4=monto_compra*3/100
    descuento5=monto_compra-descuento4
    print(f'''\nPor ser cliente 
    Te has hecho acreedor al siguiente descuento
    Monto de la compra: ........$ {monto_compra:.2f} 
    Descuento otorgado del 3%: $   {descuento4:.2f}
    Tu monto a pagar es ........$ {descuento5:.2f}
"TE INVITAMOS A HACERTE SOCIO DE LA TIENDA"''')
else:
    print(f'''\nPor no ser cliente 
     Su monto a pagar es $ {monto_compra:.2f}

"TE INVITAMOS A HACERTE SOCIO DE LA TIENDA"''')


print()
'''Vamos a crear algunos ejemplos para poner en práctica las sentencias de decisión y también el operador
NOT para aplicar una lógica inversa en nuestros programas.
Así que para ello vamos a simular que estamos dentro de un sistema bancario.
Considerando que estamos dentro de un sistema bancario, se solicita preguntar al usuario si desea continuar
dentro del sistema y utilizando el operador NOT.
Para aplicar una lógica inversa se debe de programar las siguientes condiciones.
Si no deseamos salir del sistema, se manda a imprimir el mensaje.
Continuamos dentro del sistema, de lo contrario se va a mandar a imprimir saliendo del sistema.'''

print('*** SISTEMA BANCARIO ***')
salir_del_sistema=input('Deseas salir del sistema si/no: ')
salir_sistema=salir_del_sistema.strip().lower()=='si'
if not salir_sistema:
    print("Continuar dentro del sistema")
else:
    print('Saliendo del sistema')

print()

print('*** CASA DE LOS ESPEJOS ***')
edad=float(input("Ingresen su edad: "))
miedo=input('Le tienes miedo a la oscuridad (Si/No): ')
miedoso=miedo=="si".strip().lower()
if not miedoso and edad>=10 :
    print("Puedes ingresar")
else:
     print('No puedes ingresar')
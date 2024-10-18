"El OPERADOR DE ASIGNACION se utiliza para asignar un valor a una variable, y se representa con el simbolo de ' = ' "
#Sintaxis operador de asignacion
variable="valor"
#ejemplo
numero=10
texto="Bienvenidos"

'''para poder usar operadores de asignacion previamente es fundamental declarar
una variable y asignarle un valor inicial, porque estos solo sirven para
aumentar, disminuir, dividir, multiplicar a lo que ya tenemos, en caso de no 
hacerlo python no va a saber a quien aplicarle dicho valor asignado al operador
y generara un error'''

'''AQUI EN EL EJEMPLO VEMOS UNA VARIABLE CON UN VALOR ASIGNADO, LOS OPERADORES DE ASIGNACION 
VAN A UTILIZAR A ESTA VARIABLE PARA APLICAR EL RESTO DE LAS FUNCIONES PARA QUE AUMENTE O DISMINUYA
SEGUN EL OPERADOR ARITMETICO QUE LE ASIGNEMOS'''

a=2   #VARIABLE CON SU VALOR ASIGNADO
a=a+5 # esta es la forma larga de escribir una operacion de asignacion
print(a)#7
'Metodos acotados de asignacion'
a=2   # a continuacion utilizamos los metodos acortados de los operadores de asignacion a vale 2
a+=5  #suma en asignacion 
print(a)#7 (si a vale 2 mas 5 es igual a 7)

a-=2  #resta en asignacion
print(a)#5 (el valor de arrastre de a es 7 menos el valor asignado 2 da 5)

a*=3 #multiplicacion por asignacion
print(a)#15 (el valor de arrastre de a es 5 por el valor asignado 3 da 15)

a/=3 #division en asignacion
print(a)#5 (el valor de arrastre de a es 15 dividido el valor asignado 3 da 5)

a**=2 #potenciacion en asignacion
print(a)#25 (el valor de arrastre de a es 5 elevado al cuadrado por el valor asignado 2 da 25)

a%=2 #modulo en asignacion da como resultado el resto de la division
print(a)#5 (el valor de arrastre de a es 7 menos el valor asignado da 5)

a=2    # VARIABLE CON SU VALOR ASIGNADO              2
a+=5   #suma en asignacion                           2+5=7
a-=2   #resta en asignacion                              7-2=5
a*=3   #multiplicacion en asignacion                         5*3=15
a/=3   #division en asignacion                                   15/3=5
a**=2  #potenciacion en asignacion                                    5**2=25
a%=2   #modulo en asignacion da como resultado el resto de la division     25/2=12                  y resto 1
print(a) #aqui el print nos arroja el ultimo valor asignado a la variable pero con los valores de arraste ( 1 )

'''En Python tambien enemos la asignacion de variables multiples, lo que nos permite asignarvalores a varias variables
en una sola linea de codigo. El codigo es mas compacto y facil de leer'''
valor1=10
valor2=3.14
#sintaxis de asignacion multiples
variable1,variable2=valor1,valor2
print()
#asignacion multiple de distintos datos
a,b,c,=10,"Cancion",14.5 #pueden ser tanto numeros (int o float) como str
#Ejemplo
x,,y,z=
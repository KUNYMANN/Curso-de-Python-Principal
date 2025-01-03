# OPERADORES ARITMETICOS
'''Los operadores aritmeticos son símbolos especiales que representan cálculos
(+-*/%<>) como la suma o la multiplicación. 
Los valores a los cuales se aplican esos operadores reciben el nombre de operandos.'''
# 1. Paréntesis (): Los paréntesis tienen la mayor precedencia
# 2. Exponente **: Este operador calcula la potencia de un número.
# 3. Unario +, -: Estos operadores realizan operaciones unarias de positivo y negativo
# 4. Multiplicación *, División /, División entera //, Módulo %
# 5. Suma +, Resta -: Estos operadores realizan operaciones aritméticas.
# 6. Comparaciones (==, !=, >, <, >=, <=)
# 7. Operadores lógicos not, and, or
# 8. Asignación (=, +=, -=, *=, /=, entre otros)

suma= 5+2
print(suma)

resta=6-2
print(resta)

multiplicacion=3*5
print(multiplicacion)

division=20/2
print(division)

modulo=25%2
print(modulo)
'MODULO: es un operador que sirve para tomar en cuenta la parte del resto o residuo de una operacion (division)'
"partes de una division"
 #dividendo..> 25 L_2_ <...divisor      
 #             04  12 <...cociente
 #     RESTO..> 1 

'el resto o residuos representa o determina cuanto va a sobrar al realizar una division'
'EL MODULO EVALUA EL RESIDUO O RESTO, no va a evaluar ni el dividendo, ni el divisor ni el cosiente'

exponenciacion=6**3 
print(exponenciacion)


'la division entera no existe como tal, siempre va a traer implicita todo en relacion a los decimales'
division_comun=44/5 #en una division comun representado con un solo "/" nos va a mostrar el cociente con los decimales si esta tuviera
print(division_comun) # 8.8
'Una division entera nos va a traer solo la parte entera del cociente'
division_entera=44//5 # con doble "//" nos va a mostrar la parte entera del cociente, aunque este tuviese decimales
print(division_entera) # 8

"""PARA LA RADICACION NO EXISTE UN OPERADOR ARITMETICO IMPLICITO sino que en lugar se utilizan
   operadores y funciones disponibles para calcular RAICES"""

numero=25
raiz_cuadrada = numero ** (1/2)
print(raiz_cuadrada)  # Salida: 5.0

numero1=27
raiz_cuadrada=numero1**(1/3)
print(raiz_cuadrada)

numero2=10  #numero al que queremos aplicar la raiz
n=5         #este dato es el valor de raiz que queremos extraer
raiz_n=numero2**(1/n) #operacion realizada para obtener el resultado de hallar la raiz 5 del numero 10 
                      #(numero2 elevado a (1 dividido el valor de raiz))
print(raiz_n)# 3.105422 resultado


#JERARQUIAS DE LAS OPERACIONES
'''que es una JERARQUIA; cuando se presentan muchas operaciones aritméticas, la ferarquia determina
el orden con el que deben realizarse dichas operaciones matemáticas'''

#orden de operaciones en python: 

'PARENTESIS: ()' # es el primer proceso que realiza, resuelve lo que esta dentro de los parentesis

'EXPONENCIACION:**' # si el programa detecta una exponanciacion, es el segundo proceso que realiza

'UNARIOS:+ -'# (+)positivo y (-)negativo

'MULTIPLICACION, DIVISION, DIVISION ENTERA Y MODULO: *, /, //, % ' # ocupa el penultimo de los procesos de la operacion matematica

'SUMA Y RESTA' # al final, iniciando siempre de izquierda a derecha

'COMPARACION: ==, !=, <, <=, >, >= ' # igual que; distinto de; mayor; mayor o igual; menor; menor o igual

'OPERADORES LOGICOS: ' # not, and y or

'OPERADORES DE ASIGNACION COMPUESTOS: =, +=, -=, /=, //=, %=, **=' #igual, igual mas, igual menos, division igual, division entera igual, resto igual, exponente igual
'PRESEDENCIA DE OPERADORES:     ejemplo     5+3*2**2= 17  Distinto de: (5+3)*2**2= 32'
'se resuleve primero el exponente, da 4 luego *3 + 5= 17  Distinto de:   8  *  4 = 32'
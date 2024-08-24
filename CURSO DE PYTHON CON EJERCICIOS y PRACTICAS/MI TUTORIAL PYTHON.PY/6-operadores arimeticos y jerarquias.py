# OPERADORES ARITMETICOS
'''Los operadores aritmeticos son símbolos especiales que representan cálculos
(+-*/%<>) como la suma o la multiplicación. 
Los valores a los cuales se aplican esos operadores reciben el nombre de operandos.'''
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
 #divisor..> 25 L_2_ <...divisor      
 #           04  12 <...cociente
 #   RESTO..> 1 

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

#JERARQUIAS DE LAS OPERACIONES
'''que es una JERARQUIA; cuando se presentan muchas operaciones aritméticas, la ferarquia determina
el orden con el que deben realizarse dichas operaciones matemáticas'''

#orden de operaciones en python: 
#PARENTESIS: es el primer proceso que realiza, resuelve lo que esta dentro de los parentesis

#EXPONENCIACION: si el programa detecta una exponanciacion, es el segundo proceso que realiza

#MULTIPLICACION O DIVISION ocupa el penultimo de los procesos de la operacion matematica

#SUMA Y RESTA iniciando de izquierda a derecha


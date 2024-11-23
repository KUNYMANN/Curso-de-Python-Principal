#JERARQUIAS DE LAS OPERACIONES
'''que es una JERARQUIA; cuando se presentan muchas operaciones aritméticas, la ferarquia determina
el orden con el que deben realizarse dichas operaciones matemáticas'''

#orden de operaciones en python: 

'PARENTESIS: ()' # es el primer proceso que realiza, resuelve lo que esta dentro de los parentesis

'EXPONENCIACION:**' # si el programa detecta una exponanciacion, es el segundo proceso que realiza

'UNARIOS:+ -'# (+)positivo y (-)negativo

'MULTIPLICACION, DIVISION, DIVISION EXACTA Y MODULO: * / // %' # ocupa el penultimo de los procesos de la operacion matematica

'SUMA Y RESTA' # al final, iniciando siempre de izquierda a derecha

'COMPARACION: ==, !=, <, <=, >, >= ' # igual que; distinto de; mayor; mayor o igual; menor; menor o igual

'OPERADORES LOGICOS: ' # not, and y or

'OPERADORES DE ASIGNACION COMPUESTOS: =, +=, -=, /=, //=, %=, **=' #igual, igual mas, igual menos, division igual, division exacta igual, resto igual, exponente igual
'PRESEDENCIA DE OPERADORES:    ejemplo     5+3*2**2= 17  Distinto de: (5+3)*2**2= 32'
'se resuleve primero el exponente da 4 luego *3 + 5= 17  Distinto de:   8  *  4 = 32'

num1=100
num2=50
num3=25
num4=10
print(num1+num2*num3) # 1350
#aqui la jerarquia indica que primero se va a realizar la multiplicacion y luego la suma
#num2 por num3 y al resultado se le va a sumar el num1
'pero que sucede si yo quiero que resuleva primero la suma y luego realice la multiplicacion'
"aqui entran en juego los parentesis, que son los que se ejecutan primero por encima de la jerarquia"
print((num1+num2)*num3) # 3750
#esto quiere decir que por medio de los parentesis le indicamos al programa que es lo que queremos que se ejecute primero
'si yo quiero que se ejecute la resta primero debo indicarlo con los parentesis'
print((num1+num2)*(num3-num4)) # 2250
print((num1+num2)*(num3-num4)/(num1-num1)) #esta operacion va a dar error y es muy importante
#al arrojar ZeroDividionError: division by zero, nos esta diciendo que una division por 0 el resultado es infinito
#saber leer los errores que muestra el programa por consola, nos ayudara a comprender que es lo que temenos que solucionaroperadores.

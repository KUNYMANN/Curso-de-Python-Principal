"""'UN OPERADOR ARITMETICO VA A SER LA REPRESENTACION SIMBOLICA DE UN PROCEDIMIENTO MATEMATICO'
print(2+3) #    5  #operador suma (muestra el resultado de la suma)
print(7-3) #    4   #operador resta (muestra el resultado de la resta)
print(6*3) #   18   #operador multiplicacion (muestra el resultado de la multiplicacion)
print(89/7) #  12.714285  #operador de division simple (muestra el cociente con decimales)
print(89//7) # 12  #operador division entera (muestra el cociente entero, sin decimales)
print(13%4) #   1  #operador modulo (muestra el resto de una division, inclusive si es 0)
print(4**3) #  64  #operador de exponenciacion (muestra el resultado de la multiplicacion del numero tantas veces el exponente)"""


print() #el print (vacio) nos imprime un salto de renglon en la consola

#OPERADORES ARITMETICOS CON VARIABLES
"hay qe tener presente que una variables va a ser un dato al que se le asigna un nombre"
'de igual forma el operador aritmetico va a ser aquel que va a realizar una funcion marematica'

#como mezclarlos
'operador suma'
'hay que saber que estas dos variables son de tipo numerico aunque sean numeros enteros o flotantes'
num1=10
num2=5
'se podrian colocar los numeros directamente pero aqui estamos utilizando variables'
print(num1+num2) #15 aqui el print va a mostrar la suma de los valores asignados a cada variable
#de la misma manera lo hace con el resto de los operadores aritmeticos
print(num1-num2)#resta
print(num1/num2)#division simple
print(num1*num2)#multiplicacion
print(num1**num2)#potenciacion
print(num1//num2)#division entera
print(num1%num2)#modulo=restoº
print(num1**(1/num2))#radicacion (operadores y funciones utilizadas para hallar el resultado)


print() #el print (vacio) nos imprime un salto de renglon en la consola


'podemos reemplazar las variables por los datos  asignados a cada variable'
#Ejemplo
print(10+num2) #15 suma
print(num1-5)#resta
print(10/5)#division simple
print(num1*5)#multiplicacion
print(10**num2)#potenciacion
print(10//5)#division entera
print(num1%5)#modulo=resto
print(10**(1/5))#radicacion (operadores y funciones utilizadas para hallar el resultado)

print() #el print (vacio) nos imprime un salto de renglon en la consola

'Tambien puedo crear variables que ya contengan las operaciones aritmeticas'
numeroX=15
numeroW=10
numeroZ=5.2

suma=numeroX+numeroW+numeroZ
print(suma) #30.2

resta=numeroX-numeroW
print(resta) #5

multiplicacion=numeroW*numeroZ
print(multiplicacion) #52

division_simple=numeroW/numeroX 
print(division_simple)#0.6666

division_entera=numeroW//numeroX
print(division_entera)#0

modulo_o_resto=numeroX%numeroZ
print(modulo_o_resto)#4.6

combinadas=(suma*resta/multiplicacion)**3
print(combinadas) #24.48616
print()
combo=suma*suma/suma-suma**3
print(combo) # -27513.4079
combo0=(suma*suma/suma)-(suma**3)
print(combo0)# -27513.4079
combo1=(suma*suma/suma-suma)**3 # (30.2*30.2/30.2-30.2)**3..... (0)**3 es = 0
print(combo1) #0
combo2=((suma*suma/suma)-suma)**3
print(combo2) #0
combo3=((suma*suma/suma)-(suma))**3
print(combo3) #0

'Y ASI DE TODAS LAS MANERAS POSIBLES manteniendo el orden de jerarquia en la resolucion'

# 1. Paréntesis (): Los paréntesis tienen la mayor precedencia
# 2. Exponente **: Este operador calcula la potencia de un número.
# 3. Unario +, -: Estos operadores realizan operaciones unarias de positivo y negativo
# 4. Multiplicación *, División /, División entera //, Módulo %
# 5. Suma +, Resta -: Estos operadores realizan operaciones aritméticas.
# 6. Comparaciones (==, !=, >, <, >=, <=)
# 7. Operadores lógicos not, and, or
# 8. Asignación (=, +=, -=, *=, /=, entre otros)

#€jemplo
resultado = 12 // 3 + 2 * 3 - 1 #analisis de precedencia de izquierda a derecha (siempre se evalua asi)
# 1. Division entera 12 // 3 = 4
# 2. Multiplicacion 2 * 3 = 6
# 3. Suma 4 + 6 = 10
# 4. Resta 10 - 1 = 9
print(f'Resultado: {resultado}') # resultado = 9
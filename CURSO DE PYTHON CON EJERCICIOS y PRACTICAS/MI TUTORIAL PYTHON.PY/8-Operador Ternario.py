'''El operador ternario en Python es una forma compacta de agregar una condición, y el objetivo es asignar
un valor a una variable dependiendo del valor de la condición, así que es muy parecido a la sintaxis
if else.
Sin embargo, es una sintaxis más compacta y podemos observar la sintaxis.
El objetivo, como hemos comentado, es asignar el valor a una variable.
En primer lugar indicamos el valor en caso de que la condición a evaluar sea verdadero.
Así que por otro lado, vamos a tener otro bloque de código.
Tenemos un bloque de código interno con la sentencia if, posteriormente la condición y también la palabra
else.
Y por otro lado, del lado izquierdo tenemos el valor de verdadero y por otro lado tenemos el valor
a utilizar en caso de que la condición sea falsa y entonces, si la condición es verdadera, se asigna
el valor que hemos establecido a la variable de resultado.
Si la condición es falsa, se asigna este valor a la variable de resultado y todo el código importante
se encuentra dentro de esta sección, el bloque if y posteriormente else.
Y en medio de esta sintaxis la condición a evaluar.'''

#SINTAXIS

'''resultado=      | valor_si_verdadero  | IF   "condicion"    ELSE  | valor_si_falso
  (variable)=      |    (evaluacion T)   |                           | (evaluacion F)    
OPERADOR TERNARIO  |          1          |           2               |      3     '''

#Ejemplo Operador Ternario
edad=float(input("Ingrese su edad: "))
es_adulto="Si" if edad>=18 else "No"# Estamos evaluando que: si la edad es mayor o igual a 18 imprima Si(Verdadero) caso contrario que imprima No 
print(f"Es usted adulto? {es_adulto}") #la evaluacion siempre se hace de izquierda a derecha
''' 1/1 recordemos que es el valor en caso de que la condición sea verdadera y la última parte es el valor
en caso de que la condición haya sido falsa, pero ya sabemos que se tiene que leer de la siguiente
manera. Si la variable de edad es mayor o igual de 18, entonces se regresa el valor de SI y si la condición
es falsa, se regresa el valor de NO.'''
#IMPORTANTE
'''Cabe mencionar que este operador únicamente se recomienda utilizarlo en caso de que el
código sea muy compacto, es decir, que no pase de una línea de código.
Si el código que estamos utilizando sobrepasa una línea, entonces se recomienda utilizar el bloque
if else tal como lo hemos venido trabajando anteriormente.
Y si es un código muy compacto como el que estamos visualizando, entonces podemos utilizar este operador ternario.'''

#EJERCICIO
''' solicita crear una aplicación de salud y fitness que le pida al usuario la siguiente información.
En primer lugar, se le va a pedir el nombre del usuario y posteriormente los pasos caminados en el día.
Además, por nuestra parte de manera interna en nuestro programa definiremos las siguientes constantes.
En primer lugar, la constante de meta de pasos diarios.
La meta es de 10.000 pasos y también vamos a agregar la constante de calorías por paso.
Cuántas calorías se queman aproximadamente por cada paso que damos y agregamos el valor de 0.4?
Este es un valor aproximado en kilocalorías y con esas constantes ya definidas, además de los valores
que ya tenemos, entonces debemos realizar el cálculo de las calorías quemadas según los pasos caminados
y entonces vamos a aplicar la fórmula de calorías quemadas.
Es igual al número de pasos diarios por la constante de calorías por paso, es decir, cuántas calorías
se queman por cada paso y lo multiplicamos por los pasos diarios.
Esto nos va a dar la cantidad de calorías quemadas en kilocalorías.
Y por último, también vamos a verificar si se cumplió la meta de pasos diarios para saber si se alcanzó la meta.'''
print()
nombre_de_usuario=input("Ingrese su nombre de usuario: ").strip().upper()
pasos=int(input("Ingrese la cantidad de pasos realizados en el dia: "))
print(f"\nSu nombre de usuario es: {nombre_de_usuario}")
print(f"\nLa cantidad de pasos ingresados es: {pasos}")
meta_pasos_diarios=10000
calorias_por_paso=0.04
calorias_quemadas=pasos*calorias_por_paso
print(f"\nTus calorias quemadas fueron de: {calorias_quemadas:.2F}")
meta_alcanzada=pasos>=meta_pasos_diarios
objetivo="Si"if pasos>=10000 else "No"
print(f"\nHas alcanzado tu meta? {objetivo}")
print()
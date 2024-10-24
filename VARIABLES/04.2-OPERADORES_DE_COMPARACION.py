'''OPERADORES RELACIONALES
Se utiliza para establecer una relacion entre 2 valores.
Compara estos valores entre si y esta comparacion produce
un resultado de certeza o falsedad (Verdadero(true) o Falso(false)) un Booleano
Tienen el mismo nivel de prioridad en su evaluacion
Los Operadores Relacionales tienen menos prioridad que los Aritmeticos'''
print()
n1=10   
n2=15

#como vemos en el print se pueden solicitar las claves/keys asignados n1, n2 o los valores/values asignados = 10, 15 

print(n1>n2) # es mayor que (ejemplo 10 es mayor > que 15) no false
print(n1<n2) # es menor que (ejemplo 10 es menor < que 15) si true
print(n1>=n2) # es mayor o igual que para que sea true una de las dos condicienes se tiene que cumplir (ejemplo 10 es mayor no o igual no >= que 15) false
print(n1<=n2) # es menor o igual que para que sea true una de las dos condicienes se tiene que cumplir (ejemplo 10 es menor SI o igual no <= que 15) true
print(n1==n1) # es exactamente igual a (ejemplo 10 es exactamente igual a 10) si true
print(n1==15) # es exactamente igual a (ejemplo 10 es exactamente igual a 15) no false
print(n1!=10) # es distinto a (ejemplo 10 es distinto de 10) no false
print(n1!=15) # es distinto a (ejemplo 10 es distinto de 15) si true
print(10>15) # es mayor que (ejemplo 10 es mayor > que 15) no false
print(n1<15) # es menor que (ejemplo 10 es menor < que 15) si true
print(10>=n2) # es mayor o igual que para que sea true una de las dos condicienes se tiene que cumplir (ejemplo 10 es mayor no o igual no >= que 15) false
print(n1<=15) # es menor o igual que para que sea true una de las dos condicienes se tiene que cumplir (ejemplo 10 es menor SI o igual no <= que 15) true
print(10==n1) # es exactamente igual a (ejemplo 10 es exactamente igual a 10) si true
print(10==n2) # es exactamente igual a (ejemplo 10 es exactamente igual a 15) no false
print(10!=n1) # es distinto a (ejemplo 10 es distinto de 10) no false
print(10!=n2) # es distinto a (ejemplo 10 es distinto de 15) si true
print()
# LOS OPERADORES FUNCIONAS ASI "VALOR - OPERADOR - VALOR"
# IMPRIME true o false 
# los operadores comparaciones solo indican si es verdadero o falso 
# EJEMPLOS DE OPERADORES
# == es igual que 
es_igual_que= 5==5
                   # en este ejemplo para que sea falso deberia ser 5==cualquier numero menos el 5
                   
# != es distinto de
es_distinto_de= 5!=6

# <  es menor que
es_menor_que= 5<6

# <= es menor o igual que
es_menor_o_igual_que= 5<=6

# >  es mayor que
es_mayor_que= 5>6

# >= es mayor o igual que
es_mayor_o_igual_que= 5>=6

# RESULTADOS
print(es_igual_que)
print(es_distinto_de)
print(es_menor_que)
print(es_menor_o_igual_que)
print(es_mayor_que)
print(es_mayor_o_igual_que)

#EJERCICIOS
a=5
b=10
c=20
#comparacion=a+b==c     print(comparacion)RESULTADO FALSE
#comparacion=a+b<=c       "        "      RESULTADO TRUE
#comparacion=c-a==a+b     "        "      RESULTADO TRUE
#comparacion=c+b/a!=a*b   "        "  RESULTADO TRUE
contraseña_almacenada="kunymann programador"
contraseña_escrita="kunymann programador"
print(contraseña_almacenada==contraseña_escrita)

resultado= a*2+b==c
print(resultado)

print()

print("*** OPERADORES DE COMPARACION (Relacionales) ***")
a,b=7,5
print(f"Valor inicial de a:{a} y valor de b:{b}")
'OPERADOR DE IGUALDAD =='
print(a==b)#False
#comprobaciones
print(a==7)#True
print(a==5)#False
print(b==a)#False
print(b==5)#True
print(b==7)#False
print()

print("***EJERCICIOS***")
#UTILIZANDO UNA VARIABLE
'OPERADOR DE IGUALDAD =='
resultado=(a==b) #utilizando ya los valores asignados de 7 y 5, los parentesisson opcionales no modifican en nada si no se los coloca
print(f"Preguntamos si a (7) es igual que b (5), el resultado es: {resultado}")#False
print()

'OPERADOR DISTINTO DE !='
resultado=a!=b
print(f"Preguntamos si a (7) es distinto de b (5), el resultado es: {resultado}")#True
print()

'OPERADOR MENOR QUE <'
resultado=a<b
print(f"Preguntamos si a (7) es menor que b (5), el resultado es: {resultado}")#False
print()

'OPERADOR MENOR o IGUAL QUE <=' #Si alguna de las dos condiciones se cumple es True caso contrario sera False
resultado=a<=b
print(f"Preguntamos si a (7) es menor o igual que b (5), el resultado es: {resultado}")#False
print()

'OPERADOR MAYOR QUE >'
resultado=a>b
print(f"Preguntamos si a (7) es mayor que b (5), el resultado es: {resultado}")#True
print()

'OPERADOR MAYOR o IGUAL QUE >=' #Si alguna de las dos condiciones se cumple es True caso contrario sera False
resultado=a>=b
print(f"Preguntamos si a (7) es mayor o igual que b (5), el resultado es: {resultado}")#True
print()
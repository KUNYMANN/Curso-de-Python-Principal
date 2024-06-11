'''OPERADORES RELACIONALES
Se utiliza para establecer una relacion entre 2 valores.
Compara estos valores entre si y esta comparacion produce
un resultado de certeza o falsedad (Verdadero(true) o Falso(false)) un Booleano
Tienen el mismo nivel de prioridad en su evaluacion
Los Operadores Relacionales tienen menos prioridad que los Aritmeticos'''

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
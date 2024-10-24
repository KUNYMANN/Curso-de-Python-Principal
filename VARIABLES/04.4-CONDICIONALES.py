
#LOS CONDICIONALES SON TRES TIPOS DE SENTENCIAS PARA COMPARAR DOS VALORES Y ESA COMPARACION ME VA A DAR COMO RESULTADO UN VALOR LOGICO 
numero=int(input("digite un numero: ")) #aqui le estamos solicitando al usuario que ingrese (input) un numero entero (int)

# if: significa SI, esto quiere decir que si la siguiente condicion se cumple, se van a ejecutar un numero determinado de acciones o no se ejecute nada
if numero>0:     #En la mayoria de los lenguajes de programacion para indicar que todo pertenece al mismo bloque se coloca entre llaves {}
    print("el numero es positivo") #en cambio en python para indicar que todo pertenece al mismo bloque se utiliza la identacion (sangria)
    #esto quiere decir que todas las linea de instrucciones que esten colocadas con la misma sangria en los sucesivos renglones
    # pertenece el mismo bloque, en este caso el condicional if
    """ estos cuatros caracteres antes de las comillas es para mostrar lo que es una identacion, o sangria, o tabulacion
    (se utilizan cuatro espacios vacios a partir del margen)"""


#elif: es para mostrar un condicion intermedia entre la primera condicion(if) y la segunda condicion(else)
elif numero==0:
    print("el numero es cero") #esta instruccion ya no pertenece a la de arriba sino al nuevo condicional, en este caso a elif
    """ estos cuatros caracteres antes de las comillas es para mostrar lo que es una identacion, o sangria, o tabulacion
    (se utilizan cuatro espacios vacios a partir del margen)"""

#else: es una condicion que muestra lo contrario a if 
else:
    print("el numero es negativo") #esta instruccion ya no pertenece a la de arriba sino al nuevo condicional, en este caso a else
    """ estos cuatros caracteres antes de las comillas es para mostrar lo que es una identacion, o sangria, o tabulacion
    (se utilizan cuatro espacios vacios a partir del margen)"""


print("fin del programa") #esta instruccion sin la sangria significa que esta fuera de las instrucciones de los condicionales anteriores que 
#si tenia sangria o identacion y se va a imprimir siempre
print()

'OPERADORES CONDICIONALES: se utilizan para comparar valores'
#el resultado siempre es un valor booleano "True" o "False", dependiendo de si la condicion se cumple o no
'Operadores de igualdad (==) compara si dos valores son exactamente iguales'
# a=b
#Ejemplo
print(5==5)#True
print(5.0==5) #True
print(5==8) #False
print()

'Operadores "distinto de" o "no es igual a" (!=)  compara si dos valores son distintos'
# c!=d 
#Ejemplo
print(5!=5)#False
print(5!=8)#True
print()

'''Operador de menor que (<): compara si el valor de la izquierda es menor que el de la derecha
si es menor devuelve True y si no lo es devuelve False'''
#a<b
print(5<5)#False (porque el numero es igual pero no menor)
print(5<8)#True
print()

'''Operador de "menor o igual que" (<=): verifica si el valor de la izquierda es menor o igual que el de la derecha
si estas condicion se cumple devuelve True caso contrario devuelve False'''
#a<b
print(5<=5)#True
print(5<=8) #True
print(5<=2)#False
print()

'''Operador de mayor que (>): compara si el valor de la izquierda es mayor que el de la derecha
si es mayor devuelve True y si no lo es devuelve False'''
#a>b
print(5>5)#False (porque el numero es igual pero no mayor)
print(5>8)#False
print(8>5)#True
print()

'''Operador de "mayor o igual que" (>=): verifica si el valor de la izquierda es mayor o igual que el de la derecha
si estas condicion se cumple devuelve True caso contrario devuelve False'''
#a>b
print(5>=5)#True
print(5>=8) #False
print(5>=2)#True
print()
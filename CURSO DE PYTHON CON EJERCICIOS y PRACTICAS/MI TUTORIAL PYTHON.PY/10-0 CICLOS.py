'''
Los ciclos en Python son estructuras de control que repiten una serie de instrucciones hasta que se
cumple una condición específica.
En Python tenemos dos tipos de estructuras para ejecutar ciclos el "ciclo while" y el "ciclo for".
Vamos a comenzar con el ciclo while.
El ciclo while repite una serie de instrucciones mientras la condición a evaluar es verdadera y podemos
observar la sintaxis del ciclo while.
Vamos a utilizar la palabra reservada while en minúsculas.
Posteriormente dejamos este espacio y agregamos posteriormente una condición.
Posteriormente tenemos dos puntos y se agrega el bloque de código a ejecutar.
Este bloque de código se va a repetir tantas veces como esta condición sea verdadera y se va a detener
hasta que la condición sea falsa.'''

#ejemplo ciclo while
contador=1
while contador<=5:
    print(contador)
    contador+=1

'''DIAGRAMA DE FLUJO'''

#                    O-------inicio
#                    |
#                contador = 1
#volvemos a          |             mientras el contador va corroborando y de la evaluacion surge que el valor resultante es un numero menor o igual a tres sera True
#  evaluar           |             
#           -- contador <=3 --------
#           |        |           False
#           | True   |             |
#           |        |             |  en cambio si al evaluar el contador arroja un numero mayor a tres sera False y terminara ahi el ciclo de busqueda
#           | print (contador)     |
#           |        |             |
#           |    contador +=1      |
#           |________|             |
#                                  |
#                  ________________|
#                  |  
#                 fin
''' vamos a ver el paso a paso.

Si ejecutamos paso a paso este ejercicio, entonces la primera vez que lo ejecutamos se define la variable de contador con el valor de uno.
Posteriormente, como hemos comentado, se revisa la condición.En este caso la condición que se va a evaluar es la siguiente.
El valor de la variable de contador vale uno y la condición que se va a evaluar es uno menor o igual que tres.
Esta condición es verdadera, por lo tanto entramos al bloque de código del ciclo while, se imprime la variable de contador y a consola.
Podemos observar que se manda a imprimir el valor de uno.Es la primera vez que se manda a imprimir esta información a consola.
Posteriormente se incrementa la variable de contador para evitar ciclos infinitos, así que se incrementa
la variable de contador y podemos observar que ya no vale uno sino en este momento ya vale dos y se vuelve a repetir nuestro ciclo.
Volvemos a evaluar nuestra condición.
Entonces, en esta segunda iteración, la variable de contador ya vale dos y entonces revisamos la condición.
En este caso la nueva condición es dos menor, igual que tres. En este caso todavía regresa verdadero.
Por lo tanto, volvemos a entrar al ciclo while, entramos al bloque de código, se manda a imprimir
la variable de contador y entonces a consola.
Ya podemos observar el valor de uno y también ahora el valor de dos.
Se incrementa la variable de contador y entonces la variable de contador ya no vale dos, sino que en
este momento ya vale tres y se repite nuestro ciclo.
Volvemos a evaluar nuestra condición Ahora, para esta nueva iteración, entonces la variable de contador tiene el valor de tres.
Por lo tanto, la condición que vamos a evaluar es si tres es menor o igual que tres.
Esto regresa todavía verdadero ya que se está incluyendo el límite tres.
Por ello es menor o igual, así que regresa verdadero.
Entramos a la ejecución del ciclo while, se ejecuta nuestro bloque de código, se manda a imprimir la variable de contador y entonces la salida.
Ya tenemos ahora también el valor de tres.
Ya podemos observar completa la salida con los valores del uno al tres y va a ser la última vez que se va a ejecutar este ciclo.
Pero la variable de contador ya tiene el valor de cuatro.
Por lo tanto, si revisamos la condición, podemos observar que en este caso cuatro no es menor o igual
que tres, por lo tanto esta condición regresa falso y termina la ejecución de nuestro programa.'''
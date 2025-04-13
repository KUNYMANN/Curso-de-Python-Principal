'''Vamos a sumar el valor de uno más dos más tres más cuatro más cinco para finalmente obtener el valor de 15. 
Sin embargo, vamos a utilizar un ciclo while para realizar esta suma. Por ello se conoce como una suma iterativa o una suma acumulativa.'''

#Vamos a realizar el siguiente ejercicio de ACUMULADOR SUMA o SUMA ITERATIVA.
#También se conoce como suma iterativa y se pide lo siguiente.
#Realizar la suma de los primeros cinco números utilizando un ciclo while
print('***Suma ACUMULATIVA***')

#estas son las variables que creamos para utilizar
maximo=10  # (1) definimos esta variable para saber hasta que numero va a iterar, podria ser cualquier número
numero=1  # (2) definimos esta variable para saber cual sera el punto de partida de la iteración, puede variar dependiendo de lo que querramos (1,2,3, etc)
acumulador_suma=0 # esta va a guardar el valor de la suma acululada por cada iteración hasta que termine de evaluar la funcion while
print()

#este es el modo de ejecución del programa con la función while
while numero<=maximo: #primeramnte partimos de la variable (2) que tiene que ser menor o igual al maximo ingresado en la variable (1) definida con anterioridad
    print(f'(acumulador_suma + numero) -> {acumulador_suma} + {numero}') # (*) de esta manera mostramos lo que se imprime por consola a medida  
                                                                         #que se va realizando la suma acumulada
    acumulador_suma+=numero # este es el nucleo principal de la operacion que va a ejecutar los pasos de la suma siguiendo los parametros ingresados
    numero+=2 # (**) de esta manera indicamos que del valor de inicio salte cada dos números para realizar la suma, puede ser de uno en uno, de tres en tres, etc.  
  
   #(*) y(**)       #(acumulador_suma + numero) -> 0 + 2
                      #suma pacial acumulada 2
                    #(acumulador_suma + numero) -> 2 + 4
                      #suma pacial acumulada 6
                    #(acumulador_suma + numero) -> 6 + 6
                      #suma pacial acumulada 12
                    #(acumulador_suma + numero) -> 12 + 8
                      #suma pacial acumulada 20
                    #(acumulador_suma + numero) -> 20 + 10
                      #suma pacial acumulada 30
                               
    print(f'suma pacial acumulada {acumulador_suma}\n') #si coloco el print a la altura de la variable me va a dar el paso a paso de la suma acumulada (1º+2º=3+3º=6+4º=10+5º=15)
                                    #el simbolo º es solo para identificar a los numeros que se van sumando deacuerdo a la iteración
   
print(acumulador_suma) #si coloco el print al inicio del renglon me va a dar el resultado final de la suma acumulada
                       #me imprimiria por consola "30" que es el resutado para este caso
   

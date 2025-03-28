'''Vamos a sumar el valor de uno más dos más tres más cuatro más cinco para finalmente obtener el valor de 15. 
Sin embargo, vamos a utilizar un ciclo while para realizar esta suma. Por ello se conoce como una suma iterativa o una suma acumulativa.'''

#Vamos a realizar el siguiente ejercicio de ACUMULADOR SUMA.
#También se conoce como suma iterativa y se pide lo siguiente.
#Realizar la suma de los primeros cinco números utilizando un ciclo while
print('***Suma ACUMULATIVA***')

#estas son las variables que creamos para utilizar
maximo=5  #definimos esta variable para saber hasta que numero va a iterar, podria ser cualquier numero
numero=1  #definimos esta variable para saber cual sera el punto de partida de la iteración
acumulador_suma=0
print()
#este es ya el modo de ejecucion del programa
while numero<=maximo:
    print(f'(acumulador_suma + numero) -> {acumulador_suma} + {numero}')
    acumulador_suma+=numero
    numero+=1

  
    print(f'suma pacial acumulada {acumulador_suma}\n') #si coloco el print a la altura de la variable me va a dar el paso a paso de la suma acumulada (1º+2º=3+3º=6+4º=10+5º=15)
                                    #el simbolo º es solo para identificar a los numeros que se van sumando deacuerdo a la iteración
   
print(acumulador_suma) #si coloco el print al inicio del renglon me va a dar el resultado final de la suma acumulada'''

   

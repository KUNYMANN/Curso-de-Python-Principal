#HOLA KUNYMANN
#Ejercicio 1
'''Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.'''
print('hola Mundo')

#Ejercicio 2
'''Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable
 y luego muestre por pantalla el contenido de la variable.'''
a=('Hola KUNY')
print(a)

#Ejercicio 3
'''Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca 
muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.'''
nombre=str(input('Coloque su nombre por favor: ' )).upper()
print("Hola", nombre,"sos un CRACK !!!")

#Ejercicio 4
'''Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética'''
operacion=((3+2)/(5*2))**2
print("El resuktado es: ", operacion)

#Ejercicio 5
'''Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.'''
horas=float(input("Coloque la cantidad de horas trabajadas: "))
precio_de_la_hora=float(input("Coloque el valor de cada hora: "))
sueldo=horas*precio_de_la_hora
print(f"Total a cobrar por las horas trabajadas: {sueldo:.2f}")

#Ejercicio 6
'''Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta . 
La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
suma=(n*(n+1))/2'''
n=int(input("Coloque un numero: "))
suma=(n*(n+1))/2
print("La suma de los numeros positivos hasta el numero ingresado es: ", suma)

#Ejercicio 7
'''Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.'''
peso=float(input("Coloque aqui su peso: "))
altura=float(input("Coloque aqui su altura: "))
imc=peso/(altura**2) # calculo para el indice de masa corporal (imc)
print(f"Tu indice de masa corporal es de: {imc:.2f}")# mas de 30 es conciderado obeso'''

#Ejercicio 8
'''Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> 
son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.'''
n=int(input("ingrese un numero dividendo: "))
m=int(input("ingrese un numero divisor: "))
division=int (n/m)
resto=(n%m)
print(n,"dividido por",m,"da un cociente de", division,"y cuyo resto es", resto)
'''Otra manera de expresarlo'''
n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))

#Ejercicio 9
capital=float(input("Dinero que desea invertir: "))
interes=float(input("Coloque la tasa de interes anual: "))
tiempo=int(input("Coloque la cantidad de dias que va durar la inversion: "))
interes_decimal=interes/100
total=capital*(1+interes_decimal)**(tiempo/365)
print(f"El monto final a cobrar de la inversion mas el interes es de $:  {total:.2f}")

capital=float(input("Dinero que desea invertir: "))
interes=float(input("Coloque la tasa de interes anual: "))
tiempo=int(input("Coloque la cantidad de meses que va durar la inversion: "))
interes_decimal=interes/100
total=capital*(1+interes_decimal)**(tiempo/12)
print(f"El monto final a cobrar de la inversion mas el interes es de $:  {total:.2f}")

capital=float(input("Dinero que desea invertir: "))
interes=float(input("Coloque la tasa de interes anual: "))
tiempo=int(input("Coloque la cantidad de años que va durar la inversion: "))
interes_decimal=interes/100
total=capital*(1+interes_decimal)**tiempo
print(f"El monto final a cobrar de la inversion mas el interes es de $:  {total:.2f}")

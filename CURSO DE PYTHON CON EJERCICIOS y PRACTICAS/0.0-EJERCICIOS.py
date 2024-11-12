#HOLA KUNYMANN
#Ejercicio 1 
'''Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print('hola Mundo')'''

#Ejercicio 2
'''Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable
 y luego muestre por pantalla el contenido de la variable.
a=('Hola KUNY')
print(a)'''

#Ejercicio 3
'''Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca 
muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
nombre=str(input('Coloque su nombre por favor: ' )).upper()
print("Hola", nombre,"sos un CRACK !!!")'''

#Ejercicio 4
'''Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética
operacion=((3+2)/(5*2))**2
print("El resuktado es: ", operacion)'''

#Ejercicio 5
'''Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.
horas=float(input("Coloque la cantidad de horas trabajadas: "))
precio_de_la_hora=float(input("Coloque el valor de cada hora: "))
sueldo=horas*precio_de_la_hora
print(f"Total a cobrar por las horas trabajadas: {sueldo:.2f}")'''

#Ejercicio 6
'''Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta . 
La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
suma=(n*(n+1))/2
n=int(input("Coloque un numero: "))
suma=(n*(n+1))/2
print("La suma de los numeros positivos hasta el numero ingresado es: ", suma)'''

#Ejercicio 7
'''Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
peso=float(input("Coloque aqui su peso: "))
altura=float(input("Coloque aqui su altura: "))
imc=peso/(altura**2) # calculo para el indice de masa corporal (imc)
print(f"Tu indice de masa corporal es de: {imc:.2f}")# mas de 30 es conciderado obeso '''

#Ejercicio 8
'''Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> 
son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
n=int(input("ingrese un numero dividendo: "))
m=int(input("ingrese un numero divisor: "))
division=int (n/m)
resto=(n%m)
print(n,"dividido por",m,"da un cociente de", division,"y cuyo resto es", resto)
Otra manera de expresarlo
n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))'''

#Ejercicio 9
'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión.
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
# Solicitar datos al usuario
cantidad_invertir = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (en porcentaje): "))
años = int(input("Introduce el número de años: "))

# Convertir el interés anual de porcentaje a decimal
interes_anual_decimal = interes_anual / 100

# Calcular el capital obtenido usando la fórmula del interés compuesto
capital_obtenido = cantidad_invertir * (1 + interes_anual_decimal) ** años

# Mostrar el resultado
print(f"El capital obtenido en la inversión después de {años} años es: {capital_obtenido:.2f}")

# Solicitar datos al usuario
cantidad_invertir = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (en porcentaje): "))
meses = int(input("Introduce el número de meses: "))

# Convertir el interés anual de porcentaje a decimal y luego a interés mensual
interes_mensual_decimal = (interes_anual / 100) / 12

# Calcular el capital obtenido usando la fórmula del interés compuesto mensual
capital_obtenido = cantidad_invertir * (1 + interes_mensual_decimal) ** meses

# Mostrar el resultado
print(f"El capital obtenido en la inversión después de {meses} meses es: {capital_obtenido:.2f}'''

#Ejercicio 10
'''Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido
 y calcule el peso total del paquete que será enviado.

payaso=int(input("Igrese la cantidad de payasos que desea recibir en este envio: "))
muñeca=int(input("Igrese la cantidad de muñecas que desea recibir en este envio: "))
peso_payasos=(112*payaso)
peso_muñecas=(75*muñeca)
peso_total=peso_payasos+peso_muñecas
print(f"El peso total del envio es de: {peso_total}")'''

#Ejercicio 11
'''Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
Redondear cada cantidad a dos decimales.
dinero_inversion=float(input("Importe de la invercion $ "))
interes_anual=4/100
interes_acumulado=1+4/100
ahorro1=dinero_inversion*(interes_acumulado)
ahorro2=ahorro1*(interes_acumulado)
ahorro3=ahorro2*(interes_acumulado)
print(f"el interes mensual es de {interes_anual:.2f}")
print(F"Ahorro obtenidos balance 1er año es $ {ahorro1:.2f}")
print(F"Ahorro obtenidos balance 2do año es $ {ahorro2:.2f}")
print(F"Ahorro obtenidos balance 3er año es $ {ahorro3:.2f}")'''

#Ejercicio 12
'''pan=int(input("Ingrese la cantidad de barras de pan del dia: "))
pan2=int(input("Ingrese la cantidad de barras de pan que no es del dia: "))
precio=3.49
descuento=precio-(precio*(60/100))
descontable=60
pan_del_dia=3.49*pan
pan_viejo=descuento*pan2
total_compra=pan_del_dia+pan_viejo

print(f"El precio del pan del dia es $ {precio:.2f}")
print(f"el descuento por no ser pan del dia es {descontable}%")
print(f"El precio del pan con descuento por no ser del dia $ {descuento:.2f} ")
print(f"total compra de pan del dia $ {pan_del_dia:.2f}")
print(f"total compra de pan por no ser del dia $ {pan_viejo:.2f}")
print(f"El total final de la compra $ {total_compra:.2f}")'''

#Calcular el area y el primetro de un rectangulo
base=float(input('Ingrese el valor de la base del rectangulo: '))
altura=float(input("Ingrese el valor de la altura del rectangulo: "))

area=base*altura
perimetro=2*(base+altura)
print(f'El area del rectangulo es: {area}')
print(f'el perimetro del rectangulo es: {perimetro}')
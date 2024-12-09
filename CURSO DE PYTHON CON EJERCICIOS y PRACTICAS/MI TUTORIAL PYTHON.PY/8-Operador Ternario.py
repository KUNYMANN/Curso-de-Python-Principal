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
'''edad=float(input("Ingrese su edad: "))
es_adulto="Si" if edad>=18 else "No"# Estamos evaluando que: si la edad es mayor o igual a 18 imprima Si(Verdadero) caso contrario que imprima No 
print(f"Es usted adulto? {es_adulto}") #la evaluacion siempre se hace de izquierda a derecha'''
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
'''print()
nombre_de_usuario=input("Ingrese su nombre de usuario: ").strip().upper()
pasos=int(input("Ingrese la cantidad de pasos realizados en el dia: "))
print()
print(f"Su nombre de usuario es: {nombre_de_usuario}")
print(f"La cantidad de pasos ingresados es: {pasos}")
meta_pasos_diarios=10000
print(f"La meta de pasos diarios es de: {meta_pasos_diarios}")
calorias_por_paso=0.04
calorias_quemadas=pasos*calorias_por_paso
print(f"Tus calorias quemadas fueron de: {calorias_quemadas:.2F} kcal.")
meta_alcanzada=pasos>=meta_pasos_diarios
objetivo="Si"if pasos>=10000 else "No"
print(f"Has alcanzado tu meta? {objetivo}")
print()'''

'''sistema de reserva de hotel.

Se les pide realizar lo siguiente.Se solicita crear un sistema de reservación de un hotel y se debe de pedir la siguiente información
al usuario.En primer lugar le van a pedir el nombre del cliente.
Posteriormente los días de estadía en el hotel cuántos días se va a quedar en el hotel?
Y también van a preguntar si quiere 1/4 con vista al mar.Ahora el hotel tiene las siguientes tarifas.
1/4 sin vista al mar tiene un costo de 150.50 por día y 1/4 con vista al mar.
Tiene el costo de 190.50 por día y el sistema debe de calcular el costo total de la estadía dependiendo
si escogió 1/4 con vista al mar o no, y además también debe de indicar si escogió 1/4 con vista al
mar o no.Vamos a ver el resultado de ejecutar nuestra aplicación.
Se muestra el título Sistema de reserva de hotel.
Nos pide un nombre, por ejemplo Juan Carlos, los días de estadía, por ejemplo cinco días, y nos
pregunta si queremos el 4.º con vista al mar.
En ese caso le decimos que sí y podemos observar los detalles de la reservación.
Así lo tiene que mandar a imprimir el cliente es Juan Carlos.
Los días de estadía cinco y el costo total tiene que ser de 952.50.
Y también comenta que la habitación si fue con vista al mar.
Ahora si volvemos a ejecutar, por ejemplo, el nombre del cliente Susana, el número de días que se
va a quedar, por ejemplo, solamente tres días y en este caso el 4.º no debe de incluir vista al mar
y tenemos el detalle de la reservación.
El cliente Susana.
Los días de estadía tres El costo total de la reservación 451.50 y también indica que el 4.º no tiene
vista al mar, así que eso es lo que debe de realizar su aplicación.'''


print("    ***SISTEMA RESERVA HOTEL***")

precio1=200
precio2=150

print(f"Cuartos con vista al mar $ {precio1} por dia")
print(f"Cuartos sin vista al mar $ {precio2} por dia")
print()
nombre_completo_pasajero=input("Ingrese su nombre y apellido completo: ").strip().title()
dias_en_el_hotel=int(input("Indique la cantidad de dias que va a alojarse en el hotel: "))
cuartos_con_vista_al_mar=input("Desea un cuarto con vista al mar? (Si/No): ").strip().lower()
efectivo_debito=input("Si abona en efectivo/debito obterndra un descuento 10% (Si/No): ").strip().lower()
print("\n----------Detalles de la reserva-----------")

#mas de 20 dias, Hab.C V Mar,pago en efectivo
if dias_en_el_hotel>=20 and cuartos_con_vista_al_mar=="si":    
   descuento1=precio1*0.80
   valor_promocion1=descuento1*dias_en_el_hotel
   if efectivo_debito=="si": 
    pago_efectivo=valor_promocion1*0.90
    print(f""""Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de dias de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitacion con vista al mar: {cuartos_con_vista_al_mar}
Promocion otorgada de un descuento de $ {descuento1} por 20 dias o mas.../
El total de su reserva por los {dias_en_el_hotel} dias es $ {valor_promocion1} 
Si abona en efectivo la suma final a pagar es {pago_efectivo}""")

#mas de 20 dias, Hab.C V Mar,paga con otro medio  
   if efectivo_debito=="no": 
    print(f""""Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de dias de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitacion con vista al mar: {cuartos_con_vista_al_mar}
Promocion otorgada de un descuento de $ {descuento1} por 20 dias o mas...//
El total de su reserva por los {dias_en_el_hotel} dias es $ {valor_promocion1}""")

#menos de 20 dias, Hab.C V Mar,pago en efectivo    

    if efectivo_debito=="no": 
     valor_s_promocion=precio1*dias_en_el_hotel
     print(f""""Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de dias de su reserva es: {dias_en_el_hotel}
**Solicito reserva para una habitacion con vista al mar: {cuartos_con_vista_al_mar}
El total de su reserva por los {dias_en_el_hotel} dias es $ {valor_s_promocion}""")

#mas de 20 dias, Hab.sin V Mar,pago en efectivo
if dias_en_el_hotel>=20 and cuartos_con_vista_al_mar=="no":
  descuento2=precio2*0.80
  valor_promocion2=descuento2*dias_en_el_hotel
  if efectivo_debito=="si": 
      pago_efectivo=valor_promocion2*0.90
      print(f""""Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de dias de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitacion con vista al mar: {cuartos_con_vista_al_mar}
Promocion otorgada de un descuento de $ {descuento2} por 20 dias o mas ***/
El total de su reserva por los {dias_en_el_hotel} dias es $ {valor_promocion2}
Si abona en efectivo la suma final a pagar es {pago_efectivo}""") 

#mas de 20 dias, Hab.sin V Mar,paga con otro medio
if dias_en_el_hotel>=20 and cuartos_con_vista_al_mar=="no":
     descuento2=precio2*0.80
     valor_promocion2=descuento2*dias_en_el_hotel
     print(f""""Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de dias de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitacion con vista al mar: {cuartos_con_vista_al_mar}
Promocion otorgada de un descuento de $ {descuento2} por 20 dias o mas ***//
El total de su reserva por los {dias_en_el_hotel} dias es $ {valor_promocion2}""") 
      
#menos de 20 dias, Hab.sin V Mar,pago en efectivo
if dias_en_el_hotel<20 and cuartos_con_vista_al_mar=="no":
     descuento2=precio2*0.80
     valor_promocion2=descuento2*dias_en_el_hotel
     pago_efectivo=valor_promocion2*0.90
     if efectivo_debito=="si": 
      print(f""""Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de dias de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitacion con vista al mar: {cuartos_con_vista_al_mar}
Promocion otorgada de un descuento de $ {descuento2} por 20 dias o mas ***
El total de su reserva por los {dias_en_el_hotel} dias es $ {valor_promocion2}
Si abona en efectivo la suma final a pagar es {pago_efectivo}""") 

#menos de 20 dias, hab.sin V Mar, paga con otro medio 
else:
  efectivo_debito=="no"
  print(f"""Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de días de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitación con vista al mar: {cuartos_con_vista_al_mar}
El total de su reserva por los {dias_en_el_hotel} días es $ {precio2 * dias_en_el_hotel}""")













'''else:

  print(f"""Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de dias de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitacion con vista al mar: {cuartos_con_vista_al_mar}
El total de su reserva por los {dias_en_el_hotel} dias es $ {precio2*dias_en_el_hotel}""")'''

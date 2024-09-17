#1
# "Hoy es un dia para programas" correcto
# 'El dia esta nublado" incorrecto
# '¿Que dia es hoy?' correcto
# "Mañana, en inglés se dice"morning"" incorrecto

#2
#El tipo de error que devuelve un string mal escrito es un SyntaxError (error de sintaxis)
'''
#3
#imprimir por consola la cantidad de caracteres de la palabra "automaticamente" 
palabra="automáticamente"
print(len(palabra)) # la funcion len es para contar la catidad de caracteres 

#4
#Mostrar en consola solo el caracter de la "á" mediante la posicion del string
palabra1="automáticamente"
print(palabra1[5]) #colocando entre corchetes el numero de indice a partir del 0 nos dira que caracter se aloja en ese indice
print(palabra1.find("á")) #la funcion find es para ubicar un caracter en especial dentro de un texto o palabra y nos dice en que indice se encuentra

#5
#Realizar 10 elevado a la 5 con el operador exponente
operacion_exponencial=10**5
print(operacion_exponencial)
#aqui optra manera
operacion=10
operacion **=5
print(operacion)

#6
#aqui sin la funcion exponente
operacion2=10*10*10*10*10
print(operacion2)

#7
#En que dos estados puede estar un dato booleano
#en True o en False

#8 
#Mostrar que tipo de dato tiene esta variable
nunm1=675.87
print(type(nunm1))

#9 
#LEN solo funciona con string NO con numeros
#mostrar la cantidad de digitos de una variable, utilizando la funcion len
variable=768763843
print(len(str(variable))) #primero hay que volver un string al numero de la variable para despues pedir un len

#10 convertir en enteros estos datos float mediante tipos y sumalos
numx="14.527"
numv="560.92"
numr=float(numx)
nums=float(numv)
print(int(numr)+int(nums))

#11
#Redondear estos numeros con la cantidad de decimales indicada en los comentarion e imprimelos en la consola
numer1=10.897654876534  #3 decimales
numer2=7674.7886 #2 decimales
numer3=68754.78 #un decimal
print(round(numer1,3)) #con la funcion round (redondeo)
print(round(numer2,2))
print(round(numer3,1))

print(f"{numer1:.3f}") #con la funcion f (format)
print(f"{numer2:.2f}")
print(f"{numer3:.1f}")

#12
#cual es la diferencia entre el operador modulo y el floor division
#el operador modulo devuelve el resto de una division y el floor devuelve el resultado de la operacion un numero sin decimales (int)

#13
#asigna con los operadores de asignacion los siguientes valores indicados
valor=10        #  +60
valor1=24       # -100
valor2=65.67    #   +4.33
valor+=60
valor1-=100
valor2+=4.33
print(valor)
print(valor1)
print(valor2)

#14
#Mediante la tecnica de formateo de string muestra literalmente estos calores en una
#frase en el print sin utilizar la concatenacion 
nu1=4
nu2=769.97
tex="ai i a string"
decision=True
inicio="VALOR"
decorado="es bastante mas grande que"
relleno="the answer is"

print(f"El {inicio.lower()} {nu2} {decorado.capitalize()} {nu1}. ¿{tex.title()}? {relleno.upper()} {decision}")

#15 
#Armar una calculadora de exponente
print("\tCALCULADORA EXPONENCIAL")
numero_ingresado=int(input("Coloque el numero que desee exponenciar: \n"))
exponente=int(input("Coloque el numero al que quiere elevarlo: \n"))
resultado=(int(numero_ingresado))**(int(exponente))
print(f"El resultado de la operacion es: {resultado}") '''
print()




cliente=input("Coloque su nombre: ")
dias_estadia=input("Cuantos dias desea alojarse: ")
tarifa_diaria= 1200
Respuesta=input("Desea que la habitacion tenga vista al mar: ")

if Respuesta=="si":
    VAR=True
else:
    VAR=False

if Respuesta=="si":
    Respuesta="True"
else:
    Respuesta="False"



print("\t*** Sistema de Reserva de Hotel***")
print("Nombre de la reserva: ",cliente)
print("Cantidad de dias alojado: ",dias_estadia)
print("Precio por dia $: ",tarifa_diaria)
print("Usted reservo una habitacion con vista al mar: ",VAR)
print("Usted reservo una habitacion con vista al mar: ",Respuesta)



Producto="Camara Digital"
Precio=399.99
Stock=20
Disponible=True

print("\t***Sistema Tienda Online***")
print("Producto: ",Producto)
print("Precio : $",Precio)
print("Cantidad en el Inventario: ", Stock)
print("Disponible para entrega: ",Disponible)

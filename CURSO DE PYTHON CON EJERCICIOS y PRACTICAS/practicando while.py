"""¿Cómo empezar a resolverlos?
Lee el enunciado cuidadosamente: Antes de empezar a escribir código, asegúrate de entender bien lo que pide el ejercicio.
Piensa en la lógica: Piensa cómo se puede resolver el problema paso a paso. Si tienes que contar algo, qué valor deberías incrementar, 
o si tienes que comparar algo, cómo puedes hacerlo.
Escribe poco a poco: Ve resolviendo los ejercicios en partes. Si te atoras en un ejercicio, trata de simplificarlo o pregunta si no entiendes algo.
Prueba y corrige: Ejecuta tu código y verifica que hace lo que esperas. Si algo no funciona, prueba encontrar el error y corregirlo."""

#programa que le pregunte al usuario si quiere sumar dos números, y se repita hasta que diga que no.
'''
print("***SUMA DE DOS NUMEROS***")
print("Vamos a sumar dos numeros")
salir=False
while not salir:
    numero1=float(input("Ingrese un numero: "))
    numero2=float(input("Ingrese otro numero: "))
    suma=numero1+numero2
    print(f"El resultado de la suma es: {suma}")
    respuesta=input("Desea sumar otros dos numeros (Si/No): ").title()
    if respuesta=="No":
        print("Gracias por utilizar el programa")
        salir=True

#1. Contar del 1 al 10 Instrucciones: Escribe un programa que use while para imprimir los números del 1 al 10.
numero=1
while numero<=10:
     print(numero)
     numero+=1
  '''
print()
'''
#Pide al usuario que "ingrese números positivos" y "los sume". El bucle debe seguir pidiendo números hasta que el usuario ingrese 
# un número negativo o cero. "Al final, muestra la suma total".      
  
'estas son las variables que necesito'
suma = 0  # 1º necesitamos esta variable como parametro de inicio, empezamos con la suma en 0 
numero = int(input("Ingresá un número positivo (0 o negativo para salir): ")) # 2º esta variable es medio por el cual solicito al usuario que "ingrese números positivos" 

'este es el desarrollo del ciclo'
while numero > 0: # 1º de esta manera nos aseguramos que el numero ingresado tiene que ser positivo para continuar con el ciclo
    suma += numero  # 2º de esta manerta se van acumulando los numero y a su ves los va sumando
    numero = int(input("Ingresá otro número positivo (0 o negativo para salir): "))# 3º volvemos a aseguramos que el numero ingresado sea positivo 
                                                                                   # caso contrario finaliza el ciclo

'en caso de colocar 0 o un numero negativo antes de salir imprime el ultimo dato que se solicitaba en el ejercicio'
print("La suma total de los números ingresados es:", suma) # ultimo paso de esta manera mostramos al final la suma total '''

"""Contar cuántas veces se repite una palabra
'Pide al usuario que ingrese una palabra'. El programa debe preguntar por una nueva palabra cada vez. 
El bucle debe continuar hasta que el usuario ingrese la palabra "salir".
Al final, muestra cuántas palabras ingresó el usuario (sin contar "salir").

suma_palabras=0
palabra=input("Ingrese una palabra: ").strip().lower() #Pide al usuario que ingrese una palabra

while palabra!="salir":
    suma_palabras+=1
    palabra=input("Ingrese otra palabra o salir para abandonar el programa: ").strip().lower()
print(f"La suma total de palabras ingresadas es: {suma_palabras}")"""



#COMO DISTINGUIR SI EL DATO ES UN NUMERO O UNA LETRA PARA LA EJECICION DE UN PROGRAMA QUE PIDE AMBOS DATOS con la funcion isdigit()
'''Suma de números (NUMEROS) hasta que se ingrese la palabra "fin" (LETRAS)
El programa debe pedir al usuario que ingrese números uno por uno. Cuando el usuario escriba "fin", 
el programa termina y muestra la suma total de los números ingresados.'''

#FORMA FACIL
entrada=input("Ingrese un numero o la palabra fin para salir: ")# en la pregunta debo identificar claramente que quiero que el usuario ingrese
                                      #pero yo tengo que tener en cuenta el dato que este ingresa para saber que hacer sea un numero o letra o una palabra 
                                      #i tendre que ver que herramientas de codigo conozco para darle el uso correcto al dato ingresado
suma=0
while  entrada!="fin":
    numero=int(entrada) 
    suma+=numero
    entrada=input("Ingrese otro numero (o fin si desea salir): ")

print(f"la suma total de los numeros ingresados es: {suma}")

print()

#FORMA IDEAL
entrada=input("Ingrese un numero o la palabra fin para salir: ")
while entrada.lower()!= "fin":
    if entrada.isdigit():          # con esta funcion isdigit() se evalua si el dato ingresado es un numero o una letra
           suma+=int(entrada)      # se arma asi la estructura para que aquello que sea numero forme parte de la suma caso contrario si es letra no
    #si el usuario ingresa una letra que no sea la asignada como cierre del bucle se le debe avisar y se hace de la manera que se muestra a continuacion
    else:
         print("No es un numero valido") 
    entrada=input("Ingrese otro numero o la palabra fin para salir: ")
    #este bucle se seguira repitiendo hasta que el usuario  ingrese la palabra fin, y es ahi que termina el ciclo e imprime la ultima consigna del programa
print(f"La suma total de los numeros ingresados es: {suma}")
    

print()
#el programa debe tener un número secreto (puede estar fijo, como 7).
#El usuario debe adivinarlo. Si falla, el programa debe pedir otro intento hasta que acierte.

'''
numero_secreto=7
numero=int(input("ingrese el numero secreto:" ))
while numero!=numero_secreto:
      print("ERROR")
      numero=int(input("ingrese el numero secreto:" ))
print("Felicitaciones ese es el numero secreto")
'''
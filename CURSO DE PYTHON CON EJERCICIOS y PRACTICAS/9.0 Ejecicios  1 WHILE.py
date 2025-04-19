#EJEMPLO DE UN BUCLE AUTOMATIZADO DE WHILE
'''Carrera de vehiculos a 10 vueltas'''

#primero debemos crear una variable que contenga un dato inicial
vueltas=0 #indicamos el numero de partida de vueltas de la carrera (puede ser cero si es del inicio, o tambien podemos partir de la vuelta 2 o 3 o 10 inclusive
           # no el 11 porque ya habria finalizado, dado que la carrera termina en la vuelta 10)
#luego 
while             vueltas <= 10: #indica cuando finaliza la carrera
#mientras que ....la cantidad de vueltas no supere el numero indicado seguira, girando hasta completar la cantidad de giros indicadas como tope
    print(f"Vuelta Nº:{vueltas}") #mostrara la cantidad de veces que pase por el punto de inicio
    vueltas+=2 # indficamos en este codigo cada cuantas vueltas debe mostrar el print (puede ser en todas las vueltas o sea de 1 en 1 o del numero que querramos
               #en este caso elegi de 2 en 2)

#ESTE EJEMPLO ES CUANDO SE SOLICITA LA INTERACCION DE UN TERCERO
"""Un mini programa que le pide al usuario que adivine una contraseña secreta.
Y no se termina hasta que la adivine.
¿Qué queremos lograr?

    El programa tiene una contraseña secreta.

    Le pide al usuario que adivine.

    Mientras el usuario no escriba la contraseña correcta, le sigue preguntando.

    Cuando la adivina, el bucle se termina y le dice "¡Correcto!"."""


contraseña_secreta = "gato123"
intento = ""

while intento != contraseña_secreta:
    intento = input("Adivina la contraseña: ")

print("¡Correcto! La contraseña era", contraseña_secreta)   

print()

# de ahi que se tenga que crear una variable que refleje esa interacciòn
contraseña_secreta= "HEZ" #dato a identificar
#interaccion con un tercero
contraseña_ingresada="" #variable donde se almacenan los intentos ingresados por el tercero
#desarrollo de lo que quiero que el programa realice con los datos almacenados e ingresados
while contraseña_secreta!=contraseña_ingresada:
#mientras que contr. ingres sea distinta de contr.secr se sigue solicitando que vuelva a intentar el ingreso 
    contraseña_ingresada=input("Ingrese su clave de ingreso: ")
#si la contraseña ingresada coincide con la contraseña secreta se va a imprimir
print("Ingreso exitoso")


print()


palabra=input('Ingrese una palabra: ')
saludo='Hola'
while palabra!=saludo:
      print('Palabra erronea')
      palabra=input("Ingresa de nuevo: ")
else:   
     print('Exacto esa es la palabra')
'''
# explicacion:Acá, la variable 'palabra' nunca cambia dentro del bucle.
Entonces, si el usuario escribe por ejemplo "chao", 'palabra' vale "chao" siempre, y la condición 'palabra' != "hola" siempre será verdadera.
⚠️ Resultado: ¡El bucle se convierte en infinito! Porque nunca cambiás el valor de palabra, entonces nunca se cumple la condición para salir.
✅ ¿Por qué se necesita volver a pedir el input dentro del while?

La línea:

palabra = input("Intenta de nuevo: ")

hace que el usuario pueda escribir una nueva palabra, y eso actualiza el valor de la variable palabra.

De esa forma, el programa puede volver a evaluar:

while palabra != "hola":

y esta vez, si el usuario escribe "hola", se rompe el bucle porque la condición ya no se cumple.'''


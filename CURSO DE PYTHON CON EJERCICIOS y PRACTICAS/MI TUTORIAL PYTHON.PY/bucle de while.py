#esperando una respuesta
respuesta="" #creo esta variable vacia para que ahi se almacene lo ingresado por el usuario
while respuesta!="'si'": #si el usuario contesta algo diferente a si se va a volver a ejecutar el bucle con la pregunta del input
    respuesta=input("¿Ya terminaste tu tarea? (escribe si para salir): ") #si aca el usuario coloca "si" como respuesta , termina el ciclo de While 
'''¿Ya terminaste tu tarea? (escribe si para salir): 'SI' (regresa al bucle)
¿Ya terminaste tu tarea? (escribe si para salir): 'Si'    (regresa al bucle)
¿Ya terminaste tu tarea? (escribe si para salir): 'sI'    (regresa al bucle)
¿Ya terminaste tu tarea? (escribe si para salir): 'si' (tiene que estar escrito exacamente como lo ingresado en la condicion si se quiere salir del bucle) 
PS H:\CURSO DE PYTHON\Curso de Python Principal> (esto indica que termino el ciclo)'''

 #¡Cuidado con los bucles infinitos!

'Si la condición nunca cambia o siempre es verdadera, el bucle nunca se detiene. Mira este error común:'

while True:
    print("¡Nunca termina!")
    break
'Esto se ejecutará para siempre (hasta que lo detengas manualmente).'

# cómo salir de un bucle antes de que termine

'Puedes usar break para salir:'

while True:
    texto = input("Escribe 'salir' para terminar: ")
    if texto == "salir":
        break

"""break es una palabra clave (instrucción) que se usa para salir de un bucle antes de que la condición termine naturalmente.
Se puede usar tanto en bucles while como en for.
¿Cómo funciona?
Cuando Python lee la palabra break, sale inmediatamente del bucle, sin importar si la condición aún es True."""

# Ejemplo simple con while

contador = 1

while contador <= 10:
    print("Contador:", contador)
    
    if contador == 5:
        print("¡Llegamos al 5! Saliendo del bucle.")
        break  # salimos del bucle
    
    contador += 1
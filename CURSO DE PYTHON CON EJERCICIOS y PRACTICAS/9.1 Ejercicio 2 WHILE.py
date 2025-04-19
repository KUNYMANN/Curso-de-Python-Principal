'''Ejercicio con contador:

El programa debe pedir al usuario que escriba la palabra mágica ("por favor"). Tiene 3 intentos. Si la escribe correctamente dentro de esos intentos, debe mostrar un mensaje de éxito. Si se equivoca las 3 veces, debe mostrar un mensaje de que no lo logró.

 Pista:

    Usá un while que se repita mientras el usuario no acierte y no se pase de los 3 intentos.

    Usá una variable como intentos = 0 para contar.'''

intentos=0
palabra_magica="gracias"
correcta=""
while correcta!=palabra_magica and intentos<3:
    correcta=input("Ingrese la palabra magica: ").strip().lower()
    intentos+=1
if correcta==palabra_magica:
      print("fantastico")
else:
    print("Acceso bloqueado")

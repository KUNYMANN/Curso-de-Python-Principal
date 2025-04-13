''' crear un menú interactivo.
En este caso vamos a agregar un título que va a ser Sistema de administración de cuentas y vamos a tener el siguiente menú.
Vamos a tener las opciones de Crear cuenta, eliminar una cuenta y también salir del sistema.
Posteriormente vamos a solicitar una opción, por ejemplo en este caso Crear cuenta y nos manda el mensaje creando tu cuenta.
El objetivo del ejercicio es crear un menú que se repita tantas veces como sea necesario hasta que proporcionemos la opción de salir.'''

print("***SISTEMA DE ADMINISTRACION DE CUENTAS***")
salir=False
while not salir:
    print('''MENU:
  1. Crear
  2. Eliminar cuenta
  3. Salir''')
    opcion=int(input("Escoje una opcion:"))
    if opcion==1:
        print("Creando cuenta...\n")
    elif opcion==2:
        print("Eliminando cuenta...\n")
    elif opcion==3:
        print("Saliendo del sistema \n")
        salir=True
    else:
        print('Opción invalida')
   



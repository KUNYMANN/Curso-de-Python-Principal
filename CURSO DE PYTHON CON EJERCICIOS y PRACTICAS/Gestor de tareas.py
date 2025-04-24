tareas = []
salir = False

while not salir:
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    try:
        opcion = int(input("Elegí una opción: "))
    except ValueError:
        print("❌ Tenés que ingresar un número.")
        continue

    if opcion == 1:
        nueva_tarea = input("Escribí la nueva tarea: ")
        tareas.append(nueva_tarea)
        print("✅ Tarea agregada correctamente.")

    elif opcion == 2:
        if len(tareas) == 0:
            print("📭 No hay tareas todavía.")
        else:
            print("📋 Tus tareas:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")

    elif opcion == 3:
        if len(tareas) == 0:
            print("❌ No hay tareas para eliminar.")
        else:
            try:
                num = int(input("¿Qué número de tarea querés eliminar? "))
                if 1 <= num <= len(tareas):
                    eliminada = tareas.pop(num - 1)
                    print(f"🗑️ Tarea '{eliminada}' eliminada.")
                else:
                    print("❌ Número fuera de rango.")
            except ValueError:
                print("❌ Ingresá un número válido.")

    elif opcion == 4:
        print("👋 ¡Hasta luego!")
        salir = True

    else:
        print("❌ Opción inválida. Probá de nuevo.")

 # explicacion del desarrollo del programa y variables utilizadas

'''🔁 1. tareas = []

tareas = []

¿Qué hace?
Crea una lista vacía llamada tareas.
Ahí se van a guardar las tareas que el usuario escriba.

🧠 Pensalo como una caja vacía donde vas a guardar papelitos con tus tareas:

["hacer la tarea", "lavar los platos", "estudiar python"]

🛑 2. salir = False

salir = False

¿Qué hace?
Crea una variable para controlar cuándo salir del programa.
Mientras sea False, el programa va a seguir ejecutándose.
🔁 3. El bucle principal (while not salir)

while not salir:

¿Qué hace?
Es un bucle que se repite una y otra vez mientras salir sea False.
Cuando salir se convierte en True, el programa termina.

📌 Esto es lo que permite que el menú vuelva a aparecer cada vez.
📋 4. Mostrar el menú

    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

¿Qué hace?
Muestra las opciones disponibles al usuario.
Esto aparece cada vez que se repite el bucle.
🎯 5. Elegir una opción del menú

    try:
        opcion = int(input("Elegí una opción: "))

¿Qué hace?
Pide al usuario que ingrese una opción (1, 2, 3 o 4).
int(...) convierte lo que escribió en número.

    except ValueError:
        print("❌ Tenés que ingresar un número.")
        continue

¿Por qué ese try/except?
Para evitar que el programa se rompa si el usuario escribe algo que no es número (como una letra).
Por ejemplo, si alguien escribe "hola", sin try se rompe el programa.
Con try, solo muestra un mensaje y vuelve a mostrar el menú.
➕ 6. Opción 1 – Agregar tarea

    if opcion == 1:
        nueva_tarea = input("Escribí la nueva tarea: ")
        tareas.append(nueva_tarea)
        print("✅ Tarea agregada correctamente.")

¿Qué hace?

    Le pide al usuario que escriba la tarea.

    La agrega a la lista con .append().

    Muestra mensaje de éxito.

🧠 Ejemplo:

Usuario escribe: estudiar python
La lista queda: ["estudiar python"]

👀 7. Opción 2 – Ver tareas

    elif opcion == 2:
        if len(tareas) == 0:
            print("📭 No hay tareas todavía.")
        else:
            print("📋 Tus tareas:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")

¿Qué hace?

    Si la lista está vacía (len(tareas) == 0), dice que no hay tareas.

    Si tiene tareas, las muestra una por una con su número.

🧠 Ejemplo:

tareas = ["estudiar", "comer", "dormir"]

Se imprime:

1. estudiar
2. comer
3. dormir

🗑️ 8. Opción 3 – Eliminar una tarea

    elif opcion == 3:
        if len(tareas) == 0:
            print("❌ No hay tareas para eliminar.")

    Si no hay tareas, no puede eliminar nada.

        else:
            try:
                num = int(input("¿Qué número de tarea querés eliminar? "))
                if 1 <= num <= len(tareas):
                    eliminada = tareas.pop(num - 1)
                    print(f"🗑️ Tarea '{eliminada}' eliminada.")

¿Qué hace?

    Pide un número de tarea para eliminar.

    Verifica que el número esté en el rango correcto.

    Si es válido, elimina la tarea usando .pop(num - 1) y muestra un mensaje.

💡 num - 1 porque las listas en Python empiezan en 0:

tareas[0] → 1. tarea
tareas[1] → 2. tarea

                else:
                    print("❌ Número fuera de rango.")
            except ValueError:
                print("❌ Ingresá un número válido.")

    Si el usuario escribe mal (letras, símbolos...), muestra error sin romper el programa.

👋 9. Opción 4 – Salir del programa

    elif opcion == 4:
        print("👋 ¡Hasta luego!")
        salir = True

¿Qué hace?

    Muestra un mensaje de despedida.

    Cambia salir a True, lo que corta el bucle y finaliza el programa.

❌ 10. Opción inválida

    else:
        print("❌ Opción inválida. Probá de nuevo.")

¿Qué hace?

    Si el usuario elige una opción distinta de 1 a 4, le muestra un mensaje de error.'''


print()

#Paso 1: Crear la lista vacía y una variable para salir

tareas = []      # Acá vamos a guardar las tareas
salir = False    # Esta variable nos dice cuándo salir del programa

#👉 Esto solo prepara el espacio para guardar información y controlar el bucle.

#Paso 2: Empezamos el bucle que muestra el menú

while not salir:
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = int(input("Elegí una opción: "))

#👉 Acá se repite el menú hasta que salir se vuelva True.
#El usuario elige una opción del 1 al 4.

#Paso 3: Opción 1 - Agregar tarea

    if opcion == 1:
        nueva_tarea = input("Escribí la nueva tarea: ")
        tareas.append(nueva_tarea)
        print("✅ Tarea agregada correctamente.")

#👉 Guardamos la tarea en la lista con .append() y le damos feedback al usuario.


#Paso 4: Opción 2 - Ver tareas

    elif opcion == 2:
        if len(tareas) == 0:
            print("📭 No hay tareas todavía.")
        else:
            print("📋 Tus tareas:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")

#👉 Si no hay tareas, avisamos. Si hay, las mostramos con numeritos.


#Paso 5: Opción 3 - Eliminar tarea
    elif opcion == 3:
        if len(tareas) == 0:
            print("❌ No hay tareas para eliminar.")
        else:
            num = int(input("¿Qué número de tarea querés eliminar? "))
            if 1 <= num <= len(tareas):
                eliminada = tareas.pop(num - 1)
                print(f"🗑️ Tarea '{eliminada}' eliminada.")
            else:
                print("❌ Número fuera de rango.")

#👉 Solo eliminamos si hay tareas y si el número es válido.


#Paso 6: Opción 4 - Salir

    elif opcion == 4:
        print("👋 ¡Hasta luego!")
        salir = True

#👉 Cuando elige salir, cambiamos salir = True para cortar el bucle.


#Paso 7: Cualquier otra opción

    else:
        print("❌ Opción inválida. Probá de nuevo.")

#👉 Si elige algo que no está entre 1 y 4, le mostramos un error.

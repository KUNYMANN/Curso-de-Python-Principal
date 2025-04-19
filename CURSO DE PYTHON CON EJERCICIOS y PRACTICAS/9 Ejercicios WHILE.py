'''
🧠 Ejercicio 1: Contador hasta que el usuario diga "salir"

Pide al usuario una palabra, y sigue pidiéndola hasta que escriba "salir". Cuenta cuántas veces ingresó algo antes de salir.

contador=0
ingreso=input("Ingrese una palabra(escribe 'salir' para termnar): ")
while ingreso!="salir":
     ingreso=input("Vuelva a ingresar otra palabra o 'salir' para terminar: ")
     contador+=1
print(contador)

🔢 Ejercicio 2: Número positivo
Pide al usuario que ingrese un número. Si es negativo, vuelve a pedirlo hasta que dé uno positivo. Luego muestra el número ingresado.
numero_ingresado=float(input('Ingrese un numero a su gusto: '))
while numero_ingresado>0:
    print('El numero ingresado es positivo')
    numero_ingresado=float(input('Vuelva a Ingresar un numero a su gusto: '))
while  numero_ingresado==0:
       print("El numero ingresado es el cero")
       numero_ingresado=float(input('Vuelva a Ingresar un numero a su gusto: '))
print(f"El numero {numero_ingresado} ingresado es negativo")   '''


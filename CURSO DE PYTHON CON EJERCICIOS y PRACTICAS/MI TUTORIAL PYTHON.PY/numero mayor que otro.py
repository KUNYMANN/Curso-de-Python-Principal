
#programa para indicar el mayor de dos números proporcionados.

"""Así que se les pide crear lo siguiente.
Van a crear un programa para indicar cuál es el mayor de dos números.
El programa debe pedir al usuario dos números enteros y posteriormente se deben comparar y mandar a
imprimir el número mayor."""

numero1=int(input("Ingrese un numero entero que desee: "))
numero2=int(input("Ingrese otro numero entero:"))
if numero1>=numero2:
    print(f"el numero mayor es {numero1}")
else:
    print(f"el numero mayor es {numero2}")
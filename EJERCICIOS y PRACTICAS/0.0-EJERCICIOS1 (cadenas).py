#Ejercico 1
'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.'''
#con un BUCLE for i in range,  recordar que el PRINT va identado
'''nombre=input("Coloque su nombre: ")
num=int(input("Coloque un numero de cantidades de veces que aparecera su nombre: "))
for i in range(num):
    print(nombre)'''
#con \n.join 
'''nombre=input("Coloque su nombre: ")
num=int(input("Coloque un numero de cantidades de veces que aparecera su nombre: "))
print("\n".join(nombre)*num)'''

#Ejercicio 2
'''Escribir un programa que pregunte el nombre completo del usuario en la consola 
y después muestre por pantalla el nombre completo del usuario tres veces,
una con todas las letras minúsculas, otra con todas las letras mayúsculas 
y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.'''
'''nombre=input("ingrese su nombre completo: ")
print(nombre.upper())
print(nombre.lower())
print(nombre.title())'''

#Ejercicio 3
'''Escribir un programa que pregunte el nombre del usuario en la consola 
y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
donde <NOMBRE> es el nombre de usuario en mayúsculas 
y <n> es el número de letras que tienen el nombre.'''
'''nombre=input("Coloque su nombre: ")
caracteres=len(nombre)
print(f"Su nombre es {nombre} y tiene la cantida de {caracteres} caracteres")'''

#Ejercicio 4
'''Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo 
es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato 
y muestre por pantalla el número de teléfono sin el prefijo y la extensión.'''

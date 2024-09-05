#Ejercico 1
'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.'''
#con un BUCLE for i in range,  recordar que el PRINT va identado
'''nombre=input("Coloque su nombre: ")
num=int(input("Coloque un numero de cantidades de veces que aparecera su nombre: "))
for i in range(num):
    print(nombre)'''
#con \n.join 
'''# nombre=input("Coloque su nombre: ")
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
print(f"Su nombre es {nombre} y tiene la cantida de {caracteres} caracteres")
print(len(nombre)) #tambien se puede pedir directamente asi la cantidad de caracteres de una variable'''

#Ejercicio 4
'''Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo 
es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato
y muestre por pantalla el número de teléfono sin el prefijo y la extensión.'''
'''numtelef=input("coloque su numero de telefono con este formato +xx-xxxxxxxxx-xx: ")
print("el Numero ingresado es: ", numtelef[4:-3])'''

#Ejercicio 5
'''Escribir un programa que pida al usuario que introduzca una frase 
en la consola y muestre por pantalla la frase invertida.'''
'''frase=input("Ingrese una frase: ")
print(frase[::-1])'''

#Ejercicio 6
'''Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
 y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.'''
'''frase1=input("Ingrese una frase: ")
vocal=input("Ingrese  una vocal: ")
print(f"{frase1.lower()} {vocal.title()}")'''

#Ejercicio 7
'''Escribir un programa que pregunte el correo electrónico del usuario en la consola
 y muestre por pantalla otro correo electrónico con el mismo nombre 
 (la parte delante de la arroba @) pero con dominio ceu.es.'''

'''correo=input("Ingrese su correo electronico: ")
print(correo[:correo.find("@")] + "@ceu.es.com")
email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')] + '@ceu.es')'''

#Ejercicio 8
'''Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y 
muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find(".")], "euros y", precio[precio.find(".")+1:], "centimos.") # aqui toma en el valor de la variable "precio" 
#desde el indice 0 por eso no hay nada escrito antes de los ":"  hasta el punto ("." que representa la coma de los num decimales) en el valor colocado,
# luego incertamos lo que queremos que aparezca en consola en este caso "euros y" despues colocamos "," para concatenar la segunda parte 
# del valor que resta a partir del punto (.) por eso se pide del valor introducido en la variable "precio" a partir del (.) en adelante por eso se 
# coloca "+ 1" lo cual sera el siguiente indice que quiero utilizar, si coloco los ":" sin nada detras quiere decir que es hasta el final de la variable'''

#Ejercicio 9
#longitud de una cadena
'''cadena="No voy en tren voy en avion"
print("la cantidad de caracteres incluidos los espacio de esta frase es de :", len(cadena))
#numero de veces que aparece la letra "o". 
print("Cantidad de repeticiones de la letra 'v' : ",cadena.count("v"))
#Si no se encuentra, arrojar este mensaje: "La letra no aparece"
no_esta=cadena.count("u")
if no_esta==0:
      print("la letra solicitada no aparece")
else:
      print("Cantidad de repeticiones de la letra : ",cadena.count("u"))
#numero de veces que aparece una vocal en la cadena
vocal="aeiou"
contador=0
for x in cadena:
      if x in vocal:
            contador=contador+1
print("esta frase tiene la cantidad de", contador, "vocales")'''


#Ejercicio 10
''' Crear un programa, que tenga una variable con la cadena “Te quiero solo como amiga”, y muestre la siguiente información:'''

texto='Te quiero solo como amiga'
texto2="recta"
#• Imprima los dos primeros caracteres.
print(texto[:2])
#• Imprima los tres últimos caracteres.
print(texto[-3:])
#• Imprima dicha cadena cada dos caracteres.
print(texto2[::2])
#• Dicha cadena en sentido inverso.
print(texto[::-1])
#• Imprima la cadena en un sentido y en sentido inverso.
print(texto+texto[::-1])
#otra manera de Imprimir la cadena en un sentido y en sentido inversones asi:
print(texto2, end='')
print(texto2[::-1])
#como tambien se pueden sumar ambos textos
print(texto+texto2[::-1])
print(texto[::-1]+texto2)


#Ejercicio 11
'''Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); 
e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r
Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0.'''
palabra="separado"
caracter=","
mezclado=caracter.join(palabra)
print(mezclado)

cadena="Estoy usando el metodo Replase"
print(cadena.replace("e","X")) 
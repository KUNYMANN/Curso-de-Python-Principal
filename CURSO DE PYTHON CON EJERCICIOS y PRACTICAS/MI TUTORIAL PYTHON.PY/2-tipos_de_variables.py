'UNA VARIABLE ES UN ESPACIO EN MEMORIA, QUE VA A SER MOMENTANEO, Y QUE LLEVA ASIGNADO UN NOMBRE Y UN VALOR '
# nombre_de_la_variable  =  valor (o tipo de dato) } asi es la sintaxis de una variable
nombre="KUNY MANN" # esta variable indentificada con la palabra "nombre" tiene un valor o dato que es "Kuny" (que es una cadena de texto o strings)
print(type(nombre)) # str
print(nombre)

print() #un print(vacio) genera un salto de renglon en consola

numero_entero=10
print(type(numero_entero)) # int
print(numero_entero)

print()

numero_decimal=15.3
print(type(numero_decimal)) # float
print(numero_decimal)

print()
#REGLAS A SEGUIR CON LAS VARIABLES Y CONCEJOS

'UNA VARIABLE NO PUEDE TENER EL NOMBRE DE UNA PABLARA RESERVADA (que es aquelkla que el lenguaje ya posee)'

imprimir= "se puede utilizar como nombre para la variable"
print(imprimir)
# ejemplo
#nombre de la variable                          valor o dato asignado
#        print                =         "es una pablabra reservada del lenguaje" 

#        print(print) "cuando la quiera imprimir va a dar error"

import keyword
print(keyword.kwlist)
# estas son las palabras reservadas del lenguaje que no se pueden utilizar como nombre de una variable
'''['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
   'lambda', 'nonlocal', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']'''

print()

'UNA VARIABLE NO PUEDE COMENZAR CON UN NUMERO,NI TENER CARACTERES ESPECIALES ^@`-!?, etc (la Ñ es considerado un caracter especial)'
'ATENCION si se puede el guion bajo (_)'
#ejemplo:
#   30_años="anvesario"
#    print(30_años) va a arrojar error ya sea porque comenzo por un numero o por tener incluido un caracter especial
"si es correcto, colocar una palabra que anteceda a un numero"
años30="Decada de 1930"
print(años30)

'no se pueden colocar espacios vacios'
#ejemplo:
#   mis amigos="son unos genios"
#   print(mis amigos) va a dar error por tener espacios vacios entre palabra y palabra en el nombre de la variable
                     #para evitar ese error se coloca el guion bajo como nexo entre una palabra y otra (mis_amigos)

print()

'CONSEJOS'
#colocar nombres a las variables que sean descriptivas, o sea que hagan referencia al dato o valor que voy a colocarle a esta

#ejemplo:
#si tengo que colocar datos de una persona
edad=20
sexo="masculino"
color_de_piel="trigueño" 
color_de_ojos="miel"
altura=1.75
contextura="robusta"
tamaño_del_calzado=44.5
print(f"su edad es: {edad} años \nsu sexo es: {sexo}\nsu tono de piel es: {color_de_piel}\nsu color de ojos es: {color_de_ojos} ")
print(f"su altura es: {altura}\nsu contextura fisica es: {contextura}\nsu tamaño de calzado es:{tamaño_del_calzado}")
print()
print(f"su edad es: {edad} años")
print(f"su sexo es: {sexo}")
print(f"su tono de piel es: {color_de_piel}")
print(f"su color de ojos es: {color_de_ojos}")
print(f"su altura es: {altura}")
print(f"su contextura fisica es: {contextura}")
print(f"su tamaño de calzado es:{tamaño_del_calzado}")
print()
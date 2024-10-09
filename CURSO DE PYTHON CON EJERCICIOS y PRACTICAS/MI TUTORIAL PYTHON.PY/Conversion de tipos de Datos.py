#ENTRADA DATOS POR CONSOLA
'La conversion de tipos de datos, tambien vonocida como casting es una tecnic para manipular datos que no estan el el tipo requerido'
#podemos hacer conversiones desde y hacia distintos tipos de datos
'''CADENAS DEL TIPO NUMERICOS 
convertir a entero utilizando la funcion INT()
convertir a flotante con la funcion FLOAT()
convertir a cadena con la funcion STR()
convertir a booleano con la funcion bool()'''
#convertir de cadena a numero
numero_cadena='10' #al estar entre comillas es un str
numero_entero=int(numero_cadena)
print(f"el numero {numero_cadena} de la variable numero_cadena es un string")
print(type(numero_cadena))#str
print(f"el numero {numero_entero}  de la variable numero_entero convertido ahora es un int")
print(type(numero_entero))#int

print()
 
#convertir de cadena a float
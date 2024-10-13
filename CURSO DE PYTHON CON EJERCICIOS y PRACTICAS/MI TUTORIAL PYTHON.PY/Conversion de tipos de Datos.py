#CONVERSION DE TIPOS DE DATOS
'La conversion de tipos de datos, tambien vonocida como casting es una tecnic para manipular datos que no estan el el tipo requerido'
#podemos hacer conversiones desde y hacia distintos tipos de datos
'''CADENAS DEL TIPO NUMERICOS 
convertir a entero utilizando la funcion INT()
convertir a flotante con la funcion FLOAT()
convertir a cadena con la funcion STR()
convertir a booleano con la funcion bool()'''

#LA CONVERSION DE NUMEROS STRINGS"" A NUMEROS ENTEROS O FLOTANTES NOS PERMITE UTILIZARLOS EN OPERACIONES ARITMETICAS o VICEVERSA

#convertir de cadena(STRING) a numero
numero_cadena='10' #al estar entre comillas es un str
numero_entero=int(numero_cadena)
print(f"el numero {numero_cadena} de la variable numero_cadena es un string")
print(type(numero_cadena))#str
print(f"el numero {numero_entero}  de la variable numero_entero convertido ahora es un int")
print(type(numero_entero))#int

print()
 
#convertir de cadena(STRING) a float
numero_redondo=156
print(f"el numero redondo es: {numero_redondo}")
print(type(numero_redondo))
print()
numero_string="3.14"
print(f"el numero string es: {numero_string}")
print(type(numero_string))
print()
numero_decimal=float(numero_string)
print(f"el numero redondo convertido a float(decimal) es: {numero_decimal}")
print(type(numero_decimal))
print()
#Como convertir de numeros a cadena(STRING)
numero=25
print(f"El numero entero es: {numero}")
print(type(numero))
print()
numero_texto=str(numero)
print(f"el numero entero 25 convertido a texto(string) es: {numero_texto}")
print(type(numero_texto))

#Convertir a booleano (recordemos que la funcion bool evalua en True o False)
'el Bool es falso en los siguientes casos'
#Si el valor de una variable es 0, cadena vacia o None, entonce Regresa False
'Regresa True, si el valor de es distintom de 0, si es distinto de cadena vacia y tambien si es distinto de None'

numero_entero=0
booleano=bool(numero_entero)
print(f"El valor booleano de 0 es: {booleano}")#False, puede ser 0 o 0.0
print()
numero_entero=5
booleano=bool(numero_entero)
print(F"eL valor booleano de 5 es: {booleano}")#True
print()
cadena_vacia=''# al colocarlo asi significa que el largo de la cadena es 0,  por eso va a arrojar False
bool_cadena=bool(cadena_vacia)
print(f"el valor booleano de una cadena vacia es: {bool_cadena}")#Falsae, tambien incluye colecciones vacias
print()
cadena_con_valor="Kunymann"
bool_de_cadena_con_valor=bool(cadena_con_valor)
print(f"El booleano de una cadena con valor es : {bool_de_cadena_con_valor}")#True
print()
variable_tipo_None=None
bool_de_variable_tipo_None=bool(variable_tipo_None)
print(f"El valor booleano de una variable tipo None es: {bool_de_variable_tipo_None}")#False
print()

#EJERCICIO DE CONVERSION DE DATOS
#Concatenacion o suma de valores
numero1_cadena='10'
print(f'numero 1 en cadena: {numero1_cadena}')
numero2_cadena='20'
print(f'numero 2 en cadena: {numero2_cadena}')
resultado=numero1_cadena+numero2_cadena
print(f'El resultado es una concatenacion {resultado}')# 1020 el resultado es una concatenacion de ambos numeros no una operacion aritmetica
print()
#convertir a tipos enteros
numero1_entero=int(numero1_cadena)
numero2_entero=int(numero2_cadena)
resultado=numero1_entero+numero2_entero
print(f'El resultado va a ser una operacion aritmetca SUMA que da como total: {resultado}')#30
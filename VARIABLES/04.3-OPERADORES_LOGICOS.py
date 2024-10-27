# Los operadores logicos permiten construir expresiones logicas y se obtiene como resultado booleanos 
'LA COMPARACION MINIMA ES ENTRE DOS OPERANDOS'
# and (y).... conjuncion o multiplicacion logica true es 1 y false es 0  
# or (o)..... disyuncion o suma logica
# not (no).... negacion      
'''PRIORIDAD DE LOS PERADORES LOGICOS
not (que españos significa "NO")
and (que en español significa "Y") 
y or (que en español significa "O")'''


'OPERADOR AND (y) "multiplicacion logica"'
#IMPORTANTE!!! solo si ambos operandos son verdaderos el resultado va a ser siempre verdadero
#con un minimo de dos operandos de valores logicos o booleanos a comparar
#En la programacion TRUE tiene el valor de 1 dado que solo el 1 multiplicado por si mismo da 1
#y FALSE tiene el valor 0 porque todo numero multiplicado por 0 es siempre 0
'''operando1   operador   operando2   RESULTADO   
True        and (y)       True       TRUE  (si ambos operandos son verdaderos el resultado siempre sera true) 1 
True        and (y)       False      FALSE (si cuaquiera de los dos operandos es falso el resultado siempre sera false)  0 
False       and (y)       True       FALSE (si cuaquiera de los dos operandos es falso el resultado siempre sera false)  0 
False       and (y)       False      FALSE (si cuaquiera de los dos operandos es falso el resultado siempre sera false)  0
"""
print("*** OPERADOR AND***")
#Regresa verdadero si ambos valores son verdaderos
condicion1=False
condicion2=False
resultado=condicion1 and condicion2
print(f"El resultado de aplicar la condicion and entre {condicion1} y {condicion2} es: {resultado}")#False
'Cambiamos el valor de una de las variables'
condicion1=False
condicion2=True
resultado=condicion1 and condicion2
print(f"El resultado de aplicar la condicion and entre {condicion1} y {condicion2} es: {resultado}")#False
'Ahora colocaremos dos variables verdaderas'
condicion1=True
condicion2=True
resultado=condicion1 and condicion2
print(f"El resultado de aplicar la condicion and entre {condicion1} y {condicion2} es: {resultado}")#True
"""
"""
print()
edad=54
print(edad>50 and edad<52) #si uno de los resultados de esta solicitud es falso el resultado final es false (54 es mayor que 50 si y es menor que 52 NO)
print(edad>50 and edad<60) #si los resultados de esta solicitud son correctos  el resultado final es true (54 es mayor que 50 si y es menor que 60 si)
print(edad>56 and edad<60) #si uno de los resultados de esta solicitud es falso el resultado final es false (54 es mayor que 56 NO y es menor que 60 si)
print()
print(edad<60 or edad>53) # TRUE...(ambas condiciones son ciertas, 54 es menor que 60 pero tambien 54 mayor que 53)
print(not(edad>52))# FALSE...(no es cierto que 54 es mayor que 52? es falso porque 54 es mayor a 52) una verdad negada es falsa
print(not(edad>56))#TRUE...(no es cierto que 54 sea mayor que 56? es verdad porque 54 no es mayor a 56) una mentira negada es verdad
"""

# Prioridadde los operadores logicos
# 1. not lo contrario a lo evaluado, la negacion invierte el resultado si es true pasa a ser false y si es false pasa a ser true
# 2. and componente que da una orden que se tienen que cumplir varias ordenes  para ver si se cumple una cosa "y" tambien la otra 
# (en AND para que el resultado sea verdadero todo debe resultar verdadero)
# 3. or componente que evalua si es esto "o" lo otro (en OR para que el resultado sea verdadero, basta con que uno sea verdadero)
"""
# EJEMPLO
# a=10, b=12, c=13, d=13
#      desarrollo sobre un ejercicio con tres tipos de operadores:logicos, aritmeticos y relacionales

#   ((a>b)or(a<c))     and     ((a==c)or(a>=b)      ejercicio inicial
# ((10>12)or(10<13))   and   ((10==13)or(10>=12)    reemplazo por los valores asignados
#     (F  or  T)                 (F   or   F)       vamos comprobando por partes
#        (T)           and             (F)          resultante
#                   (T and F)                       evaluacion final
#                      (F) False                    conclusion final 

print()
'''
'EJERCICIO'
print("""Una tienda de supermercado ofrece un descuento especial a los clientes que compren 10 o mas articulos por dia
y que ademas sean miembros de la tienda
    el sistema debe solicitar al cliente que indique cuantos articulos a comprado en el dia
    tambien preguntarle si cuenta con una membresia de la tienda
    En caso de haber comprado 10 o mas articulos y ser miembro de la tienda tendra acceso 
    al descuento VIP""")
'''
print("***DESCUENTO VIP con el operando AND***")
numeros_productos=10  #cantidad de productos requerida para descuento
cantidad=int(input("Ingrese la cantidad de articulos comprados hoy en la tienda: ").strip())
clientevip=input("Cuenta usted con una cuenta menmbresia de la tienda: (Si/No) ").strip().lower()

articulos=(cantidad>=numeros_productos #aqui preguntamos cuantos articulos compro en el dia y si dicha cantidad superanes igual o mayor a los 10 requeridos 
           and # y
           clientevip=="si") #preguntamos con el == si Si o No, el cliente tiene una cuenta membresia, para ver si correspode el descuento
"""
print(f"SU ACCESO AL DESCUENTO VIP ES {articulos}  ")
print("""Si ambos operandos son verdaderos el resultado siempre sera TRUE
Si cuaquiera de los dos operandos es falso el resultado siempre sera FALSE""")

print()

"""OPERADOR OR se lo conoce como una suma logica
IMPORTANTE!!! solo si ambos operandos son falsos el resultado va a ser siempre falso
operando  RESULTADO
True         or (o)       True       TRUE    (basta que cualquiera de los dos operandos sea verdadero el resultado siempre sera true) 1
True         or (o)       False      TRUE    (basta que cualquiera de los dos operandos sea verdadero el resultado siempre sera true) 1
False        or (o)       True       TRUE    (basta que cualquiera de los dos operandos sea verdadero el resultado siempre sera true) 1
False        or (o)       False      FALSE   (cuando ambos operandos son falso el resultado siempre sera false) 0"""

"""
print("*** OPERADOR LOGICO ***")
situacion1=False
situacio2=False
#El operador OR devuelve False unicamente si ambos operandos son False 
resultado=situacion1 or situacio2
print(resultado) #False

print()

#El operador OR devuelve True si cualquiera de los operandos es True
situacion3=False
situacion4=True
resultado=situacion3 or situacion4
print(resultado)#True
"""
'EJERCICIO'
print("""Se pide crear un sistema para una biblioteca, la cual desea prestar libros, solo si cumple 
con qualquiera de las siguientes condiciones
1-el usuario debe tener credencial de estudiante
2-el usuario vive a no mas de 3 km a la redonda
Si cumple con cualquiera de estas condiciones se le puede prestar el libro""")
print()
"""
print('*** PRESTAMO DE LIBROS con el operando OR ***')
estudiante=input("Para retirar un libro nesecitamos saber si tiene credencial de estudiante (Si/No): ").strip().upper()
cercano=input("Vive a menos de 3 Km de la biblioteca (Si/No): ").strip().upper()
prestamo=estudiante=="SI"
prestamo1=cercano=="SI"
resumen=prestamo or prestamo1
print(f"DE ACUERDO CON LO INGRESADO VEREMOS SI ESPOSIBLE PRESTARLE UN LIBRO: {resumen}")'''
print('''cuando ambos operandos son falso el resultado siempre sera FALSE
si cualquiera de los dos operandos es verdadero el resultado siempre sera TRUE)''')

print()
"""
print('***Creditos con el operando OR***')
cliente=input("Para otorgarle un Credito nesecitamos saber si usted es cliente del banco (Si/No): ").strip().upper()
distancia=int(input("A cuantos Km vive usted del banco : ").strip())
distancia_permitida=3
credito=cliente=="SI"
credito1=distancia<=distancia_permitida
otorgamiento=credito or credito1
print(f"DE ACUERDO CON LO INGRESADO PARA ACCEDER A UN CREDITO EN NUESTRO BANCO SU CONDICION ES {otorgamiento}  ")
print('''cuando ambos operandos son falso el resultado siempre sera FALSE
si cualquiera de los dos operandos es verdadero el resultado siempre sera TRUE)''')
print()"""


"""OPERADOR NOT se lo conoce como un valor de negacion
IMPORTANTE!!! Invierte el valor del operador y se lo conoce como un Operador Unario porque trabaja con un solo valor
operando    RESULTADO
not(True)    FALSE  (UNA VERDAD NEGADA ES UNA MENTIRA) Ejemplo: #si es verdad que jesus no existió...FALSO porque se esta mintiendo sobre una verdad, jesus existio
not(False)   TRUE   (UNA MENTIRA NEGADA ES UNA VERDAD) Ejemplo: #no es verdad que jesus no existio...VERDAD porque jesus si existio"""

print()

print("*** OPERADOR NOT ***")
condicional=False
resultado= not condicional
print(f"Si el condicional es 'False' con el operador NOT pasa a ser '{resultado}'")

condicional1=True
resultado1=not condicional1
print(f"Si el condicional es 'True' con el operador NOT pasa a ser '{resultado1}'")

#revisar si una variablees una cadena vacia
nombre='' #creamos una variable
es_cadena_vacia=not nombre #preguntamos si la variable tiene algun valor
print(f"\nLa variable no tiene nungun valor? {es_cadena_vacia}")#nos devuelve la respuesta

#si le asignamos un valor a la cadena
nombre='casa Rosa' #creamos una variable
es_cadena_vacia=not nombre #preguntamos si la variable tiene algun valor
print(f"\nLa variable no tiene nungun valor? {es_cadena_vacia}")#nos devuelve la respuesta

print()

#si una variable no tiene ningun valor asignado
variable=None #creamos una variable con el valor "None"
variable_sin_valor=not variable #preguntamos si la variable tiene algun valor
print(f"\nLa variable no tiene nungun valor asignado? {variable_sin_valor}")#nos devuelve la respuesta
#si le asignamos un valor a la variable
variable= 'casa Rios' #creamos una variable con un valor asignado
variable_sin_valor=not variable #preguntamos si la variable tiene algun valor
print(f"\nLa variable no tiene nungun valor asignado? {variable_sin_valor}")#nos devuelve la respuesta
print()
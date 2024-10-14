#ENTRADA DATOS POR CONSOLA
'En Python la entrada de datos se realiza mediante la funcion INPUT()'
'''esta funcion pausa la ejecucion del programa y espera a que el usuario introduzca algun texto
 (aunque sea un numero el programa lo ingresa como texto) desde el teclado'''
'una vez que usuario presiona enter, el texto introducido se devuelve como una cadena (str)'
'''CARACTERISTICAS DE LA FUNCION INPUT()

INTERACTIVIDAD: nos permite interactuar con el Usuario, permite proporcionar valores dinamicos, 
en lugar de utilizar valores en codigoduro o estaticos

SENCILLEZ: la funcion input()es muy facil de usar y solo necesita, opcionalmente, la cadena o mensaje a mostrar al usuario,
para que este sepa lo que se le esta solicitando, lo recomendable es que siempre le indiquemos con un mensaje, con un texto, 
qué valor tiene que proporcionar en la consola.

TIPOS DE DATOS: En este caso la función input siempre devuelve una cadena, pero si requerimos otro tipo de dato, simplemente
hay que convertirlo con todo lo que ya hemos visto de conversión de tipo de datos.'''
#EJEMPLO
nombre=input("Ingrese su Nombre: ")#Hector
nombre=nombre.upper()
print(f"Su Nombre es: {nombre}")#Su Nombre es Hector
edad=input("Ingrese su edad: ")#58
print(edad)#58
print(type(edad))#str
años=int(edad)#58
print(años)#58
print(type(años))#int
edad1=int(input("Ingrese su edad: "))#si no colocamos la funcion INT()al inicio el valor que nos arroja es un string no un int o un float
print(f"Su edad es: {edad1} años")#58
print(type(edad1))#int
altura=input("Ingrese su altura exacta: ")#1.83
print(altura)#1.83
print(type(altura))#str
altura1=float(input("Ingrese su altura exacta: "))#si no colocamos la funcion FLOAT()al inicio el valor que nos arroja es un string no un int o un float
print(f"Tu altura exacta es: {altura1}")#1.83
print(type(altura1))#float
print()
#ejercicio
print(f"Tu edad es: {edad1} pero dentro de dos años tendras {edad1+2}")# al ser un int puedo realizar una operacion aritmetica
print()

#Generar un programa que solicite los de un empleado
print("   *** SISTEMA DE EMPLEADOS ***   ")
nombre_empleado=input("Ingrese su nombre registrado en la empresa: ")
nombre_empleado=nombre_empleado.upper()
edad_del_empleado=int(input("Ingrese su edad: "))
salario=float(input("Ingrese el monto de su salario exacto: "))
ocupacion=input("Ingrese SI / NO  si su puesto de trabajo es como jefe de departamento: ")
ocupacion=ocupacion.upper()=="SI"                 #Con el ==(el igual igual es una expresion comparativa) convertimos una variable en booleano para 
#el metodo tiene que ser igual al comparativo     #que cuando la solicitemos por print nos arroje si la informacion es True o False
print()
print('\nDatos del empleado')
print(f"Su nombre registrado es: {nombre_empleado}")
print(f"Su edad es de: {edad_del_empleado} años")
#print(type(edad_del_empleado))#int
print(f"Su salario es de $ {salario:.2f}")
#print(type(salario))#float
print(f"Le comunicamos que el puesto de trabajo que usted ingreso segun nuestros registros es {ocupacion}")
#print(type(puesto_trabajo))#bool
print()
print(" *** Receta de Cocina *** ".upper())
nombre_receta=input("Ingrese un nombre para identificar la receta: ")
ingredientes=input("Ingrese los ingredientes que se van a utilizar en la receta: ".capitalize())
tiempo_preparacion=int(input("Introduzca el tiempo que lleva de preparacion expresado en minutos: "))
dificultad=input("Ingrese que tipo de dificultad posee el hacerla Facil, Madia, Alta: ".capitalize())
print()
print("------------------------")
print()
print(f"Nombre de la Receta: {nombre_receta}")
print(f"Ingredientes: {ingredientes}")
print(f"Tiempo de preparacion: {tiempo_preparacion} minutos")
print(f"Nivel de Dificultad: {dificultad.title()}")
print()




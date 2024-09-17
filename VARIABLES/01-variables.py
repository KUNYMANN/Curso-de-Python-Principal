# TIPOS DE VARIABLES "Python almacena objetos, dentro de esos objetos puede haber distintos tipos de datos"
#  variable="Hola Mundo" #este tipo de dato se lo conoce como STRING y hace referencia a un texto
#  numero=42 #llamado NUMBER en este caso es un Nº entero y se lo denomina como INT (INTeger)
#  decimal=3.141516 #llamado NUMBER en este caso los Nº con decimales se lo denomina FLOAT (flotante)
#  verdadero=True # SI esta es una funcion llamada boolean
#  falso=False # NO esta es una funcion llamada boolean

# TIPADO DINAMICO: es que a una variable se le puede asignar valores de diferentes tipos (number o string) en diferentes momentos del programa
valor=10 
print(valor)
print(type(valor))
valor="Kunymann" 
print(valor)
print(type(valor))
print('tu sobrenombre es:', valor) #esta es una forma de imprimir por consola 
print(f"Tu sobrenombre es: {valor}")#esta es otra forma de imprimir por consola con el metodo f (format)
#NUMEROS ENTEROS "INT"
print("hola mundo") # aqui print () seguido de comillas te imprime "el mensaje" en este caso "hola mundo"
numero=10
print(numero) #aqui print() sin las comillas nos muestra "el valor" de la variable "10" y no el mensaje como en hola mundo
print(type(numero))
print('El numero almacenado en la "variable numero" es:', numero)
#NUMERO DECIMAL "FLOAT"
decimal=15.34 
print(decimal)
print(type(decimal)) #float
cadena= "estoy"
print(cadena)
print(type(cadena)) #string
print("quisiera que me digas el valor de la variable cadena:", cadena)
#Utilizacion de comillas de ambas maneras se puede utilizar para resaltar algo en un texto "''" o '""'
#CADENA DE TEXTO "STRING CON 'DESTACADO'" 
cadena= "estoy 'estudiando'"
print(cadena)
print(type(cadena))
cadena= 'estoy "estudiando"'
print(cadena)
print(type(cadena))
#BOOLEAN
valor=True
print(valor)
print(type(valor))
valor=False
print(valor)
print(type(valor))
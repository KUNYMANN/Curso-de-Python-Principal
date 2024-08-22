''' DATO: UN DATO ES UNA DE LAS COSAS BASICAS QUE UTILIZA UN PROGRAMA, COMO UN A LETRA O UN CONJUNTO DE LETRAS (string) 
O UN NUMERO O UN CONJUNTO DE NUMEROS (int/float)no es exclusivo de un lenguaje de programacion '''
#por ejemplo 
#5 que es un numero entero (int) o 49.99 que eun numero condecimales (float)
'''VARIABLE:ES UN NOMBRE QUE HACE REFERENCIA A UN DATO, no es exclusiva de un lenguaje de programacion, 
Y UNA DE LAS CARACTERISTCAS MAS PORTENTES DE UN LENGUAJE DE PROGRAMACION ES LA CAPACIDAD DE MANIPULAR VARIABLES'''
#UNA VARIABLE VA A SER UN ESPACIO EN MEMORIA que vamos a crear y asignar, esta va a llevar un nombre y un dato asignado
#a la inversa seria un dato al que se le asigna un nombre. 
#una variable como su nombre lo indica, puede variar
#-puede ser numerica, pero ese dato puede cambiar
#  -no se puede comenzar con un numero (ejemplo ... 12cafe= "te comun")
#  -no pueden llevar caracteres especiales ñ/*/@ etc., ni al principio ni en cualquier parte del nombre de la variable
# (ejemplo ñandu="animal", sal@me="embutido") el sistema lo identifica y da error
#no puede llevar el nombre de palabras reservadas del lenguaje (ejemplo..print="impresora") el sistema lo identifica y da error

'TIPOS DE DATOS'
#   1-Entero (int) ejemplo: 7
#   2-Flotante (float) ejemplo: 7.14
#   3-Cadena de texto (string) ejemplo: Hola
#   4-Booleanos (True o False)


'las variables por lo general llevan nombres alusivos a los datos ingresados'
#ejemplo:
'si se desea almacenar en una variable un dato que haga referencia a la edad de un ususario'
edad=21 #tipo de dato "int"
print(edad)

'si se desea almacenar en una variable un dato que hace referencia a la altura de un objeto'
altura=1.82 #tipo de dato "float"
print(altura)

'si se desea almacenar en una variable un dato que hace referencia a un mensaje de bienvenida'
mensaje="Bienvenido" # tipo de dato "cadena de texto" (string)
print(mensaje)

# concatenar un int y un str
print(edad,mensaje)




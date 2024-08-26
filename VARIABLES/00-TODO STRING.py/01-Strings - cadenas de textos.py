#CADENAS DE TEXTO (STRINGS)
'Una cadena siempre va a presentar METODOS, estos son otras funionalidades que se le pueden dar a las cadenas'
#QUE ES UNA CADENA O STRING QUE ES LO MISMO?
'''Es una secuencia de caracteres, o un caracter es una letra y cuando tomamos varias letras,
varios caracteres y los ponemos en secuencia, ya sea logica o ilogicamente, entonces
ahi se forman las cadenas o strings'''
#el hecho que tengamos cadenas no quiere decir que especificamente tengamos que llevar
#un orden logico
'''una cadena puede ser "QWERTY" que son las primeras letras de arriba del teclado y eso no tendria sentido 
pero no deja de ser una cadena, lo mismo ocurre para la palabra, mensaje, o la palabra cadena'''
#UNA CADENA NO NECESARIAMENTE TIENE QUE SER UN MENSAJE LOGICO, SOLO NECESITA UNA SUCECION DE CARACTERES

#Ejemplo
"M  O  N  T  Y     P  Y  T  H  O  N"  #CADA CARACTER TIENE UN ESPACIO ASIGNADO EN LA CADENA
'0  1  2  3  4  5  6  7  8  9  10 11' # como podemos verlo aqui 
# Ahora bien estos espacios son importantes tenerlos presente, porque las cadenas van a ocupar un espacio, 
# pero a su vez cada caracter dentro de la cadena va a ocuar otro espacio diferente al de la cadena
'esto quiere decir que si yo mando a llamar al espacio 4 me va a mostar Y de MONTY'
#en algunos casos la cuenta es asi: 0 1 2 3, empezando por el 0 la primer letra, 
# en otros la cuenta no es asi, la cuenta es 1 2 3 empezando por la M que es la primera de la palabra MONTY
# Y en otros el 0 va a ser la comilla, que no se cuenta pero hay algunas excepciones que si
#fundamental tener presente siempre que 'CADA CARACTER OCUPA UN ESPACIO EN LA CADENA'

"DEBANADO DE CADENAS"
# la mayoria de los lenguajes de programacion permiten el debanado de cadenas JavaScript, Python, C# (SHARP) 
# a veces se lo llama slice 
'conciste en mostrar contenido de una cadena de manera segmentada' 
#que quiere decir, que nosotros por medio de instrucciones predeterminadas,
# solo vamos a mostrar un espacio de la cadena, solo vamos a mostrar un conjunto de letras
# solo vamos a mostrar unas cuantas palabras, a eso se lo llama DEBANADO DE CADENAS.
'cuando nosotros queremos mostrar una cadena, pero solo por segmentos, solo por fragmentos de la misma'
# Ejenplo de DEBANADO
"M  O  N  T  Y     P  Y  T  H  O  N" 
'0  1  2  3  4  5  6  7  8  9  10 11'

# ESTO ASI NO SE VA A APLICAR EN TODOS LOS LENGUAJES DE PROGRAMACION
#vamos a ver en que momento se ocupa una regla, en que momento se ocupa otro debanado, en 
#que momento se ocupa un debanado diferente y asi.

cadena='MONTY PYTHON'
print(cadena[0:5])
#[0:5] = "MONTY " #yo aqui mande a llamar del 0 al 5 y me devuelve MONTY 
' " M O N T Y " '
# 0 1 2 3 4 5 #porque de 0 a 5 esta MONTY, vemos que toma la comilla como indice 0
print(cadena[:3])
#[ :3] = "MON "   #espacio null me va a traer, las primeras 3 letras o sea MON
' " M O N " ' # lo mismo ocurre aqui toma como indice 0 la comilla
# 0 1 2 3
print(cadena[-3:])
#[-3: ] = "HON"   #luego del 3 : espacio en blanco eso me va a traer HON, este es un tipo de debanado
'" H  O  N " '    #diferente , este lo que me va a traer es las ultimas tres letras de la cadena puesto que 
# -1 -2 -3        #la solicitud se hizo con un numero negativo, comienza a contar de atras para adelante
print(cadena[:-3])
#[ :-3] = "MONTY PYT" aqui esta eliminado de la seleccion las tres ultimas letras ya que pidio que muestre desde el caracter 0 al -3
'"M  O  N  T  Y     P  Y  T  " '
# 0  1  2  3  4  5  6  7  8
print(cadena[0:11])
#[0:11] = "MONTY PYTO"
' " M  O  N  T  Y     P  Y  T  H  O  "  ' #aqui en la solicitud ocurren dos cosas
' 0 1  2  3  4  5  6  7  8  9  10 11  ' # que tome el valor inicial 0 para la comilla entonces el 11 seria la "O" de PITHON " M  O  N  T  Y    P  Y  T  H  O  " 
print(cadena[0:12])
#[0:12] = "MONTY PYTON"
' " M  O  N  T  Y     P  Y  T  H  O  N"  ' # si queremos que nos devuleva la cadena entera debemos agregar un valor mas al indice, porque si colocamos el ultimo
' 0 1  2  3  4  5  6  7  8  9 10 11 12'  # indice de la cadena puede que el sistema tome como indice 0 las comillas, entonces no nos incluira el ultimo indice

### ATENCION A TENER SIEMPRE EN CUENTA
"""cuando uno solicita un determinado numero de caracteres de una cadena, si se tomo el primero no incluye el ultimo, dado que la solicitud se hace
hasta tal numero, NO INCLUSIVE, si queremos que lo incluya a este ultimo,  debemos solicita un caracter mas, como cuando contamos con los dedos"""
'no ocurre esto a la inversa, cuando la solicitud la hacemos con numeros negativos'


telefono=input("Ingrese un numero de telefono con codigo de area: ")
if telefono[0:3]=="549":
    print("Argentina")
else: 
    print("Es de otro pais")

#reglas de las cadenas
1- '''"las cadenas siempre se escriben entre comillas" inclusive 
si un numero se escribe entre comillas es una cadena o strings'''
# numero= 4 este es un numero
# numero="4" este es una cadena o string
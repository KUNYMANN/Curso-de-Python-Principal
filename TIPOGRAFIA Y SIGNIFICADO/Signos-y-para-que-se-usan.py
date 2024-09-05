#con Shift + Alt mas flecha hacia abajo se duplica la linea 
'''delimitan cadenas de textos
"" delimitan cadenas de textos 
Las 3 comillas te permiten hacer saltos de línea. Por ejemplo puedes imprimir información en pantalla:
print("""Hola, esto es un párrafo 
Esto es otro párrafo 
Y este es otro párrafo""") 

O simplemente hacer comentarios  (#)
# esto es un cometario de una linea o si necesitas hacer comentarios de varias lineas se utiliza """ """
"""Esto es un comentario 
usando varias líneas""" 
tambien puede utilizarse tres comillas simples'''

'''El  "=" es un simbolo de asignacion que difiere del == que se utiliza en los Operadores Aritmeticos
la coma "," es un separador, en el PRINT la coma actua como union entre un string y otro, sin producir espacio vacio en la concatenacion
El ";" permite cambiar de linea

Los paréntesis "()" en Python se utilizan para la creación de tuplas, que son colecciones no modificables de objetos. 
También se utilizan para la definición de funciones así como para su invocación.
El último uso habitual es establecer el orden de evaluación dentro de una expresión.

Los corchetes "[]" en Python se utilizan para la definición de listas, 
para el acceso de lectura a los elementos de tuplas, listas, diccionarios y strings, como para la busqueda de posicion de un elemento,
tambien para el acceso de escritura a listas y diccionarios.

Las llaves "{}" en Python se utilizan para definir diccionarios y para formatear cadenas de texto
incluyendo valores de variables o expresiones.'''

'''para resaltar una palabra se utilizan las comillas dobles per para solicitarlo se utilizan comillas simples, ejemplo
print('"Kuny" es mi apodo') aqui se imprimira lo siguiente  "Kuny" es mi apodo, tambien podria ser print("'Kuny' es mi apodo")
 dependiendo de con que comillas quiero que se imprima, las invierto, nunca se utiliza las mismas para imprimir y resaltar una palabra'''

''' "n\" se utiliza para cambiar de renglon'''

''' "\t.:MENU:." se utiliza en el print para que el titulo aparezca desplazado del margen a 4 espacios'''

'''el input se utiliza siempre cuando es algo que solicite que ingrese el usuario 

el "print(vacio)" solo se utiliza como salto de linea para mostrar resultados

la funcion "len()" es para solicitar la cantidad de caracteres que posee el valor de una variable y SOLO se utiliza con string

el print de la variable en el modo f se solicita entre {} ejemplo print(f"jajaja{}")

"print ()" es para que ejecute la solicitud de lo que deseamos y siempre va entre parentesis
si lo que pedimos internamente esta entre comillas va a arrojar un texto, 
en cambio si lo hacemos sin las commillas va a arrojar un valor

"print(type())" me arroja que tipo o clase "class"" del valor es, sea ""int" numero entero, "float" numero con decimales o "str" texto

"None" es un tipo de dato especial que representa la ausencia de valor o la falta de definición de un valor. 
Se utiliza para indicar que una variable no tiene asignado ningún valor válido. 

count() metodo para saber cuantos elementos estan repetidos dentro de una variable, ya sea una letra o un grupo de letras ejemplo: letras, numeros 
print("Cantidad de repeticiones de la letra o: ",cadena.count("o"))

Utiliza “in” para comprobar si un string contiene ciertas letras o términos. 
Esta función comprueba si el término que buscas está presente en el string y responde con true (verdadero) o false (falso). 

Utiliza “not in” para asegurarte de que un término no aparece en el string. 

es posible dividir un string con la funcion "split()". Un ejemplo sencillo de división es el siguiente:'''
text = "Esto es un ejemplo"
print(type(text)) # es un string
print(text.split()) #aqui el metodo split me divide a la frase en elementos de una la lista, utilizando para dividirla los espacios vacios
#El resultado quedaria asi:  ["Esto", "es", "un", "ejemplo"] en text ha sido dividida en todos sus espacios y se devolvió una lista de subcadenas
print(type(text.split())) # es una lista
mi_cadena="soy Hector, mi apodo es kuny, tengo 58 años, juego al basquet"
print(type(mi_cadena))# es un string
print(mi_cadena.split(",")) #aqui el método split() usando el parametro de division la "," devuelve una lista de mi cadena, donde cada parte de la frase 
#hasta la coma es un elemento de la lista. ejemplo: "soy Hector" es un elemento, "mi apodo es kuny" es otro elemento, y asi sucesivamente
print(type(mi_cadena.split())) # es una lista

print("".join(mi_cadena)) #con el metodo .join()vuelvo a unir los elementos y los transforma en un solo elemento
mi_cadena1=["Manzanas","Naranjas","Peras","Platanos","Bayas"]
print("---".join(mi_cadena1)) 
print(type(mi_cadena1))# es una lista
print(type("---".join(mi_cadena1)))# es un string


#calculo de interes anual
interes_anual=4/100 
#calculo de interes acumulado, se le agrega un 1 delante al calculo del interes anual
interes_acumulado=1+4/100

listado2=[1,6,8,"avion",16,81,14,5,"ventilador",6,13,81,"ventilador",1,81,6,1,"ventilador",81]
print(listado2.count(1))
print(listado2.count(16))
print(listado2.count("avion"))
print(listado2.count(81))
print(listado2.count("ventilador"))
listado2.index(6)
print(f"El indice del numero 6 es: {listado2.index(6)}")
listado3=[3,"m",5,"y",11]
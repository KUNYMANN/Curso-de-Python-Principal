'UN METODO va a ser una nueva funcion que nos va a permitir crear nuevas utilidadades o que va acambiar el comportamiento de la string'
'cuando hablamos de metodos hablamos de palabras ya reservadas del lenguaje'
'algunos son Metodos que se repiten lenguaje con lenguaje, pero otros son propios de Python'

#METODOS DE CARACTERES
cadena='Estoy utilizando los Metodos de Python'
print(cadena) #con Shift + Alt mas flecha hacia abajo se duplica la linea 
print(cadena) #con Shift + Alt mas flecha hacia abajo se duplica la linea jajajajaj

#primero tengo que identificar a que variabe le voy a aplicar un metodo, luego un punto, recordemos que  cada metodo lleva sus propios ()
texto='Estoy utilizando los Metodos de Python' #dato STRING
#      0123456789 cada caracter dentro de un dato tiene asignado un indice y este comienza desde 0 
#      tambien se cuenta como caracter a los espacios vacios

print(texto.upper()) #si elegimos el metodo UPPER()automaticamente pasa todo el texto a MAYUSCULAS
print(texto.lower()) #si elegimos el metodo LOWER()automaticamente pasa todo el texto a minusculas
print(texto.capitalize()) #con capitalize coloca en mayusculas la primera letra de la primer palabra solamente, el resto quedara igual
print(texto.title()) # si elegimo el metodo TITLE()automaticamente pasa a mayuscula las primera letra de cada palabra Del Texto
print(cadena.swapcase())#cambia las MAYUSCULAS a minusculas y las minusculas a MAYUSCULAS
print(texto.find("M")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el caracter solicitado
print(texto.find("zando")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el 1er. caracter solicitado
print(texto.find("metodo")) #si elegimos el metodo FIND("")automaticamente busca en que INDICE esta colocado el 1er. caracter solicitado, pero ATENCION!!! que
# si colocamos mal el texto va a dar error (-1) porque la busqueda se realiza colocando exactamente como esta escrito, respetando si esta en mayuscula o minuscula

'LAS LISTAS ESTAN COMPUESTAS POR VARIOS ELEMENTOS'

'''es posible dividir un string con la funcion "split()". Un ejemplo sencillo de división es el siguiente:'''
text = "Esto es un ejemplo"
print(type(text)) # es un string
print(text.split()) #aqui el metodo split me divide a la frase en elementos de una la lista, utilizando para dividirla los espacios vacios
#El resultado quedaria asi:  ["Esto", "es", "un", "ejemplo"] en text ha sido dividida en todos sus espacios y se devolvió una lista de subcadenas
print(type(text.split())) # es una lista
mi_cadena="soy Hector, mi apodo es kuny, tengo 58 años, juego al basquet"
print(type(mi_cadena))# es un string
print(mi_cadena.split(",")) #aqui el método split() usando el parametro de division la "," devuelve una lista de mi cadena, donde cada parte de la frase 
#hasta la coma, es un elemento de la lista. ejemplo: "soy Hector" es un elemento, "mi apodo es kuny" es otro elemento, y asi sucesivamente
print(type(mi_cadena.split())) # es una lista
print("".join(mi_cadena)) #con el metodo .join() vuelvo a unir los elementos y los transforma en un solo elemento
mi_cadena1=["Manzanas","Naranjas","Peras","Platanos","Bayas"]
'dentro de las comillas puedo colocar con que caracter quiero que me los separe'
print("---".join(mi_cadena1))# con el metodo join.(insertar/unir) cambia las comas de una lista por el string elegido como inserto/union, en este caso es ---
print("***".join(mi_cadena1))# dado que python utiliza para las separaciones de una lista la coma ",".IMPORTANTE: ahora la lista, paso a convertirse en un string
print(type(mi_cadena1))# es una lista
print(type("---".join(mi_cadena1)))# es un string
palabra="Campeon"
print("*/*".join(palabra))#para Python una palabra por si sola, ya es una cadena, esto quiere decir que al no haber una lista de elementos a separar, python  va a concatenar
#letra por letra con el caracter o caracteres utilizado/s como incerto o separador
print(type(palabra))# es un string
print(texto.replace("Python","Kuny//"))#de esta manera se reemplaza al nuevo texto o parte del nuevo texto, los Slahs solo los coloque para identificar donde esta el cambio
nuevo_texto=texto.replace("utili","Calzada//") # los Slahs solo los coloque para identificar donde esta el cambio en consola, no cumplen ninguna funcion
print(texto,nuevo_texto)
print(texto.replace("e","X"))#Estoy utilizando los MXtodos dX Python (aqui no rremplazo la primer E porque esta en mayusculas 
                             #y Python lo toma como un caracter diferente al de la "e" minuscula)
print(texto.replace("",","))#cuando le damos el primer parametro vacio "", interpreta como que va a reemplazarce cada uno de los espacios al que va a separar cada caracter 
                            #por el segundo parametro que en este caso es una coma, pero puede ser cualquier caracter o string)
print(texto.replace("", "*/*"))# */*E*/*s*/*t*/*o*/*y*/* */*u*/*t*/*i*/*l*/*i*/*z*/*a*/*n*/*d*/*o*/* */*l*/*o*/*s*/* */*M*/*e*/*t*/*o*/*d*/*o*/*s*/* */*d*/*e*/* */*P*/*y*/*t*/*h*/*o*/*n*/*

#CREANDO UN CONJUNTO CONJUNTO O SET
conjunto={"kunymann"  ,  "soy jugador de basquet" ,  "mido 1.87" ,  "kunymann"} #conjunto va siempre entre {llaves} 
lista=["kunymann" , "soy jugador de basquet" , "mido 1.87" , "kunymann"] #lista va siempre entre [corchetes] se pueden duplicar datos
tupla=("kunymann" , "soy jugador de basquet" , "mido 1.87" , "kunymann") #tupla va siempre entre (parentesis) se pueden duplicar datos
print(lista) #se pueden duplicar datos
print(tupla) #se pueden duplicar datos
print(conjunto) #no se pueden duplicar datos y no se puede llamar a los elementos por su indice [0,1,2,3, etc.]



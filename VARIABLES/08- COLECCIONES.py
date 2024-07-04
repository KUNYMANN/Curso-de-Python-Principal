#Listas: son algo parecidas a lo que se conoce en otros lenguajes de programacion
# como los arreglos o vectores, son estructuras de datos mas flexibles, se pueden almacenar valores
# numéricos, tipo cadenas, booleanos e inclusive otras listas, las listas se delimitan por [] y en su
# interior los elementos se separan por comas
lista=["lunes","martes","miercoles","jueves","viernes"] #qui tenemos una lista
#indice   0        1         2         3          4  de esta manera se solicita el print para indicar que elementos queremos imprimir
#         1        2         3         4          5  asi toma python para indicar cuantos elementos hay en una la lista
print(lista)#con este print va a escribir toda la lista, 
print(lista[:])
#pero si yo necesito que imprima un solo elemento de la lista lo hago de la siguiente manera
print(lista[2]) #aqui entre corchetes indicamos el numero de indice donde se encuenta el valor que queremos imprimir
#con LISTA podemos imprimir desde el primero al ultimo de los elementos detallados siempre se empieza desde el indice cero
#Ejemplo
print(lista[0])# lunes
print(lista[1])# martes
print(lista[2])# miercoles
print(lista[3])# jueves
print(lista[4])# viernes
#pero tambien podemos hacerlo a la inversa y python toma como primer indice al ultimo, y se imprime utilizando numeros negativos
#desde el final hacia el principio comenzando por -1 (no existe el -0)
#Ejemplo
print(lista[-1])# viernes
print(lista[-2])# jueves
print(lista[-3])# miercoles
print(lista[-4])# martes
print(lista[-5])# lunes

print(lista[0:3])
print(lista[:3])
print(lista[2:5])
print(lista[2:])
print(lista[0:-4])
#qui tenemos una lista que almacena distintos tipos de datos
#se pueden colocar        cadenas de textos             Nº enteros (int)   Nº decimales (float)  booleanos
lista=["lunes","martes","miercoles","jueves","viernes",   1, 2, 3, 4, 0,     11.36, 9.5, 7.84,     True]  
#indices  0        1         2         3          4       5  6  7  8  9        10   11    12        13 de esta manera se solicita el print para indicar que elementos queremos imprimir
#         1        2         3         4          5       6  7  8  9  10       11   12    13        14 asi toma python para indicar cuantos elementos hay en una la lista
#siempre se cuenta el indice 0 como el 1er. elemento y asi sucesivamente, en este ejemplo serian 14 elementos
print(lista)
print(len(lista)) 
print(lista[9])
print(lista[3:11])


# aqui hay una sub lista () y se cuenta como un solo elemento
lista=["lunes","martes","miercoles","jueves","viernes",   1, 2, 3, 4, 0, [11.36, 9.5, 7.84], True]  
#indices  0        1         2         3          4       5  6  7  8  9           10          11
#         1        2         3         4          5       6  7  8  9  10          11          12 asi toma python para indicar cuantos elementos hay en la lista
#siempre se cuenta el indice 0 como el 1er. elemento y asi sucesivamente, en este ejemplo serian 12 elementos
print(len(lista)) 
print(lista[10:11]) 
print(lista[8:12]) 
print(lista[2:14]) 

lista1=[1,2,3,4,5]
lista1.append(3) #con la funcion append sepuede agregar un elemento mas al final de la lista 
lista1.append("kuny")
lista1.append(56.81)
print(lista1)

lista2=[1,2,3,4,5,"perro",35.8,"elefante",9,10 ]
lista2.insert(6,24.67) #con la funcion insert() puedo ingresar un elemento 
# indicandole despues de que elemento deseo ingresarlo aqui le estoy diciendo que desues del indice 6 
lista2.insert(8,"cafe")
print(lista2)

lista3=[1,2,3,4,5,"perro",35.8,"cafe","elefante",9,10 ]
lista3.extend([11,12,"anana",13,22.59,"perla"])# con la funcion extend([]) podemos agregar varios elementos al 
#final de una lista
print(lista3)

listado=[1,6,8,"avion",16,81,14,5,"ventilador"]
print(listado.index(14)) #con la funcion index()podemos averiguar en que indice se ubica un elemento 
print(listado.index("avion"))


lista4=["coco", 12, "gato", 13.55]
lista5=["araña","tela",84]
print(lista4+lista5) #podemos sumar dos listas
print("cafe" in lista5)    #con la funcion "in" podemos averiguar si un elemento esta dentro de la lista
print("cafe" in lista3)    # y nos va a decir si esta (true) y si no esta (false)
print("perla" in lista3)   # inclusive si el elemento que busquemos se encuentre incluido dentro de un extend() de la lista a explorar

listado2=[1,6,8,"avion",16,81,14,5,"ventilador",6,13,81,"ventilador",1,81,6,1,"ventilador",81]
print(listado2.count(1))
print(listado2.count(16))
print(listado2.count("avion"))
print(listado2.count(81))
print(listado2.count("ventilador"))
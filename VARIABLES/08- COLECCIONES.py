#Listas: son algo parecidas a lo que se conoce en otros lenguajes de programacion
# como los arreglos o vectores, son estructuras de datos mas flexibles, se pueden almacenar valores
# numéricos, tipo cadenas, booleanos e inclusive otras listas, las listas se delimitan por [] y en su
# interior los elementos se separan por comas
lista=["lunes","martes","miercoles","jueves","viernes"] #qui tenemos una lista
#indice   0        1         2         3          4
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
#indices  0        1         2         3          4       5  6  7  8  9        10   11    12        13 
print(lista)
print(lista[9])
print(lista[3:11])
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
#aqui podemos solicitar que nos muestre en el print una seccion de numeros en especial
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


# aqui hay una sub lista, se cuenta como un solo elemento, es la que esta encerrada entre [] dentro de la lista[a,b[c],d]
lista=["lunes","martes","miercoles","jueves","viernes",   1, 2, 3, 4, 0, [11.36, 9.5, 7.84], True]  
#indices  0        1         2         3          4       5  6  7  8  9     10 sub-lista      11
#         1        2         3         4          5       6  7  8  9  10    11 sub-lista      12 asi toma python para indicar cuantos elementos hay en la lista
#siempre se cuenta el indice 0 como el 1er. elemento y asi sucesivamente, en este ejemplo serian 12 elementos
print(len(lista)) 
print(lista[10:11]) 
print(lista[8:12]) 
print(lista[2:14]) 

lista1=[1,2,3,4,5]
lista1.append(3) #con la funcion append se puede agregar un elemento mas al final de la lista 
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

listado3=[3,"m",5,"y",11]
listado3.pop() #con el metodo .pop(vacio) elimina el ultimo elemento del listado o tambien podemos pasarle el indice que queremos eliminar ejemplo: .pop (2)
print(listado3)
listado3.pop(2) #aqui va a eliminar el indice 2 en este caso seria el 5,  ya que el 3 es indice 0, "m" es el indice 1 y el 5 es el indice 2
print(listado3)

listado4=[1,6,8,"avion",16,81,14,5,"ventilador",6,13,81]
listado4.remove("avion") #con este metodo se puede eliminar un elemento por el nombre si no se sabe en que indice se encuentra                 
print(listado4)

listado5=[1,6,8,"avion",16,81,14,5,"ventilador",6,13,81]
listado5.clear() #con este metodo eliminamos toda la lista de elementos
print(listado5)

listado6=[1,6,8,"avion",16,81,14,5,"ventilador",6,13,81]
listado6.reverse()#con este metodo invertimos el listado de elementos manteniendo el orden
print(listado6)

listado7=[3,"m",5,"y",11]*2 #de esta manera duplicamos la lista de elemento o por tantas veces que querramos
print(listado7)

listado8=[-23,1,2,-17,3,-11.5,4,5,-9,18.64]
listado8.sort()
print(listado8)
listado8.sort(reverse=True)
print(listado8)

lenguajes=["Python","Ruby", "PHP","Javascript","Java"]
#indice       0       1       2         3         4 
print(lenguajes[0]) # de esta manera se solicita un indice en espcial correspondiente al dato
lenguajes[1]="HTML" # cuando quiero cambiar algun dato de la lista, cambiamos el valor del indice 1 "Rubi" por "HTML"
print(lenguajes)
print(lenguajes[-1]) #imprime el ultimo esta manera es una solicitud DESCENDENTE
print(lenguajes[-2]) #imprime el antepenultimo y asi sucesivamente dependiendo del dato que solicite 
#RECORDEMOS que hemos cambiado el valor del indice 1 "Rubi" por "HTML"
print(lenguajes[1:3])#imprime los elementos que queremos seleccionar "de donde : hasta donde", 
      #el 1 significa desde donde queremos que empiece : y el 3 hasta donde queremos que muestre, 
      # no va a incluir el valor 3 porque ese es el limite de busqueda.
print(lenguajes[:3])# de esta manera quiere decir que va a incluir desde el indice cero :3 por mas
                    #que no este escrito queda implicito
print(lenguajes[1:])#igualmente de esta manera, va a mostrar desde el indice indicado hasta el final,
#ya que al no tener un parametro de busqueda final, se sobreentiende que quiere que muestre los valores hasta el final      


lenguajes=["Python","Ruby", "PHP","Javascript","Java"]
#como INSERTAR elementos
lenguajes.insert(3, "HTML")
lenguajes.insert(0,"Word")
print(lenguajes)
#como ELIMINAR elementos
lenguajes.remove("Ruby")
print(lenguajes)
#como PREGUNTAR si existe un elemento dentro de la lista
print("PHP"in lenguajes)#si esta dentro del listado dira True, si no esta dira False
print(len(lenguajes)) #acceder cuantos elementos contiene un listado
lenguajes.clear() #para limpiar el listado y que no contenga absolutamente nada
print(lenguajes)

#ejemplo: 
coloque_su_clave=input("coloque la clave: ") 
print(coloque_su_clave)
#y si solicito que sea un numero (ya que los numeros son float) 
#ejemplo:  
temperatura= float(input("ingrese la temperatura: "))
print(temperatura)

#CUANDO TENEMOS VARIOS ELEMENTOS QUE QUEREMOS MOSTRAR SE COLOCAN EN UNA LISTA O EL NOMBRE QUE LE QUERRAMOS ASIGNAR
listas=["kunymann" , "Soy juegador basquet" , "1.87"]
#LO PEDIMOS PARA QUE LO MUESTRE ASI
print(listas)
#SIN EMBARGO PUEDO PEDIR QUE ME MUESTRE PUNTIUALMENTE ALGUN DATO EN ESPECIAL DE LA (LISTA SE HACE ASI entre [ ]) 
#TENER EN CUENTA QUE EN PROGRAMACION (LA NUMERACION SIEMPRE EMPIEZA DEL 0 ya que el indice esta en la posicion 0),
# segun el ejemplo "Kunymann" es el elemento 0, "Soy jugador de basquet" es el 1, "mido 1.87" es el 2 y asi sucesivamnte
lista12=["Kunymann" , "Soy juegador de basquet" , "mido 1.87"]
print(lista12[0])
print(lista12[2])
print(lista12[1])
#TAMBIEN EXISTE LA VARIANTE tupla= y se escriben los datos entre  ( ) pero esta lista de datos asignados no se puede modificar
tupla=("Kunymann" , "Soy juegador de basquet" , "mido 1.87")
print(tupla[0])
#EN EL MODO LISTA= SIGNIFICA QUE PUEDO REEMPLAZAR LA VARIABLE 
#EN ESTE CASO REEMPLAZO "mido 1.87" QUE FIGURA EN EL INDICE 2,  por la palabra "genio"
lista[2]= "genio"
print(lista[2])
#EN CAMBIO MODO EN TUPLA NO SE PUEDE REEMPLAZAR,NO ES VALIDO, EN ESE CASO DARIA ERROR EL PRINT
# print(tupa[2]) #NameError: name 'tupa' is not defined. Did you mean: 'tupla'

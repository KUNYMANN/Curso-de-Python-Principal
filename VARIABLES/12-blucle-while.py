lenguajes=["Python","Ruby", "PHP","Javascript","Java"]
#si yo quisiera mostrar la cantidad de elementos de una lista uno por uno es engorroso de esta manera
print(lenguajes[0]) 
print(lenguajes[1]) 
print(lenguajes[2]) 
print(lenguajes[3]) 
print(lenguajes[4]) 
#EL BUCLE DE WHILE ES COMO ACCEDER A LOS NOMBRES DE LOS ELEMENTOS DE UN LISTADO DE UNA FORMA MAS RAPIDA Y AGIL
#Ejemplo
i=0
while i<len(lenguajes):
    print(lenguajes[i])
    i=i+1


#LO MEJOR ES UTILIZAR UN BUCLE DE "WHILE" este nos permite buscar dentro de una lista la cantidad de elementos
# dandole un parametro de busqueda
#Ejemplo 
i=0     # "i" representa un valor inicial, si tomo el 0 como valor de inicio
        # debo contarlo como un elemento mas de la lista(0-1-2-3-4) son 5 elementos
while i<=4:
    print(i)
    i=i+2
    
i=1
while i<=5:
    print(i)
    i=i+1

#TAMBIEN podemos utilizar el BUCLE DE WHILE para que nos muestre la cantidad de elementos
#utilizando como representacion un texto
#Ejemplo
i=1
while i<=5:   #parametro de busqueda
    print(i*"HEZ") #que imprimir por consola cuando evalue
    i=i+1 #indice de evaluacion


i=1
while i<=5:
    print(i)
    i=i+1


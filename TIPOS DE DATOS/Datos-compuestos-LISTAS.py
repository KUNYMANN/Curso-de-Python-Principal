#CUANDO TENEMOS VARIOS ELEMENTOS QUE QUEREMOS MOSTRAR SE COLOCAN EN UNA LISTA O EL NOMBRE QUE LE QUERRAMOS ASIGNAR
lista=["kunymann" , "Soy juegador basquet" , "1.87"]
#LO PEDIMOS PARA QUE LO MUESTRE ASI
print(lista)
#SIN EMBARGO PUEDO PEDIR QUE ME MUESTRE PUNTIUALMENTE ALGUN DATO EN ESPECIAL DE LA (LISTA SE HACE ASI entre [ ]) 
#TENER EN CUENTA QUE EN PROGRAMACION (LA NUMERACION SIEMPRE EMPIEZA DEL 0 ya que el indice esta en la posicion 0),
# segun el ejemplo "Kunymann" es el elemento 0, "Soy jugador de basquet" es el 1, "mido 1.87" es el 2 y asi sucesivamnte
lista=["Kunymann" , "Soy juegador de basquet" , "mido 1.87"]
print(lista[0])
print(lista[2])
print(lista[1])
#TAMBIEN EXISTE LA VARIANTE tupla= y se escriben los datos entre  ( ) pero esta lista de datos asignados no se puede modificar
tupla=("Kunymann" , "Soy juegador de basquet" , "mido 1.87")
print(tupla[0])
#EN EL MODO LISTA= SIGNIFICA QUE PUEDO REEMPLAZAR LA VARIABLE 
#EN ESTE CASO REEMPLAZO "mido 1.87" QUE FIGURA EN EL INDICE 2,  por la palabra "genio"
lista[2]= "genio"
print(lista[2])
#EN CAMBIO MODO EN TUPLA NO SE PUEDE REEMPLAZAR,NO ES VALIDO, EN ESE CASO DARIA ERROR EL PRINT
# print(tupa[2]) #NameError: name 'tupa' is not defined. Did you mean: 'tupla'









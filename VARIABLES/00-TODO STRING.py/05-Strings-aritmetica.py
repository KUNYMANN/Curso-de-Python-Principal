#CONCATENACION de STRINGS

cadena="Hola Kuny"
cadena1="Mann"
print(cadena + cadena1) #Hola KunyMann (con el + se suma al ultimo caracter del texto)
print(cadena,cadena1) #Hola Kuny Mann (con la , se agrega al texto)
print("Buenas tardes: " + cadena+cadena1)
print("Buenas tardes: " + cadena,cadena1)
print("Buenas tardes: " , cadena,cadena1)

#SI EN LA CONCATENACION QUIERO DESTACAR ALGO DENTRO DEL STRING  usando ''
cadena="Hola 'Kuny'"
cadena1="Mann"
print(cadena + cadena1) #Hola KunyMann (con el + se suma al ultimo caracter del texto)
print(cadena,cadena1) #Hola Kuny Mann (con la , se agrega al texto)
print("Buenas tardes: " + cadena+cadena1)
print("Buenas tardes: " + cadena,cadena1)
print("Buenas tardes: " , cadena,cadena1)

#CONCATENACION de NUMEROS
'no se puede concatenar con + un numero y un texto, para ello hay que pasar el numero a strings'
cadena="Hola 'Kuny'"
cadena1="Mann"
numero=1980
print(numero,"Buenas tardes: "+cadena)
print(numero,"Buenas tardes: ",cadena)
#€jemplo del error concatenacion
# print(numero + "Buenas tardes: " + cadena) de esta manera da error porque no se puede 
# concatenar con + un numero y un texto, para ello hay que pasar el numero a strings
print(str(numero) + " Buenas tardes: " + cadena)

print(str(numero)+" Buenas tardes: "+cadena+cadena1)
print(numero,"Buenas tardes: "+ cadena+cadena1)
print(numero,"Buenas tardes: ", cadena+cadena1)
print(numero,"Buenas tardes: ", cadena,cadena1)
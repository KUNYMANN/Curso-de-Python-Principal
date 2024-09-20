#CONCATENACION de STRINGS
'La concatenacion de cadenas es una operacion que permite conbinar dos o mas cadenas para formar una nueva cadena'

#El Operador "+"
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
numero=1966
print(numero,"Buenas tardes: "+cadena)
print(numero,"Buenas tardes: ",cadena)
print(type(numero))
#€jemplo del error concatenacion
# print(numero + "Buenas tardes: " + cadena) de esta manera da error porque no se puede 
# concatenar con + un numero y un texto, para ello hay que pasar el numero a strings
print(str(numero) + " Buenas tardes: " + '' + cadena)

print(str(numero)+" Buenas tardes: "+cadena+cadena1)
print(numero,"Buenas tardes: "+ cadena+cadena1)
print(numero,"Buenas tardes: ", cadena+cadena1)
print(numero,"Buenas tardes: ", cadena,cadena1)

#Metodo .join([]) nos permite dentro de una nueva variable, unir tantas cadenas de distintas variables como querramos
# se introducen dentro del los parentesis del metodo, seguido de corchetes, ahi colocamos las distintas cadenas a concatenar
# separadas por una ","(coma), Para SABER: lo que vamos a ingresar dentro de los corchetes es una Lista de variables, por medio de la
# concatenacion de todas esas listas de variables que contienen cadenas, van a generar una nueva cadena uniendo a todas las listadas
datos_peronales="".join([cadena,' ',cadena1," ",str(numero)])#las comillas vacias con un espacio en su interior generan un espacio en blanco por consola
print(datos_peronales)
print(type(datos_peronales))
print(datos_peronales[0])
listado="DNI 17.724.294"
padron=''.join([datos_peronales," ",listado])
print(padron)

#FORMATEO DE CADENAS
'''PYTHON ofrece varias maneras de formatear cadenas, que incluyen la capacidad de concatenar textos, 
incluir variables e incluso dar otro tipo de formateo a nuestras variables, 
como por ejemplo indicar el numero de decimales a utilizar para mandar a imprimir un valor decimal '''

#EL FORMATEO ES UNA TECNICA QUE NOS PERMITE INCLUIR: TEXTO, VARIABLES, EXPRESIONES E INCLUSO DAR CIERTOS FORMATOS A NUESTRAS CADENAS

'1-Metodo "f.string()" conocida como "f strig literal", es la opcion mas recomendada, por ser sencilla, rapida y legible'
#para incluir dentro de f una variable se realiza con {}
saludo1=f'Congratulation {padron}'
print(saludo1)

'2-Metodo format, aunque menos usado es muy versatil y permite construir cadenas muy complejas'
saludo2='Congratulation {}'.format(padron)
print(saludo2)


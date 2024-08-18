#STRING
'La clase str en Python se utiliza para representar "texto", más conocido en el mundo de la programación como string o cadena de caracteres'
'''el tipo str es una secuencia inmutable de caracteres Unicode. Por tanto, al igual que "list", "tuple" o "range", es un tipo secuencial y como es inmutable, 
un objeto de este tipo no se puede modificar después de haber sido creado.'''
string="texto"
print(string)



#for str Python – se utiliza "for c in" y el nombre de la variable  en el print va a recorrer los caracteres de una cadena
saludos="HOLA"
for c in saludos:
   print(c)
# con la funcion "in" podemos saber si algun caracter esta contenido dentro del string o cadena 
# y al ser una comparacion arrojara un booleano
saludo="hola"
print ("o" in saludo)
print("r" in saludo)
#y negando lo falso con "not in" (no es cierto) que tal caracter este dentro del valor de la variable 
print("p" not in saludo)#es verdadero, porque en este caso la "p" no esta dentro de la variable "hola", 
                        #o lo que es lo mismo decir 'si, "p" no esta dentro de la palabra "hola"'

#Comprobar si dos strings son iguales en Python, como es una comparacion arrojara un booleano
'para comparar si dos cadenas de caracteres son iguales, se utiliza el operador de igualdad =='

a="hola"
b="hola"
print(a==b) #True
'''Dos strings son iguales "si y solo si" ambas cadenas contienen la misma secuencia de caracteres
 (se distingue entre mayúsculas y minúsculas).
'''
c="holA"
print(a==c) #False (porque la A del final de la palabra esta en mayusculas)

#Longitud de una cadena en Python
'para obtener la longitud de una cadena se debe utilizar la función de Python len()'
cadena="motocicleta"
print(len(cadena))

#para resaltar un string dentro de otro string
'en un solo renglon si usas comillas simples para crear el string, para resaltar se utilizan las dobles o viseversa tantas veces como las necesites'
s='Hola "rey" ¿Te gusta Python?'
print(s)
s="Hola 'genio' ¿Te gusta Python?"
print(s)

'si el texto esta en varios renglones para lo cual se utilizan tres comillas dobles """ """ asi que solo se utilizara para resaltar comillas simples'
s=("""'Hola'
 'kuny'
 '¿Te gusta Python?'""")
print(s)

'si queremos que el texto salga impreso en un solo renglon utilizamos el slash "\"'
t=("""'Hola\
 'santi'\
  ¿Te gusta Python?'""")
print(t)
'si el texto esta en un solo renglon y queremos que lo imprima en varios renglones utilizamos"\n"'
n="\neste\nstring\nocupa\nmuchos\n lugares" #si aplico un espacio en n\ y la palabra lo imprimira tambien por consola
print(n)
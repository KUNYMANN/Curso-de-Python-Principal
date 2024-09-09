'''El usuario es quien va a digitar los datos pero esos datos debemos saber bien de que tipo son para evitar conflictos, 
estos datos se van a almacenar en una variable, esa variable va a contener los datos que usuario digite, cuando vamos a
manupilarlos hay que tenes cuidado porque son variables que con el tiempo pueden llegar a variar conforme pasa el tiempo
ejemplo: de entero a flotante, de flotabnte a cadena de texto y asi con cada uno de los datos '''

'''ATENCION!!!
Cual es la importancia de los datos ingresados, SU UTILIZACION ya sea para concatenarlos o para realizar operaciones aritmeticas'''

#INPUT es una funcion que nos permite obtener datos del usuario

nombre=input("coloque aqui su nombre: ".upper())#indicando el metodo .upper() estoy imprimiendo por pantalla el texto en MAYUSCULAS

edad=int(input("coloque aqui su edad: "))# si yo no especifico que ingrese un numero entero (int) o flotante (float), si o si el numero ingresado va a ser un string
print(type(edad)) #Como estoy solicitando un numero entero, el tipo de dato va a ser un int

edad0=float(input("Coloque aqui la edad y meses transcurridos desde la ultima fecha de cumpleaños: "))
print(type(edad0)) #Como estoy solicitando un numero con decimales, el tipo de dato va a ser un float

edad1=input("coloque aqui su edad ficticia: ")
print(type(edad1))#como no estoy especificando que tipo de numero tiene que ingresar, el tipo de dato va a ser un string

print(f"Usted tiene por nombre {nombre.upper()} y su edad es {edad} años")

resultado=input("Ingresa tu edad: ") #input es una funcion que nos permite obtener datos del usuario
print(resultado)
print(type(resultado))#aqui me esta diciendo que el resultado es un texto (str) y 
                      #eso implica que no puede utilizarlo para realizar una operacion matematica
#EJEMPLO
#print(resultado + 22) #va arrojar un error porque no puede sumar un texto con un numero (string+number)
                      #solo puede concatenar un string con otro string 
print(resultado + "22" , 'aqui lo esta concatenando como string') #de esta manera no va arrojar un error porque lo esta tomando como un string, o sea un texto, no un numero (string+string)
                         #solo se puede concatenar un string con otro string 
print(type(resultado))

nombre = input("Digite su nombre: ")
print(f"Hola {nombre} bienvenido!!!")

"IMPORTANTE"
"""los numeros guardados en IMPUT son string, SALVO QUE SE INDIQUE LO CONTRARIO"""

#si queremos que el numero ingresado sea un entero se solicita asi:
#para numeros INT (enteros)
numero=int(input("Digite un numero entero: "))# esta es la manera de comprobar que el numero esta tomado como numero entero y no como un texto (string)
print(f"el numero es {numero +2} porque le acabo de sumar dos")# aqui se puede realizar cualquier operatoria aritmetica
numero=int(input("Digite un numero entero: "))# esta es la manera de comprobar que el numero esta tomado como entero (int) y no como un texto (string)
print(f"el numero es {numero +4*(6**3/2)-3} por la funcion que le agregue")# aqui se puede realizar cualquier operatoria aritmetica

#si queremos que el numero ingresado sea con decimales se solicita asi:
#para numeros FLOAT (con decimales)
numero=float(input("Digite un numero con decimales: "))# esta es la manera de comprobar que el numero esta tomado como tal no como un texto (string)
print(f"el numero es {numero *2} porque lo multiplique por dos")# aqui se puede realizar cualquier operatoria aritmetica

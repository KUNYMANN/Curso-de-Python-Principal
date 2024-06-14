resultado=input("Ingresa tu edad: ") #input es una funcionque nos permite obtener datos del usuario
print(resultado)
print(type(resultado))#aqui me esta diciendo que el resultado es un texto (str) y 
                      #eso implica que no puede utilizarlo para realizar una operacion matematica
#EJEMPLO
#print(resultado + 22) #va arrojar un error porque no puede sumar un texto con un numero (string+number)
                      #solo puede concatenar un string con otro string 
print(resultado + "22" ) #de esta manera no va arrojar un error porque lo esta tomando como un string, un texto no un numero (string+string)
                      #solo puede concatenar un string con otro string 
print(type(resultado))

"IMPORTANTE"
#los numeros guardados en IMPUT son string

nombre = input("Digite su nombre: ")
print(f"Hola {nombre} bienvenido!!!")

#para que los numeros en INPUT sean tomados como INT o FLOAT (tipos de numeros) se hace de la siguiente manera

#para numeros INT (enteros)
numero=int(input("Digite un numero entero: "))# esta es la manera de comprobar que el numero esta tomado como tal no como un texto (string)
print(f"el numero es {numero +2}")# aqui se puede realizar cualquier operatoria aritmetica

numero=int(input("Digite un numero entero: "))# esta es la manera de comprobar que el numero esta tomado como tal no como un texto (string)
print(f"el numero es {numero +4*(6**3/2)-3}")# aqui se puede realizar cualquier operatoria aritmetica

#para numeros FLOAT (con decimales)
numero=float(input("Digite un numero con decimales: "))# esta es la manera de comprobar que el numero esta tomado como tal no como un texto (string)
print(f"el numero es {numero *2}")# aqui se puede realizar cualquier operatoria aritmetica

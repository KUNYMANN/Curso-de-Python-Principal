
# Condicionales combinados o anidados
#los condicionales son estructuras de codigos que nos van a servir, para que nuestro programa sea mas "inteligente"
# y sea capaz de tomar desiciones en ciertas cosas
numero=10 #si este numero fuera menor o igual a 7 no se ejecutaria nada porque la condicion if es que sea mayor que 7
if numero>7:  # aqui utilizamos if que es una condicion de que "numero" sea mayor que para que se realice o ejecute el codigo que
              # le pidamos a partir de los dos puntos
    print("el numero es mayor que 7.") #aqui dentro escribiremos el codigo que querramos que se ejecute, y se va a ejecutar si se cumple la condicion if
else:         #else esta siempre sujeto a que haya un if y no se coloca nunca una condicion, el mensaje que va a ejecutar contempla cualquier otra posibilidad
              #que no sea indicada en el if
    print("el numero es menor o igual a 7.")

numero=5 
if numero>7: 
    print("el numero es mayor que 7.") #aqui dentro escribiremos el codigo que querramos que se ejecute, y se va a ejecutar si se cumple la condicion if
else:         #else esta siempre sujeto a que haya un if y no se coloca nunca una condicion, el mensaje que va a ejecutar contempla cualquier otra posibilidad
              #que no sea indicada en el if
    print("el numero es menor o igual a 7.")

#Pero no todo es uno u otro tambien puede haber conciones intermedias ahi es cuando aparece elif
numero=7 
if numero>7: 
    print("el numero es mayor que 7.") #aqui dentro escribiremos el codigo que querramos que se ejecute, y se va a ejecutar si se cumple la condicion if
elif numero==7: #Elif se va a ejecutar si la primer condicion if no es verdadera (False)
    print("El numero es igual a 7.")
else:         #else esta siempre sujeto a que no se cumplan las condiciones de  if (False) y elif (False),  luego imprimira la condicion restante
    print("el numero es menor a 7.")


#¿como toma el programa esta desiciones? 
# por el tipo de datos booleanos
#Si la expresion del if se cumple quiere decir que es verdadera arroja un booleano True, 
# en cambio si no es verdadera la condicion if entonces arroja un booleano False,  
# esto automaticamente pasa a ejecutarse la siguiente condidcion que es el elif
# y si no se dan as condiciones anteriores (osea que todas arrogen un False. 
# se ejecuta indefectiblemente el else
#EN RESUMEN, SI EN IF TENEMOS UN TRUE SE EJECUTA, SI TENEMOS UN FALSE PASA A EJECUTARSE LA SIGUIENTE CONDICION ELIF QUE SI ARROJA UN TRUE LO EJECUTA
#Y ASI SUCECIVAMENTE HASTA QUE ARROJE UN FALSE EN ESE CASO AUTOMATICAMENTE SE EJECUTA LA CONDICION ELSE QUE ES LA RESTANTE DE LAS CONDICIONES 




vamos a solicitarle al usuario que digite su edad, que es un dato entero, 
ahora vamoa a calcular si este usuario es mayor de edad o no

edad=int(input("digite su edad: \n"))

if edad>0 and edad<100:  #aqui colocamos dos rangos o parametros,UNO que la edad sea mayor a cero y OTRO que la edad sea menor a cien
    print("Edad correcta")
    if edad>=18: # condicional anidado
        print("Eres mayor de edad")      
    else:
        print("Eres Menor de Edad")
else:
    print("Edad incorrecta")


# Otra forma mas corta 
edad=int(input("digite su edad: "))
if 0<edad<100: #aca los rangos estan solicitados de una manera mas corta
    print("Edad correcta")
    if edad>=18 and edad<100: # condicional anidado
        print("Eres mayor de edad")      
else:
    print("Edad incorrecta")

# EJEMPLAZOOOOOOOOO

nacionalidad=input("Coloque su Nacionalidad: ".capitalize())
edad=int(input("Coloque su edad: ".capitalize()))
if nacionalidad.capitalize() == "Argentina":
    if edad>18:
        print("BIenvenido COMPATRIOTA")
    else:
        papas=input("Viene acompañado de sus padres?: ".capitalize())
        if papas.capitalize()=="Si":
            print("BIenvenido")
        else:
            print("CHAU")

elif nacionalidad == "Italiano":
    if edad>18 :
        print("BENVENUTTO")
    else:
        papas=input("Viene acompañado de sus padres?: ".capitalize())
        if papas.capitalize()=="Si":
            print("BENVENUTISSSSS")
        else:
            print("FUORA")

else:
    if edad>18:
        print("HELLO")
    else:
        papas=input("Viene acompañado de sus padres?: ".capitalize())
        if papas.capitalize()=="Si":
            print("WELCOME")
        else:
            print("GOOD BYE")


edad=int(input("Ingrese su edad: \n"))
respuesta=None

if edad>=18:
    print("Eres Mayor de edad, puedes comprar alcohol, ¿Cual deseas?. ingrese un codigo del Menu")
    respuesta=(input("1-Ron.\n2-Whisky.\n3-Giniebra.\n"))


    if respuesta=="1":
        print("Has elegido Ron ")
    elif respuesta=="2":
        print("Has elegido Whisky")

    elif respuesta=="3":
        print("Has elegido Giniebre") 
    else:
        print("Has ingresado mal el codigo")
else:
    print("Eres Menor de edad chaval no puedes tomar alcohol")


def main():
    print("DIVISOR DE NÚMEROS")
    dividendo = int(input("Escriba el dividendo: "))
    divisor = int(input("Escriba el divisor: "))

    cociente = dividendo // divisor
    resto = dividendo % divisor

    if resto == 0:
        print(f"La división es exacta. Cociente: {cociente}")
    else:
        print(f"La división no es exacta. Cociente: {cociente} Resto: {resto}")


if __name__ == "__main__":
    main()

dividendo=float(input("Escriba un numero dividendo: "))
divisor=float(input("Coloque un numero divisor: "))
if dividendo%divisor==0:
    print(f"La division es exacta. Cociente: {dividendo//divisor}")
else:
    print(f"La division no es exacta el cociente es: {dividendo//divisor} y el resto es :{dividendo%divisor}")

def main():
    print("DIVISOR DE NÚMEROS")
    dividendo = int(input("Escriba el dividendo: "))
    divisor = int(input("Escriba el divisor: "))

    if dividendo % divisor:
        print(
            f"La división no es exacta. Cociente: {dividendo // divisor} "
            f"Resto: {dividendo % divisor}"
        )
    else:
        print(f"La división es exacta. Cociente: {dividendo // divisor}")


if __name__ == "__main__":
    main()


print("COMPARADOR DE NUMEROS")
numeroA=float(input("Ingrese un numero: "))
numeroB=float(input("Ingrese otro numero: "))

if numeroA<numeroB:
    print(f"Menor: {numeroA:.2F}; Mayor: {numeroB:.2F}")
elif numeroA>numeroB:
    print(f"Menor: {numeroB:.2F}; Mayor: {numeroA:.2F}")
else:
    print("Ambos numeros son iguales")

#asi lo habia hecho 
print("COMPARADOR DE AÑOS")
año=int(input("En que año estamos: "))
cualquiera=int(input("Ingrese un año cualquiera: "))
restan=cualquiera-año
pasaron=año-cualquiera

if restan==1:
    print (f"Falta solo {restan} año para el {cualquiera}")
elif pasaron==1:
    print (f"Paso solo {pasaron} año desde el {año}")
elif año<cualquiera:
    print(f"Faltan {restan} años para que llegue {año}")
elif año>cualquiera:
    print(f"Ya han pasado {pasaron} años desde {cualquiera}")
else:
    print("Estamos en el mismo año")

#asi esta mejorado (un toke nomas jajjajaja)
print("COMPARADOR DE AÑOS")
año=int(input("En que año estamos: "))
cualquiera=int(input("Ingrese un año cualquiera: "))

if cualquiera-año==1:
    print (f"Falta solo {cualquiera-año} año para el {cualquiera}")
elif año-cualquiera==1:
    print (f"Paso solo {año-cualquiera} año desde el {año}")
elif año<cualquiera:
    print(f"Faltan {cualquiera-año} años para que llegue {año}")
elif año>cualquiera:
    print(f"Ya han pasado {año-cualquiera} años desde {cualquiera}")
else:
    print("Estamos en el mismo año")

print("COMPARADOR DE MULTIPLOS\t")
numeroX=int(input("Ingrese un numero: "))
numeroZ=int(input("Ingrese otro numero: "))
if numeroX==numeroZ:
    print(f"{numeroX} es multiplo de {numeroZ}")
elif numeroX<0 or numeroZ<0:
    print("No se admiten numeros negativos")
elif numeroX==0 or numeroZ==0:
    print("El Cero es multiplo de todos")  
elif numeroX%numeroZ==0:
    print(f"el primer numero ingresado {numeroX} es multiplo de {numeroZ} ")
elif numeroZ%numeroX==0:
    print(f"el segundo numero ingresado {numeroZ} es multiplo de {numeroX} ")
else:
    print(f"{numeroX} no es multiplo de {numeroZ} ")

print("COMPARADOR DE TRES NUMEROS")
comp1=int(input("Ingrese un numero: "))
comp2=int(input("Ingrese otro numero: "))
comp3=int(input("Ingrese un tercer numero: "))
if comp1==comp2 and comp2==comp3:
    print("Has ingresado tres veces el mismo numero")
elif comp1==comp3 or comp2==comp3 or comp1==comp2:
    print("Has ingresado dos veces el mismo numero") 
else:
    print("Los tres numeros son distintos")


print("COMPARADOR DE AÑOS BISIESTOS")
año=int(input("Escriba un año y le dire si es bisisesto:"))
if año%4!=0: # Aqui dice que si "año" dividido "4" su (resto"%") es (distinto"!=") de "O" 
    print (f"El año {año} no es un año bisiesto ")#....muestre tal cosa
elif año%100==0 and año%400!=0:# O si "año" es al dividirlo por "100" es (igual"==") a "0" (y "and") "año" dividido 400 su (resto"%") es (distinto"!=") de "O" 
    print(f"El año {año} no es un año bisiesto porque es múltiplo 100.") #....muestre tal otra
elif año%4==0 and año%100!=0: # O si "año" es al dividirlo por "4" es (igual"==") a "0" (y "and") "año" dividido 100 su (resto"%") es (distinto"!=") de "O"
    print(f"El año {año} es un año bisiesto porque es múltiplo de 4 sin ser múltiplo de 100.")#....muestre tal otra
else:
    print(f"El año {año} es un año bisiesto porque es múltiplo de 400.")# si no se cumple ninguna de las anteriores entonces muestre esto 

coeficienteA=float(input("Ingrese un coeficiente: "))
coeficienteB=float(input("Ingrese otro coeficiente: "))

if coeficienteA==0 and coeficienteB==0:
    print("Todos los números son solución.")
elif coeficienteA==0 and coeficienteB!=0:
    print("la ecuacion no tiene solucion")

else: 
    print(f"La ecuación tiene una solución: {-coeficienteB/coeficienteA} ")

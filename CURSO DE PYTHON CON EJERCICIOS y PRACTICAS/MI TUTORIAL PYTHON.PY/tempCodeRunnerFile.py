edad=int(input("Ingrese desde el teclado numerico su edad para saber si eres mayor o menor de edad: "))
if edad>=18 and edad<=100: #la condicion se cumple, en el caso que ingrese un numero mayor o igual a 18 y menor a 100
    print("Eres Mayor de edad") #entonces imprimira la siguiente leyenda "Eres mayor de edad"
elif 18>edad>=0: #si no se cumple la condicion anterior, pero para que se cumpla esta, el numero ingresado debe ser menor a 18 con un parametro minimo de 0 años
    print("Eres menor de edad")#entonces imprimira la siguiente leyenda "Eres menor de edad"
else: #en caso que se ingrese un numero mayor a 100 o algun numero negarivo
    print("Dato invalido") #entonces imprimira la siguiente leyenda "Dato invalido"'''

#Realizar las cuatro operaciones basicas (Suma, Resta, Multiplicacion y Division), el Usuario debe especificar tipo de operacion
#colocando el primer caracter del nombre de la operacion
operacion=input("coloque el caracter de la operacion que desea realizar: ").lower() #el .lower() transforma el caracter a minusculas
num1=float(input("coloque un numero: "))
num2=float(input("coloque un numero: "))



if operacion=="s":
    s=num1+num2
    print(f"\nEl resultado de la suma es: {s}") #colocando \nseguido del texto que deseamos imprimir el resultado lo mostrara haciendo un salto de renglon
elif operacion=="r":
    r=num1-num2
    print(f"\nEl resultado de la resta es: {r}")
elif operacion=="m" or operacion=="p":
    m=num1*num2 #aqui no hace falta ingresar la variable p=num1*num2 ya que esta especificado en el or ya que si el usuario ingresa
    #el caracter de M o P se esta refiriendo a la Multiplicacion o Producto
    print(f"\nEl resultado de la multiplicacion es: {m:.2f}") #aqui colocamos la expresion:.2f para mostrar el resultado con un maximo de dos decimales
elif operacion=="d":                                      # en caso de querer  mas los decimales solamente variamos el numero, ejemplo :.3f, :.4f, etc
    d=num1/num2
    print(f"\nEl resultado de la division es: {d:.2f}")
else:
    print("Error al ingresar la letra de la operacion que desea realizar")

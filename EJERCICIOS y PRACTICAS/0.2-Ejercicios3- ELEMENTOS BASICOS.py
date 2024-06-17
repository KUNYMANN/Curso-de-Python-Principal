#HACER UN PROGRAMA PARA INTERCAMBIAR EL VALOR DE DOS VARIABLES
a=10
b=5
a=5
b=10

#para un number INT o FLOAT
a=float(input("coloque el valor numerico de a: "))
b=float(input("coloque el valor numerico de b: "))
a,b=b,a
print("el nuevo valor para a es: ", a)
print("el nuevo valor para b es: ", b)


#para un STR (texto-cadena)
a=input("coloque el valor de texto de a: ")
b=input("coloque el valor de texto de b: ")
a,b=b,a
print(f"el nuevo valor para a es: {a}")
print(f"el nuevo valor para b es: {b}")
print([1])
print("***CICLO WHILE***")
#imprimir valores de 0 a 5
valores=0     #esta variable da el valor de inicio de la busqueda en este caso (0)
while valores<=5:  # aqui a while le estamos ordenando que busque a partir de la variable de inicio (0) lo que se encuentra dento del parametro asignado (o sea del 0 hasta el 5)
    print(valores) # aqui estamos diciendole que imprima cada objeto que encuentra dentro del valor asignado para la busqueda segun lo indicado, en el renglon siguiente,
    valores+=1 #con esto estamos diciendole a while de que manera queremos que realice la busqueda (+=1) significa de 1 en 1, podria ser (+=2) de 2 en 2, ect
print([2])
numero=1
while numero<=10:
    print(numero, end=" ") #de esta menera lo imprimira todo en un solo renglon separados por un espacio
    numero+=2
print()
print([3])
numero=1
while numero<=6:
    print(numero, end="-")
    numero+=2
print()
print([4])
contador=3
while contador<=9:
    print(contador)
    contador+=3
print([5])
contador=2
while contador<=6:
    print(contador, end='\n') #de esta menera lo imprimira en varios renglones, si asi requiere que se establezca
    contador+=1

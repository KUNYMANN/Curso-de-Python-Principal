#Ejercicio 1
print(((3+2)/(2*5))**2)  # 0.25 metodo directo en el print

calculo=((3+2)/(2*5))**2 #metodo por medio de una variable
print(calculo) #0.25

#OTRA MANERA ES CON EL METODO POW
'pow es parte de una libreria llamada MATH, permite agregar ciertas funciones ya establecidas en el lenguaje'
"pow lo que hace es: recibe dos valores y luego los elva a una expresion"
calculo1=pow(((3+2)/(2*5)), 2) # es lo mismo que 5**2, o sea 5 elevado al cuadrado
print(calculo1) #0.25

#Ejercicio 2

#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y 
# la empresa de logística les cobra por peso de cada paquete, así que deben calcular el peso de los payasos y muñecas
# que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Un cliente frecuente 
# pide la cantidad de 23 payasos y 54 muñecas, realiza un programa que muestre el peso total de toda la venta.

payasos=112
muñecas=75
print("El peso total de la venta en gramos es :", (23*112)+(54*75)) #6626 colocar la coma es fundamntal par concatenar
#Utlizando variables
cantidad_payasos=23
cantidad_muñecas=54
peso_payaso=112
peso_muñeca=75
print("El peso total de la venta en gramos es :", (cantidad_payasos*112)+(cantidad_muñecas*75)) #6626 
'esta es la mejor forma de resolverlo ya que la cantidad de juguetes puede cambiar pero el pes de cada juguete no'
#otras formas de obtener el resultado
peso_total_venta=(cantidad_payasos*peso_payaso)+(cantidad_muñecas*peso_muñeca)
print(f"el peso total de la venta es: {peso_total_venta} gramos") #6626 con el metodo format

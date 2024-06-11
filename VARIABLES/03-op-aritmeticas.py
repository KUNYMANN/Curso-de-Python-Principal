print(5+15)
print(5-15)
print(5*15)
print(5/20)
print(5**3)
print(5%2) #el resultado de esta operacion expresa el sobrante (1) porque, veamos
           #segun este ejemplo, cuantas veces cave el 2 en el 5, 2 veces (2+2=4)
           # cuanto falta para llegar a 5...1 (ese es sobrante)
           
num1=10
num2=6.5
num3=2
num4=5
suma=num1+(num2*num3/num4)
print(suma) #como toda operacion matematica primero resuelve segun los separadores de terminos, salvo que lo dejemos expresado 
suma=10+(6.5*2/5)
print(suma)

operacion=(num4-num3)*num1/num2
print(operacion) #aqui dejamos expresado que es lo primero que queremos que resuelva
operacion=(5-2)*10/6.5
print(operacion)

# ahora vamos a concatenar un string con un number

print("El resultado es :", operacion)
#            str             float
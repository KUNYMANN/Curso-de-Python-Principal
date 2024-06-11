

#  OPERADOR    DESCRIPCION                        EJEMPLO
#     +        suma                               a+b=15
suma=12+5

#     -        resta                              b-a=5.0
resta=12-5

#     *        multiplicacion                     a*b=50
multi=12*5

#     /        division                           b/a=2.0
division=12/5 # la division nos devuelve un dato float (flotante)
# siempre los numeros en sistemas matematicos tienen coma ejem: 
# 2.00 aunque es un numero entero tiene coma por eso el dato es float

#     %        RESTO O MODULO -Devuelve el resto          b%a=0
#              de la division
resto=12%5

#     **       EXPONENTE -Realiza                 b**a=100000
#              exponencial (POTENCIACION)         
exponente=12**5 # (en este ejemplo seria doce elevado a la quinta)

#     //       DIVISION BAJA -Devuelve el         b//a=2
#              entero de la division (si da con decimales lo imprime redondeado para abajo)
division_baja= 12//5 #este ejemplo nos muesta que el numero resultante seria 2.4 pero lo redondea
#                     para abajo, inclusive si el resultado fuese 2.9999 colocaria 2


#RESULTADOS
print(suma)
print(resta)
print(multi)
print(division)
print(resto)
print(exponente)
print(division_baja)



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


'LOS OPERADORES ARITMETICOS NOS PERMITEN REALIZAR CALCULOS MATEMATICOS BASICOS ENTRE NUMEROS'

#  OPERADOR    DESCRIPCION                        EJEMPLO
#--------------------------------------------------------------------------------------------------
#     +        suma                               a+b=15
suma=12+5
#--------------------------------------------------------------------------------------------------
#     -        resta                              b-a=5.0
resta=12-5
#--------------------------------------------------------------------------------------------------
#     *        multiplicacion                     a*b=50
multi=12*5
#--------------------------------------------------------------------------------------------------
#     /        division                           b/a=2.0
division=12/5 # la division nos devuelve un dato float (flotante)
# siempre los numeros en sistemas matematicos tienen coma ejem: 
# 2.00 aunque es un numero entero tiene coma por eso el dato es float
#--------------------------------------------------------
#     //       DIVISION BAJA -Devuelve el         b//a=2
#              entero de la division (si da con decimales lo imprime redondeado para abajo)
division_baja= 12//5 #este ejemplo nos muesta que el numero resultante seria 2.4 pero lo redondea
#                     para abajo, inclusive si el resultado fuese 2.9999 colocaria 2
#--------------------------------------------------------------------------------------------------
#     %        RESTO O MODULO -Devuelve el resto          b%a=0
#              de la division
resto=12%5
#--------------------------------------------------------------------------------------------------
#     **       EXPONENTE -Realiza                 b**a=100000
#              exponencial (POTENCIACION)         
exponente=12**5 # (en este ejemplo seria doce elevado a la quinta)
#--------------------------------------------------------------------------------------------------

#RESULTADOS
print(suma)
print(resta)
print(multi)
print(division)
print(resto)
print(exponente)
print(division_baja)


#EJERCICIOS CON OPERADORES ARITMETICOS
'''Prioridades de Operadores Aritmeticos
Parentesis ()
Exponenciacion **
Multiplicacion *, Division / y Modulo %
Suma + y Resta -'''


num1=2
num2=4
num3=6
num4=8
resultado1=(num2*8)+(6/num1)
resultado2=num2**num1
resultado3=6/2*num4+num4**2 #aquiel programa separa en termino automaticamnte de acuerdo a las prioridades de los operadores aritmeticos
resultado4=(resultado1+resultado2+resultado3)
print(resultado1)
print(resultado2)
print(resultado3)
print((resultado4+(2/num1))/num4)

ecuacion=3**3*(13/5-(2*4))
print(ecuacion)



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
print(f"{operacion:.4f}") #aqui dejamos expresado que es lo primero que queremos que resuelva
operacion=(5-2)*10/6.5
print(operacion)

# ahora vamos a concatenar un string con un number

print("El resultado es :", operacion)
#            str             float

#Como convertir un numero int a string
numero=123456
numero_string=str(numero)
print(numero_string)
print(numero*2)

#Como convertir un numero  string a int
numero_str="25"
numero1_str="36"
suma=int(numero_str)+ int(numero1_str)
print(suma)

#Como convertir un numero  string a float
numerofloatstrig="35.41"
otronumerofloatstring="26.89"
numerosstringpasadosfloat=float(numerofloatstrig)+float(otronumerofloatstring)
print(numerosstringpasadosfloat)

#COMO CONVERTIR UN NUMERO FLOAT(DECIMAL) EN ENTERO(INT)
#Como truncar un numero float en int
numdecim=12.5684
numdecim1=987.123
suma=numdecim+numdecim1
resultado=suma
redondeo=int(suma) #de esta manera solo va a imprimir el numero entero sin importar cuanto decimales tenga
print(suma)
print(f"{resultado:.2f}")
print(redondeo)

#Otra manera de hacer el redondeo lo mas ajustado posible es con round
print(round(7.3))
print(round(7.5))
print(round(7.7))

multiplicacion=17.95983 * 13.5847
print(multiplicacion)
print(round(multiplicacion,2))
print(round(multiplicacion))

division=10/3
print(division)
division1=10//3 #operador floor division devuelve el resultado en un numero entero
print(division1)

division=10%3 #operador modulo devuelve el resto de una division
print(division)

#Operador de asignacion (+,-,/,*,//,**)
num1=10
print(num1)
num1+=10 #aqui le pido que sume a la variable el valor que le asigno
print(num1)
num1-=6 #aqui le pido que reste a la variable el valor que le asigno
print(num1)
num1*=30 #aqui le pido que multiplique a la variable por el valor que le asigno
print(num1)
num1**=4 #aqui le pido que eleve a la variable al valor que le asigno
print(num1)
num1//=100 #aqui le pido que divida a la variable por el valor que le asigno y me arroje el resultado entero sin decimales
print(num1)
num1/=10 #aqui le pido que divida a la variable poR el valor que le asigno
print(f"{num1:.3F}") ##aqui le pido que me devuelva el resultado con un maximo de tres decimales

suma=90+67
print(f"el resutado de esta suma es: {suma}")
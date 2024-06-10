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

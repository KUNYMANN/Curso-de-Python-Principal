# Prioridadde los operadores logicos
# 1. not negacion invierte el resultado si es true pasa a ser salse y si es false pasa a ser true
# 2. and "y ademas" (en AND para que el resultado sea verdadero todo debe resultar verdadero)
# 3. or (en OR para que el resultado sea verdadero, basta con que uno sea verdadero)

# EJEMPLO
# a=10
# b=12
# c=13
# d=13
#      desarrollo sobre un ejercicio con tres tipos de operadores:logicos, aritmeticos y relacionales

#   ((a>b)or(a<c))     and     ((a==c)or(a>=b)
# ((10>12)or(10<13))   and   ((10==13)or(10>=12)
#     (F  or  T)                 (F   or   F)
#        (T)           and             (F)
#                   (T and F)
#                      (F)  resultado final False



# EJERCICIO CON APLICACION DE OPERADORES 
a=10
b=15
c=20
resultado=((a<b)and(b<c)) #dos verdaderos en and es true
print(resultado)

resultado=((a>b)and(b<c)) #un verdadero y un falso en and es false
print(resultado)

resultado=((a>b)or(b<c)) #un falso  y un verdadero en OR es true
print(resultado)

resultado=((a<b)or(b<c)) #des verdadero en OR es true
print(resultado)


resultado=not((a<b)and(b<c)) #la negacion de algo que es verdad es false
print(resultado)

resultado=not((a>b)and(b<c)) #la negacion de algo que es falso es true
print(resultado)

# Prioridadde los operadores logicos
# 1. not lo contrario a lo evaluado, la negacion invierte el resultado si es true pasa a ser false y si es false pasa a ser true
# 2. and componente que da una orden que se tienen que cumplir varias ordenes  para ver si se cumple una cosa "y" tambien laotra 
# (en AND para que el resultado sea verdadero todo debe resultar verdadero)
# 3. or componente que evalua si es esto "o" lo otro (en OR para que el resultado sea verdadero, basta con que uno sea verdadero)

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

resultado=((a<b)and(b<c)) # en AND si ambas evaluaciones son verdaderas el resultado es true
print(resultado)

resultado=((a>b)and(b<c)) # en AND si una de las evaluaciones arroja que es verdadero y la otra es falsa resultado es false
print(resultado)

resultado=((a>b)and(b>c)) # en AND si las evaluaciones arrojan que ambas son falsas el resultado es false
print(resultado)



resultado=((a>b)or(b<c)) #en OR si una de las evaluaciones es falsa  y el otro es verdadero el resultado es true
print(resultado)

resultado=((a<b)or(b<c)) #en OR si ambas evaluaciones son verdadero el resultado es true
print(resultado)

resultado=((a>b)or(b>c))# en or si las evaluaciones arrojan que ambas son falsas el resultado es false
print(resultado)


resultado=not((a<b)and(b<c)) #la negacion de algo que es verdad es false
print(resultado)

resultado=not((a>b)and(b<c)) #la negacion de algo que es falso es true
print(resultado)

resultado=not((a>b)and(b>c)) #la negacion de algo que es falso es true
print(resultado)
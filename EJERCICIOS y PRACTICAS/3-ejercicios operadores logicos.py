
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
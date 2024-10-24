# Los operadores logicos permiten construir expresiones logicas y se obtiene como resultado booleanos 
'LA COMPARACION MINIMA ES ENTRE DOS OPERANDOS'
# and (y).... conjuncion o multiplicacion logica true es 1 y false es 0  
# or (o)..... disyuncion o suma logica
# not (no).... negacion      
'''PRIORIDAD DE LOS PERADORES LOGICOS
not (que españos significa "NO")
and (que en español significa "Y") 
y or (que en español significa "O")'''


"""OPERADOR AND (y) "multiplicacion logica" 
#IMPORTANTE!!! solo si ambos operandos son verdaderos el resultado va a ser siempre verdadero
con un minimo de dos operandos de valores logicos o booleanos a comparar
En la programacion TRUE tiene el valor de 1 dado que solo el 1 multiplicado por si mismo da 1
y FALSE tiene el valor 0 porque todo numero multiplicado por 0 es siempre 0
operando1   operador   operando2   RESULTADO   
True        and (y)       True       TRUE  (si ambos operandos son verdaderos el resultado siempre sera true) 1 
True        and (y)       False      FALSE (si cuaquiera de los dos operandos es falso el resultado siempre sera false)  0 
False       and (y)       True       FALSE (si cuaquiera de los dos operandos es falso el resultado siempre sera false)  0 
False       and (y)       False      FALSE (si cuaquiera de los dos operandos es falso el resultado siempre sera false)  0 

OPERADOR OR se lo conoce como una suma logica
IMPORTANTE!!! solo si ambos operandos son falsos el resultado va a ser siempre falso
operando  RESULTADO
True         or (o)       True       TRUE (basta que cualquiera de los dos operandos sea verdadero el resultado siempre sera true) 1
True         or (o)       False      TRUE (basta que cualquiera de los dos operandos sea verdadero el resultado siempre sera true) 1
False        or (o)       True       TRUE (basta que cualquiera de los dos operandos sea verdadero el resultado siempre sera true) 1
False        or (o)       False      FALSE (cuando ambos operandos son falso el resultado siempre sera false) 0

OPERADOR NOT se lo conoce como un valor de negacion
IMPORTANTE!!! Invierte el valor del operador y se lo conoce como un Operador Unario porque trabaja con un solo valor
operando    RESULTADO
not(True)    FALSE  (UNA VERDAD NEGADA ES UNA MENTIRA) Ejemplo: #si es verdad que jesus no existió...FALSO porque se esta mintiendo sobre una verdad, jesus existio
not(False)   TRUE   (UNA MENTIRA NEGADA ES UNA VERDAD) Ejemplo: #no es verdad que jesus no existio...VERDAD porque jesus si existio"""

print("*** OPERADOR AND***")
#Regresa verdadero si ambos valores son verdaderos
condicion1=False
condicion2=False
resultado=condicion1 and condicion2
print(f"El resultado de aplicar la condicion and entre {condicion1} y {condicion2} es: {resultado}")#False
'Cambiamos el valor de una de las variables'
condicion1=False
condicion2=True
resultado=condicion1 and condicion2
print(f"El resultado de aplicar la condicion and entre {condicion1} y {condicion2} es: {resultado}")#False
'Ahora colocaremos dos variables verdaderas'
condicion1=True
condicion2=True
resultado=condicion1 and condicion2
print(f"El resultado de aplicar la condicion and entre {condicion1} y {condicion2} es: {resultado}")#True


print()
edad=54
print(edad>50 and edad<52) #si uno de los resultados de esta solicitud es falso el resultado final es false (54 es mayor que 50 si y es menor que 52 NO)
print(edad>50 and edad<60) #si los resultados de esta solicitud son correctos  el resultado final es true (54 es mayor que 50 si y es menor que 60 si)
print(edad>56 and edad<60) #si uno de los resultados de esta solicitud es falso el resultado final es false (54 es mayor que 56 NO y es menor que 60 si)
print()
print(edad<60 or edad>53) # TRUE...(ambas condiciones son ciertas, 54 es menor que 60 pero tambien 54 mayor que 53)
print(not(edad>52))# FALSE...(no es cierto que 54 es mayor que 52? es falso porque 54 es mayor a 52) una verdad negada es falsa
print(not(edad>56))#TRUE...(no es cierto que 54 sea mayor que 56? es verdad porque 54 no es mayor a 56) una mentira negada es verdad


# Prioridadde los operadores logicos
# 1. not lo contrario a lo evaluado, la negacion invierte el resultado si es true pasa a ser false y si es false pasa a ser true
# 2. and componente que da una orden que se tienen que cumplir varias ordenes  para ver si se cumple una cosa "y" tambien la otra 
# (en AND para que el resultado sea verdadero todo debe resultar verdadero)
# 3. or componente que evalua si es esto "o" lo otro (en OR para que el resultado sea verdadero, basta con que uno sea verdadero)

# EJEMPLO
# a=10, b=12, c=13, d=13
#      desarrollo sobre un ejercicio con tres tipos de operadores:logicos, aritmeticos y relacionales

#   ((a>b)or(a<c))     and     ((a==c)or(a>=b)      ejercicio inicial
# ((10>12)or(10<13))   and   ((10==13)or(10>=12)    reemplazo por los valores asignados
#     (F  or  T)                 (F   or   F)       vamos comprobando por partes
#        (T)           and             (F)          resultante
#                   (T and F)                       evaluacion final
#                      (F) False                    conclusion final 

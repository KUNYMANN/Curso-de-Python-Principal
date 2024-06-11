# Los operadores logicos permiten construir expresiones logicas y se obtiene como resultado booleanos y la comparacion minima es entre dos operandos
# and.... conjuncion o multiplicacion logica true es 1 y false es 0  
# or..... disyuncion o suma logica
# not.... negacion      

"""OPERADOR AND
operando1   operador   operando2   RESULTADO
True           and        True       TRUE  (solo se da si ambos operandos valores son verdaderos el resultado siempre sera true)
True           and        False      FALSE (si cuaquiera de los dos operandos es falso el resultado siempre sera false)
False          and        True       FALSE (si cuaquiera de los dos operandos es falso el resultado siempre sera false)
False          and        False      FALSE (si cuaquiera de los dos operandos es falso el resultado siempre sera false)

OPERADOR OR
operando  RESULTADO
True           or        True       TRUE (basta que cualquiera de los dos operandos sea verdadero el resultado siempre sera true)
True           or        False      TRUE (basta que cualquiera de los dos operandos sea verdadero el resultado siempre sera true)
False          or        True       TRUE (basta que cualquiera de los dos operandos sea verdadero el resultado siempre sera true)
False          or        False      FALSE (cuando ambos operandos son falso el resultado siempre sera false)

OPERADOR NOT
operando    RESULTADO
not(True)    FALSE  (UNA VERDAD NEGADA ES UNA MENTIRA) Ejemplo: #mentira (jesus sí existió)...FALSO porque se esta mintiendo sobre una verdad jesus existio
not(False)   TRUE   (UNA MENTIRA NEGADA ES UNA VERDAD) Ejemplo: #mentira (jesus no existio)...VERDAD porque jesus existio"""


edad=54
print(edad>50 and edad<52) #si uno de los resultados de esta solicitud es falso el resultado final es falso (54 es mayor que 50 si y es menor que 52 NO)
print(edad>50 and edad<60) #si los resultados de esta solicitud son correctos  el resultado final es true (54 es mayor que 50 si y es menor que 60 si)
print(edad>56 and edad<60) #si uno de los resultados de esta solicitud es falso el resultado final es falso (54 es mayor que 56 NO y es menor que 60 si)

print(edad>53 or edad<60) #evaluan en true (54 es mayor que 56 no y es menor que 60 si)
print(not(edad>52))#evalua en false (no es cierto que 54 es mayor que 52? false es falso porque 54 es mayor a 52) una verdad negada es falsa
print(not(edad>56))#(no es cierto que 54 sea mayor que 56? True es verdad porque 54 no es mayor a 56) una mentira negada es verdad



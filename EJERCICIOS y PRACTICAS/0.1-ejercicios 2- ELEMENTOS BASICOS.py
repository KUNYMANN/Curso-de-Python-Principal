#DETERMINAR LA SOLUCION LOGICA DE LA SIGUIENTE OPERACION
# Valores para a=10 y b=5 
#((3+5X8)<3 and ((-6/3x4)+2<2)) or (a>b)  primero se resuelven los parentesis de los mas internos a los mas externos
#  ( 43  <3 and      (-8 +2<2)) or  True  luego los siguientes parentesis internos 
#    (43<3  and        -6<2   ) or  True  seguimos resolviendo lo terminos entre parentesis
#    (43<3  and        True   ) or  True  seguimos resolviendo lo terminos entre parentesis
#    (False and        True   ) or  True  resultados booleanos
#                        False  or  True  resultados booleanos
#                              True       resultado booleanos

a=float(input("ingrese aqui un valor para a: "))
b=float(input("ingrese aqui un valor para b: "))
ejercicio2=((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b)
print(f"el resultado del ejercicio es:  {ejercicio2} maravilloso!!")
print("el resultado del ejercicio es:" , ejercicio2, "maravilloso!!")
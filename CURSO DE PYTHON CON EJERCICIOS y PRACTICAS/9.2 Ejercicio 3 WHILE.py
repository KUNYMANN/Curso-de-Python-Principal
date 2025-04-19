clave="123hez"
ingreso=input("Ingrese su clave de ingreso: ").strip()
veces=0
while ingreso!=clave and veces<2:
    print("Clave erronea, ingrese nuevamente")
    ingreso=input("Ingrese su clave de ingreso: ").strip()
    veces+=1
if ingreso==clave:
       print("Ingreso exitoso")
else:
       print("Acceso bloquedo")

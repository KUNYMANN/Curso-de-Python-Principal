#Crear un programa para generar un email a partir de los siguientes datos
nombre="    Hector Emilio Zanor    "
empresa="   Vigor SACIF   "
dominio=".com.ar"
nombre_normalizado=nombre.strip().replace(" ", ".").lower()
renombrada=empresa.replace(" ","").lower()
email_normalizado=f"@{renombrada}{dominio}"
email_final=nombre_normalizado+email_normalizado
resultado="hector.emilio.zanor@vigorsacif.com.ar"

print("**** GENERADOR DE EMAIL ****")
print(f"Nombre del Usuario:{nombre}")
print(f"Nombre del Usuario normalizado: {nombre_normalizado}")
print(f"\nNombre de la empresa:{empresa}")
print(f"Extension del dominio: {dominio}")
print(f"Dominio de email normalizado: {email_normalizado}")
print(f"\nEmail final generado: {email_final}")
print(resultado)
print()
#Ejercicio
print("**** GENERADOR DE EMAIL ****")
nombre=input("Ingrese todos sus nombres: ")
apellido=input("Ingrese sus apellidos: ")
empresa=input("Ingrese el nombre completo de la empresa para la que trabaja: ")
dominio=input("Ingrese su domino de email: ")

nombre_completo=(nombre.strip().lower()+" "+apellido.strip().lower()).replace(" ",".")
empresa1=empresa.strip().lower().replace(" ",".")
dominio1=dominio.strip().lower().replace(" ",".")



print(f"""Su e-mail generado por el sistema es:
         {nombre_completo}@{empresa1}{dominio1}
         FELICIDADES!!!""")
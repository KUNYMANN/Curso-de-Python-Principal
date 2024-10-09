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


print()
nombre_de_usuario=input("Ingrese su nombre de usuario: ").strip().upper()
pasos=int(input("Ingrese la cantidad de pasos realizados en el dia: "))
print(f"\nSu nombre de usuario es: {nombre_de_usuario}")
print(f"\nLa cantidad de pasos ingresados es: {pasos}")
meta_pasos_diarios=10000
calorias_por_paso=0.04
calorias_quemadas=pasos*calorias_por_paso
print(f"\nTus calorias quemadas fueron de: {calorias_quemadas:.2F}")
meta_alcanzada=pasos>=meta_pasos_diarios
objetivo="Si"if pasos>=10000 else "No"
print(f"\nHas alcanzado tu meta? {objetivo}")
print()
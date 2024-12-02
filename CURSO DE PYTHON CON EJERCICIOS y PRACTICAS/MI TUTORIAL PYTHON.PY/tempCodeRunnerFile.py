
print('*** CASA DE LOS ESPEJOS ***')
edad=float(input("Ingresen su edad: "))
miedo=input('Le tienes miedo a la oscuridad (Si/No): ')
miedoso=miedo=="si".strip().lower()
if not miedoso and edad>=10 :
    print("Puedes ingresar")
else:
     print('No puedes ingresar')
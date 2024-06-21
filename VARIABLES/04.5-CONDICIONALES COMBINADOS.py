
# Condicionales combinados o anidados
"""vamos a solicitarle al usuario que digite su edad, que es un dato entero, 
ahora vamoa a calcular si este usuario es mayor de edad o no"""
edad=int(input("digite su edad: "))
mayor_de_edad=edad>18 
if edad>0 and edad<100:  #aqui colocamos dos rangos o àrametros,UNO que la edad sea mayor a cero y OTRO que la edad sea menor a cien
    print("Edad correcta")
    if edad>=18: # condicional anidado
        print("Eres mayor de edad")      
else:
    print("Edad incorrecta")


# Otra forma mas corta 
edad=int(input("digite su edad: "))
if 0<edad<100: #aca los rangos estan solicitados de una manera mas corta
    print("Edad correcta")
    if edad>=18: # condicional anidado
        print("Eres mayor de edad")      
else:
    print("Edad incorrecta")

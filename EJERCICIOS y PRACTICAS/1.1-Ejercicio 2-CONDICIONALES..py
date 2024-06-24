#EJERCICIO
#hacer un programa que pida 3 numeros y determine cual es el mayor.
"""asi lo pense yo pero hay un error de sintaxis"""
'''numero=int(input ("coloque un numero:"))
numero1=int(input ("coloque un numero1:"))
numero2=int(input ("coloque un numero2:"))
if numero>=numero1>=numero2:
    print(f"el numero {numero} es mayor")
elif numero1>=numero2>=numero:
    print(f"el numero {numero1} es mayor")
elif numero2>=numero>=numero1:
     print(f"el numero {numero2} es mayor")
else:
    print("El numero ingresado es el mismo en los tres casos")'''

numero=int(input ("coloque un numero:"))
numero1=int(input ("coloque un numero1:"))
numero2=int(input ("coloque un numero2:"))

if numero>=numero1 and numero>=numero2:
    print(f"El numero mayor es { numero}")
elif numero1>=numero and numero1>=numero2:
    print(f"El numero mayor es { numero1}")
elif numero2>=numero1 and numero2>=numero:
    print(f"El numero mayor es { numero2}")
else:
    print("Usted ingreso tres numeros iguales")

#EJERCICIO PLANTEADO CON SANTI

usuario=(input("clima "))
usu2=(input("llueve "))
if usuario=="nublado" and usu2=="si":    
    print("llevo pilotin")
elif usuario=="nublado" and usu2=="no":
    print("no llevo paraguas")
elif usuario=="llueve" and usu2=="si":
    print("LLevo pilotin entonces")  
elif usuario=="llueve" and usu2=="no":
    print("imposible")  
elif usuario=="llueve" and usu2=="no":
    print("no llevo pilotin")
elif usuario=="Soleado" and usu2=="no":
    print("hay sol")
elif usuario=="Soleado" and usu2=="si":
    print("dicen que se casa una bruja jajajjaj")

   
peso_envio=float(input("ingrese el peso en kilogramos de su envio: "))
tipo_de_envio=input("Ingrese si el destino del envio es nacional o internacional: ").strip().lower()
ciudad_de_envio=input("Ingrese la localidad de destino: ").strip().upper()
pais_de_envio=input("Ingrese pais de destino: ").strip().upper()
costo_de_envio=None #aqui la variable=none aqui va relacionado con las variables de tarifa dado que de variar los valores también varia el costo
tarifa_nacional=10
tarifa_internacional=20
print ("***TICKET DE ENVIO NACIONAL/INTERNACIONAL***" )
if peso_envio<=0:
    print("Error al ingresar el peso del envio")

elif tipo_de_envio=="nacional" and pais_de_envio!="ARGENTINA":
    print("Error verifique el pais al cual realiza el envio")

elif tipo_de_envio=="nacional" and pais_de_envio=="ARGENTINA":
    costo_envio=peso_envio*tarifa_nacional
    print(f"Su envio NACIONAL es para la localidad de {ciudad_de_envio} en {pais_de_envio} \n el peso de su envio es de {peso_envio} kg \n el costo de su envio es de $ {costo_envio:.2f}")

elif tipo_de_envio=="internacional"and pais_de_envio=="ARGENTINA":
    print("Error verifique el pais al cual realiza el envio")

elif  tipo_de_envio=="internacional" and pais_de_envio!="ARGENTINA":
      costo_envio=peso_envio*tarifa_internacional
      print(f"Envio INTERNACIONAL es para la localidad de {ciudad_de_envio} en {pais_de_envio} \n el peso de su envio es de {peso_envio} kg \n el costo de su envio es de $ {costo_envio:.2f}")


else:
    print("'ERROR' en los datos ingresados")

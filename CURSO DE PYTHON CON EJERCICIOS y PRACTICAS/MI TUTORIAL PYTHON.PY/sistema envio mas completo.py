peso_envio=float(input("ingrese el peso en kilogramos de su envio: "))
tipo_de_envio=input("Ingrese si el destino del envio es nacional o no (Si/No) : ").strip().lower()
lugar_de_envio=input("Ingrese la localidad de destino: ").strip().upper()
lugar_de_envio1=input("Ingrese pais de destino: ").strip().upper()
print ("***TICKET DE ENVIO NACIONAL/INTERNACIONAL***" )
print("tarifa de envio nacional= $10 x kilo")
print("tarifa de envio internacional= $20 x kilo")

if tipo_de_envio=="si" and lugar_de_envio1!="ARGENTINA":
    print("Error no coinciden informacion entre localidad/pais")

elif tipo_de_envio=="si" and lugar_de_envio1=="ARGENTINA":
    print("Su envio es NACIONAL")
    costo_envio1=peso_envio*10
    print(f"Envio para la localidad de {lugar_de_envio} en {lugar_de_envio1} \n el peso de su envio es de {peso_envio} kg \n el costo de su envio es de $ {costo_envio1:.2f}")

elif tipo_de_envio=="no"and lugar_de_envio1=="ARGENTINA":
    print("Error no coinciden informacion entre localidad/pais")

elif  tipo_de_envio=="no" and lugar_de_envio1!="ARGENTINA":
    print("Su envio es INTERNACIONAL")
    costo_envio2=peso_envio*20
    print(f"Envio para la localidad de {lugar_de_envio} en {lugar_de_envio1} \n el peso de su envio es de {peso_envio} kg 13 \n el costo de su envio es de $ {costo_envio2:.2f}")


else:
    print("'ERROR' verifique si el destino es nacional o no")

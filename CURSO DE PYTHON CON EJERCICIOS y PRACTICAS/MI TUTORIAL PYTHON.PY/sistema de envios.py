'''crear un programa para determinar el costo de envío de un paquete según el destino,
puede ser nacional o internacional y el peso del paquete.
Ahora, de manera interna van a definir las siguientes constantes para determinar el costo de las tarifas.
Dependiendo si es nacional, el costo va a ser de 10 $ por kilo y si es un envío internacional el costo
va a ser de 20 $ por kilo.
Obviamente pueden adaptar el costo a su moneda nacional.
Por otro lado, el programa debe solicitar dos valores.
Por un lado, el destino puede ser nacional o internacional y también el peso del paquete en kilogramos.
Así que con estos dos valores al final debe de mandar a imprimir el costo del envío del paquete considerando
los valores que hemos solicitado, el destino, si es nacional o internacional y el peso en kilogramos
del paquete.'''

peso_envio=float(input("ingrese el peso en kilogramos de su envio: "))
tipo_de_envio=input("Ingrese si el destino del envio es nacional o no (Si/No) : ").strip().lower()
lugar_de_envio=input("Ingrese la localidad/pais de destino: ").strip().upper()
print ("***TICKET DE ENVIO NACIONAL/INTERNACIONAL***" )
print("tarifa de envio nacional= $10 x kilo")
print("tarifa de envio internacional= $20 x kilo")
if tipo_de_envio=="si":
    costo_envio1=peso_envio*10
    print("Su envio es NACIONAL")
    print(f"Envio para la localidad de {lugar_de_envio} \n el peso de su envio es de {peso_envio} kg \n el costo de su envio es de $ {costo_envio1:.2f}")
else :
    costo_envio2=peso_envio*20
    print("Su envio es INTERNACIONAL")
    print(f"Envio para la localidad de {lugar_de_envio} \n el peso de su envio es de {peso_envio} kg \n el costo de su envio es de $ {costo_envio2:.2f}")





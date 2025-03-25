precio1=200 #habitacion CVM
precio2=150 #habitacion SVM

print(f"Cuartos con vista al mar $ {precio1} por dia")
print(f"Cuartos sin vista al mar $ {precio2} por dia")
print()
nombre=input("Ingrese su nombre y apellido completo: ").strip().title()
dias=int(input("Indique la cantidad de dias que va a alojarse en el hotel: "))
cuartos_vm=input("Desea un cuarto con vista al mar? (Si/No): ").strip().lower()
efectivo_debito=input("Si abona en efectivo/debito obterndra un descuento 10% (Si/No): ").strip().lower()
masde=20


print("\n----------Detalles de la reserva-----------")
print()
print(f"Nombre reserva: {nombre}")
print(f"cantidad de dias: {dias}")


#mas de 20 dias, Hab.C V Mar,pago en efectivo
if dias>=20 and cuartos_vm=="si" and efectivo_debito=="si":
   
   costo_alojamiento1=precio1*dias # CVM  
   descuento_efec=costo_alojamiento1*.80*.90 # 20% VM + 10% Efect
   print(f"Hab. vista al mar: {cuartos_vm}")
   print(f"Importe a abonar con descuento del {masde} % por alojarse mas de 20 dias $ {costo_alojamiento1*.80:.2f}")
   print(f"Por abonar en efectivo su importe final es $ {descuento_efec:.2f} ")
   print(1)

#mas de 20 dias, Hab.C V Mar,paga con otro medio  
if dias>=20 and cuartos_vm=="si" and  efectivo_debito=="no":
   costo_alojamiento1=precio1*dias # CVM 
   print(f"Hab. vista al mar: {cuartos_vm}")
   print(f"Importe a abonar con descuento del {masde} % por alojarse mas de 20 dias $ {costo_alojamiento1*.80:.2f}")
   print(2)

#menos de 20 dias, hab. C V Mar, paga efectivo
if dias<20 and cuartos_vm=="si" and efectivo_debito=="si":
   descuento2=precio1*.90*dias #10% pago en efectivo
   print(f"Hab. vista al mar: {cuartos_vm}")
   print(f"Por abonar en efectivo su importe final a pagar es $ {descuento2:.2f}")
   print(3)

#menos de 20 dias, hab. C V Mar, paga con otro medio
if dias<20 and cuartos_vm=="si" and efectivo_debito=="no" :
   costo_alojamiento1=precio1*dias # CVM 
   print(f"Hab. vista al mar: {cuartos_vm}")
   print(f"Total a pagar $ {costo_alojamiento1:.2f}")
   print(4)   

#mas de 20 dias, hab. S V Mar, paga efectivo
if dias>=20 and cuartos_vm=="no" and efectivo_debito=="si":
   costo_alojamiento2=precio2*dias # SVM
   descuento_efec=costo_alojamiento2*.80*.90 # 20% VM + 20% Efect
   print(f"Hab. vista al mar: {cuartos_vm}")
   print(f"Importe a abonar con descuento del {masde} % por alojarse mas de 20 dias $ {costo_alojamiento2*.80:.2f}")
   print(f"Por abonar en efectivo su importe final es $ {descuento_efec:.2F} ")
   print(5) 
   
#mas de 20 dias, hab. S V Mar, paga con otro medio
if dias>=20 and cuartos_vm=="no" and efectivo_debito=="no":
   costo_alojamiento2=precio2*dias # SVM
   print(f"Hab. vista al mar: {cuartos_vm}")
   print(f"Importe a abonar con descuento del {masde} % por alojarse mas de 20 dias $ {costo_alojamiento2*.80:.2f}")
   print(6) 
   
#menos de 20 dias, hab. S V Mar, paga efectivo
if dias<20 and cuartos_vm=="no" and efectivo_debito=="si":
   costo_alojamiento2=precio2*dias # SVM
   print(f"Hab. vista al mar: {cuartos_vm}")
   print(f"Por abonar en efectivo su importe final es $ {costo_alojamiento2*.90:.2F} ")
   print(7) 
   
#mas de 20 dias, hab. S V Mar, paga con otro medio
if dias<20 and cuartos_vm=="no" and efectivo_debito=="no":
   costo_alojamiento2=precio2*dias # SVM
   print(f"Hab. vista al mar: {cuartos_vm}")
   print(f"Total a pagar $ {costo_alojamiento2:.2f}")
   print(8) 

print(     '\n"GRACIAS POR ALOJARSE EN NUESTRO HOTEL"')
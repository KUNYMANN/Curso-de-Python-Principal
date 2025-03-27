

precio1 = 200
precio2 = 150

print(f"Cuartos con vista al mar $ {precio1} por día")
print(f"Cuartos sin vista al mar $ {precio2} por día")
print()
nombre_completo_pasajero = input("Ingrese su nombre y apellido completo: ").strip().title()
dias_en_el_hotel = int(input("Indique la cantidad de días que va a alojarse en el hotel: "))
cuartos_con_vista_al_mar = input("¿Desea un cuarto con vista al mar? (Si/No): ").strip().lower()
efectivo_debito = input("Si abona en efectivo/débito obtendrá un descuento 10% (Si/No): ").strip().lower()
print("\n----------Detalles de la reserva-----------")

# Más de 20 días, Hab. con vista al mar, pago en efectivo
if dias_en_el_hotel >= 20 and cuartos_con_vista_al_mar == "si":
    descuento1 = precio1 * 0.80
    valor_promocion1 = descuento1 * dias_en_el_hotel
    if efectivo_debito == "si":
        pago_efectivo = valor_promocion1 * 0.90
        print(f"""
Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de días de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitación con vista al mar: {cuartos_con_vista_al_mar}
Promoción otorgada de un descuento de $ {descuento1} por 20 días o más...
El total de su reserva por los {dias_en_el_hotel} días es $ {valor_promocion1} 
Si abona en efectivo la suma final a pagar es $ {pago_efectivo}""")
    else:
        print(f"""
Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de días de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitación con vista al mar: {cuartos_con_vista_al_mar}
Promoción otorgada de un descuento de $ {descuento1} por 20 días o más...
El total de su reserva por los {dias_en_el_hotel} días es $ {valor_promocion1}""")

# Menos de 20 días, Hab. con vista al mar, pago en efectivo
if dias_en_el_hotel < 20 and cuartos_con_vista_al_mar == "si":
    valor_s_promocion = precio1 * dias_en_el_hotel
    if efectivo_debito == "si":
        pago_efectivo = valor_s_promocion * 0.90
        print(f"""
Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de días de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitación con vista al mar: {cuartos_con_vista_al_mar}
El total de su reserva por los {dias_en_el_hotel} días es $ {valor_s_promocion} 
Si abona en efectivo la suma final a pagar es $ {pago_efectivo}""")
    else:
        print(f"""
Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de días de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitación con vista al mar: {cuartos_con_vista_al_mar}
El total de su reserva por los {dias_en_el_hotel} días es $ {valor_s_promocion}""")

# Más de 20 días, Hab. sin vista al mar, pago en efectivo
if dias_en_el_hotel >= 20 and cuartos_con_vista_al_mar == "no":
    descuento2 = precio2 * 0.80
    valor_promocion2 = descuento2 * dias_en_el_hotel
    if efectivo_debito == "si":
        pago_efectivo = valor_promocion2 * 0.90
        print(f"""
Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de días de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitación sin vista al mar: {cuartos_con_vista_al_mar}
Promoción otorgada de un descuento de $ {descuento2} por 20 días o más...
El total de su reserva por los {dias_en_el_hotel} días es $ {valor_promocion2}
Si abona en efectivo la suma final a pagar es $ {pago_efectivo}""")
    else:
        print(f"""
Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de días de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitación sin vista al mar: {cuartos_con_vista_al_mar}
Promoción otorgada de un descuento de $ {descuento2} por 20 días o más...
El total de su reserva por los {dias_en_el_hotel} días es $ {valor_promocion2}""")

# Menos de 20 días, Hab. sin vista al mar, pago en efectivo
if dias_en_el_hotel < 20 and cuartos_con_vista_al_mar == "no":
    descuento2 = precio2 * 0.80
    valor_promocion2 = descuento2 * dias_en_el_hotel
    if efectivo_debito == "si":
        pago_efectivo = valor_promocion2 * 0.90
        print(f"""
Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de días de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitación sin vista al mar: {cuartos_con_vista_al_mar}
Promoción otorgada de un descuento de $ {descuento2} por menos de 20 días...
El total de su reserva por los {dias_en_el_hotel} días es $ {valor_promocion2}
Si abona en efectivo la suma final a pagar es $ {pago_efectivo}""")
    else:
        print(f"""
Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de días de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitación sin vista al mar: {cuartos_con_vista_al_mar}
El total de su reserva por los {dias_en_el_hotel} días es $ {valor_promocion2}""")

# Menos de 20 días, Hab. sin vista al mar, paga con otro medio
else:
    print(f"""
Reserva realizada a nombre de Sr./Sra.: {nombre_completo_pasajero}
La cantidad de días de su reserva es: {dias_en_el_hotel}
Solicito reserva para una habitación sin vista al mar: {cuartos_con_vista_al_mar}
El total de su reserva por los {dias_en_el_hotel} días es $ {precio2 * dias_en_el_hotel}""") 


    




print("***SISTEMA RESERVA HOTEL***")

Precio_CVM = 200
Precio_HN = 150

Descuento_Efectivo = 0.8
Descuento_20_Dias = 0.9

print(f"Cuartos con vista al mar $ {Precio_CVM} por dia")
print(f"Cuartos sin vista al mar $ {Precio_HN} por dia")
print()


# Datos del usuario
Nombre = input("Ingrese su nombre y apellido completo: ").strip().title()
Dias = int(input("Indique la cantidad de dias que va a alojarse en el hotel: "))
CVM = input("Desea un cuarto con vista al mar? (Si/No): ").strip().upper()
Efectivo = input("Selecione si va a bonar en efectivo (Si/No): ").strip().lower()


print("\n----------Detalles de la reserva-----------") 

# Calculo el total a pagar (Sin descuentos)
if CVM == "SI":
   Precio_Intermedio = Precio_CVM * Dias      

if CVM == "NO":
   Precio_Intermedio = Precio_HN * Dias       

# Precios Finales (Con Descuentos)
if Dias >= 20 and Efectivo == "si":
   Precio_Final = Precio_Intermedio * Descuento_20_Dias * Descuento_Efectivo
   print(f""""Reserva realizada a nombre de Sr./Sra.: {Nombre}
La cantidad de dias de su reserva es: {Dias}
Solicito reserva para una habitacion con vista al mar: {CVM}
Promocion otorgada de un descuento de $ {round(Precio_Intermedio * (1-Descuento_20_Dias) * (1-Descuento_Efectivo))} por 20 dias o mas y pagar en efectivo
El total de su reserva por los {Dias} dias es $ {Precio_Final}""")

elif Dias >= 20 and Efectivo == "no":
   Precio_Final = Precio_Intermedio * Descuento_20_Dias
   print(f""""Reserva realizada a nombre de Sr./Sra.: {Nombre}
La cantidad de dias de su reserva es: {Dias}
Solicito reserva para una habitacion con vista al mar: {CVM}
Promocion otorgada de un descuento de $ {round(Precio_Intermedio * (1-Descuento_20_Dias))} por 20 dias o mas...
El total de su reserva por los {Dias} dias es $ {Precio_Final} 
Si abona en efectivo la suma final a pagar es {Precio_Final * (1-Descuento_Efectivo)}""")

elif Dias < 20 and Efectivo == "si":
   Precio_Final = Precio_Intermedio * Descuento_Efectivo
   print(f""""Reserva realizada a nombre de Sr./Sra.: {Nombre}
La cantidad de dias de su reserva es: {Dias}
Solicito reserva para una habitacion con vista al mar: {CVM}
Promocion otorgada de un descuento de $ {round(Precio_Intermedio * (1-Descuento_Efectivo))} pagar en efectivo.""")

else :
   precio_sin_descuento=Precio_CVM*Dias
print(f"""Reserva realizada a nombre de Sr./Sra.: {Nombre}
La cantidad de dias de su reserva es: {Dias}
Solicito reserva para una habitacion con vista al mar: {CVM}
El total de su reserva por los {Dias} dias es $ {precio_sin_descuento}""")


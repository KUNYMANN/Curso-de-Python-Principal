monto_compra=float(input("Ingrese el monto total de su compra: "))
membresia=input("Indique si/no es cliente de la tienda: ").lower()
descuento=monto_compra-(monto_compra*10/100)
descuento2=monto_compra-(monto_compra*5/100)
if monto_compra>=1000 and membresia=="si":
        print(f"Por ser cliente y su compra superar los $1.000 posee un descuento del 10%, su monto a pagar es $ {descuento:.2f}")
elif monto_compra<1000 and  membresia=="si":
    print(f"Por ser cliente y su compra no superar los $1.000 posee un descuento del 5%, su monto a pagar es $ {descuento2:.2f}")
elif monto_compra>1000 and membresia=="no":
    print(f'''Por no ser cliente uu compra no tiene descuentos, el  monto a pagar es $ {monto_compra:.2f}
          "TE INVITAMOS A HACERTE SOCIO DE LA TIENDA"''')
else:
    print(f'''Por no ser cliente y su compra no superar los $1.000 su monto a pagar es $ {monto_compra:.2f}
          "TE INVITAMOS A HACERTE SOCIO DE LA TIENDA"''')


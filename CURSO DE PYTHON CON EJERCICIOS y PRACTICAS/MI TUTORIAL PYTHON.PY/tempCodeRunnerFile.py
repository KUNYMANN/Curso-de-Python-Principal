print(   "****   SISTEMA DE DESCUENTO    ****")
monto_compra=float(input("Ingrese el monto total de su compra: "))
membresia=input("Indique si/no es cliente de la tienda: ").lower()
descuento=monto_compra*10/100
descuento1=monto_compra*5/100
descuento2=monto_compra-descuento
descuento3=monto_compra-descuento1

if monto_compra>=1000 and membresia=="si":
        print(f"""Felicidades!!! por ser cliente y tu compra superar los $ 1.000 
    Te has hecho acreedor al siguiente descuento
    Monto de la compra: ........$ {monto_compra:.2f} 
    Descuento otorgado del 10%: $  {descuento:.2f}
    Tu monto a pagar es ........$ {descuento2:.2f}""")
elif monto_compra<1000 and  membresia=="si":
    print(f"""Por ser cliente pero tu compra no supera los $ 1.000 
    Te has hecho acreedor al siguiente descuento
    Monto de la compra:....... $ {monto_compra}
    Descuento otorgado del 5%: $  {descuento1:.2F} 
    Tu monto a pagar es ...... $ {descuento3:.2f}""")
elif monto_compra>1000 and membresia=="no":
    print(f'''Por no ser cliente su compra no tiene descuentos, 
    el  monto a pagar es $ {monto_compra:.2f}
"TE INVITAMOS A HACERTE SOCIO DE LA TIENDA"''')
else:
    print(f'''Por no ser cliente y su compra no superar los $1.000
     su monto a pagar es $ {monto_compra:.2f}
"TE INVITAMOS A HACERTE SOCIO DE LA TIENDA"''')


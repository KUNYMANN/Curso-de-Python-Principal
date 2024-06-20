# UNA TIENDA OFRECE UN DESCUENTO DEL 15% SOBRE EL TOTAL DE LA COMPRA
# Y UN CLIENTE QUIERE SABER CUANTO DEBERA PAGAR FINALMENTE POR SU COMPRA.
'''precio=float(input("Digite el precio del producto: "))'''


mensaje="coloque el importe del producto: "
mensaje1=mensaje.upper()
precio=float(input(mensaje1))
descuento=precio*0.15
precio_final= precio-descuento
a=("El monto a pagar con descuento del 15% es de $: ")
print(a.upper() + (f"{precio_final:.2f}"))



'''mensaje="coloque el importe del producto: "
mensaje_mayusculas=mensaje.upper()
precio=float(input(mensaje_mayusculas))
print(f"el importe del producto es: {precio}")'''





'''precio=float(input(mensaje))
descuento=precio*0.15
precio_final= precio-descuento
a="El monto a pagar con descuento del 15% es de $: "
mensaje_mayusculas=mensaje.upper()
mensaje="Digite el precio del producto: "
print(f"digite el precio del producto: ", precio)'''
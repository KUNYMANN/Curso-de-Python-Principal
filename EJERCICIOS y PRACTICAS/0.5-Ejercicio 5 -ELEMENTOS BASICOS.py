# UNA TIENDA OFRECE UN DESCUENTO DEL 15% SOBRE EL TOTAL DE LA COMPRA
# Y UN CLIENTE QUIERE SABER CUANTO DEBERA PAGAR FINALMENTE POR SU COMPRA.
'''precio=float(input("Digite el precio del producto: "))'''


mensaje="coloque el importe del producto 1: "
mensaje1=mensaje.upper()
precio=float(input(mensaje1))
descuento=precio*0.15
precio_final= precio-descuento
a=("El monto a pagar con descuento del 15% es de $: ")
print(a.upper() + (f"{precio_final:.2f}"))

mensaje2="Digite el precio del producto 2: "
mensaje_mayusculas=mensaje2.upper()
precio=float(input(mensaje_mayusculas))
descuento=precio*0.15
precio_final= precio-descuento
a1="El monto a pagar con descuento del 15% es de $: "
print(a1, f"{precio_final:.2f}")

mensaje="coloque el importe del articulo 3: "
mensaje_mayusculas=mensaje.upper()
precio3=float(input(mensaje_mayusculas))
b12="El monto a pagar con descuento del 15% es de $: "
precio_final= precio3-descuento
print(b12,f"{precio_final:.2f}")

dato="ingrese el valor del objeto 4: "
precio1=float(input(dato))
descuento1=precio1*15/100
valor_final=precio1-descuento
a52="el importe a pagar del objeto con el 15% es de: "
print( a52 + f"{valor_final:.2f}")

valor=float(input("inserte el importe del producto 5: "))
ahorro=valor*15/100
importe_a_pagar=valor-ahorro
print("EL COSTO FINAL DEL PRODUCTO ES: "+f"{importe_a_pagar:.2f}")
'''Vamos a ver a continuación un programa para la generación de un ticket de venta.Así que vamos a hacer lo siguiente. 
Vamos a suponer que compramos varios artículos en el supermercado y queremos obtener el ticket de venta total, incluyendo los impuestos.
El sistema deberá solicitar el precio de cada producto a comprar y el usuario deberá indicar su precio
y este valor puede contener punto decimal. Finalmente, el sistema debe de realizar la suma de cada producto, calcular el impuesto 
y finalmente imprimir el total de la compra.'''
#Así que vamos a realizar este ejemplo.
producto1=float(input("Ingrese aqui el precio con decimales de su primer articulo: "))
producto2=float(input("Ingrese aqui el precio con decimales de su segundo articulo: "))
producto3=float(input("Ingrese aqui el precio con decimales de su tercer articulo: "))
producto4=float(input("Ingrese aqui el precio con decimales de su cuarto articulo: "))
producto5=float(input("Ingrese aqui el precio con decimales de su quinto articulo: "))
producto6=float(input("Ingrese aqui el precio con decimales de su sexto articulo: "))
descuento=int(input("Ingrese el descuento que figura como promocion para este dia: "))
suma=producto1+producto2+producto3+producto4+producto5+producto6
descuento1=suma*descuento/100
iva=suma*21/100
total=suma-descuento1+iva
print(f'''****ALMACEN SANTI*****
Detalle de la compra
producto 1.............$ {producto1}
producto 2.............$ {producto2}
producto 3.............$ {producto3}
producto 4.............$ {producto4}
producto 5.............$ {producto5}
producto 6.............$ {producto6}
------------------------------------
Subtotal..............$ {suma:.2f}
------------------------------------
Desc. del {descuento}%..........$ {descuento1:.2f}
------------------------------------
IVA 21%................$ {iva:.2f}
------------------------------------
TOTAL ................$ {total:.2f}
------------------------------------''')

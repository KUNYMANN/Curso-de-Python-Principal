'''Crear un programa para convertir una calificación numérica entre cero y diez a una
letra de la F a la A y Vamos a aplicar las siguientes condiciones Si es mayor o igual a nueve y menor
o igual a diez, entonces es una letra A.
Por otro lado, si es mayor o igual a ocho y además menor a nueve, corresponde a la letra B.
Por otro lado, si es mayor o igual a siete y menor a ocho corresponde a la letra C y además también
si es mayor o igual a seis y menor a siete.
Corresponde a la letra D, si es mayor o igual a cero y menor a seis corresponde a la letra F
 y en cualquier otro caso se debe de mandar a imprimir valor desconocido.'''

calificacion=float(input("Ingrese una calificacion del 1 al 10: "))

if calificacion>=9 and calificacion<=10:
    print(f"La calificacion {calificacion} ingresada corresponde a la letra A")
elif calificacion>=8 and calificacion<=9:
    print(f"La calificacion {calificacion} ingresada corresponde a la letra B")
elif calificacion>=7 and calificacion<=8:
    print(f"La calificacion {calificacion} ingresada corresponde a la letra C")
elif calificacion>=6 and calificacion<=7:
    print(f"La calificacion {calificacion} ingresada corresponde a la letra D")
elif calificacion<6 and calificacion>=0:
    print(f"La calificacion {calificacion} ingresada corresponde a la letra F")
else:
    print("Valor desconocido")
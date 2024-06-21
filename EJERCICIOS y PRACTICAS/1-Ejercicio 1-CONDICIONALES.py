# Hacer un programa que pida dos numeros y se de cuenta cual de ellos
# es par, o si ambos son par

dato1=int(input("ingrese un numero: "))
dato2=int(input("ingrese otro numero: "))
if dato1%2==0 and dato2%2==0: #aqui estamos dividiendo al dato1 por dos y si el resto es cero el resultado es un numero par,
                              #y lo hacemos de esta manera para ver si ambos lo son
    print("ambos numeros son par")
elif dato1%2==0 and dato2%2!=0:
    print(f"{dato1} es un numero par")
elif dato1%2!=0 and dato2%2==0:
    print(f"{dato2} es un numero par")
    
else:
    print("ambos numeros son impares")
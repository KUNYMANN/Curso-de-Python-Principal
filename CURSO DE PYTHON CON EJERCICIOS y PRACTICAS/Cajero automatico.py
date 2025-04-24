print( "***CAJERO AUTOMATICO***")
print("""...MENU:
      1- Depositar
      2- Retirar
      3- Consultar Saldo
      4- Salir""")


saldo_actual=1000 
salir=False 
while not salir:
        menu=int(input("Ingrese el numero de operacion que desea realizar: "))
        if menu==1:
          deposito=float(input("Ingrese el monto a depositar $: "))
          saldo_actual+=deposito
          print (f"Su saldo actual es $: {saldo_actual:.2f} ")
        
        elif menu==2:
           retiro=float(input("Ingrese el monto a extraer $: "))
           if retiro<=saldo_actual:
              saldo_actual-=retiro
              print (f"Su saldo actual es $: {saldo_actual:.2f} ")
           else:
              print("No dispones de fondos suficientes para realizar la extracción")
        elif menu==3:
         print(f"Su saldo es $: {saldo_actual:.2f}")
         
        elif menu==4:
         print("Gracias por operar con nuestro Banco")
         salir=True
        else :
           menu!= 1 and 2 and 3 and 4
           print("Error al ingresar el numero de operacion")
        
'''
saldo1=1000
retiro=int(input("monto a extraer: "))
saldo1-=retiro
print("su saldo es: ", saldo1)'''
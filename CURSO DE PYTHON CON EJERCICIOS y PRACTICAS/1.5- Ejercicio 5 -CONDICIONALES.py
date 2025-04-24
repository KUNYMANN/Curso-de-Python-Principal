#Hacer un programa que simule un cajero automatico con 
# un saldo inicial de 1000 y el siguiente menu de opciones:
# INGRESAR DINERO A LA CUENTA
# RETIRAR DINERO DE LA CUENTA
# MOSTRAR DINERO DISPONIBLE
# SALIR
saldo_inicial=1000
print("\t.:MENU:.") #el ("\t.:  .") es para que cuando se imprima el titulo aparezca despazado del margen unos 4 espacios
print("1.INGRESAR DINERO A LA CUENTA")
print("2.RETIRAR DINERO DE LA CUENTA")
print("3.MOSTRAR DINERO DISPONIBLE")
print("4.SALIR")
opcion=int(input("Digite una opcion de MENU: "))
print() # este print(vacio) es para hacer un salto de renglon al print("jhhdhdh") siguiente


if opcion==1:
    deposito=float(input("Ingrese el monto a depositar: "))
    saldo_inicial+=deposito #que es lo mismo qu escribir saldo_inicial= saldo_inicial + deposito
    print(f"Saldo acumulado $: {saldo_inicial:.2f}") 


elif opcion==2:
    extraccion=float(input("Importe a retirar: "))
  

    if extraccion>saldo_inicial:
        print("Saldo insuficiente")
    else:
        saldo_inicial-=extraccion
        print(f"Saldo Actual $ {saldo_inicial}")
elif opcion==3:
    print(f"Saldo Actual $ {saldo_inicial}")
elif opcion==4:
    print("good bye")
else:
    ("Error al ingresar la opcion de MENÚ")
'''

def mostrar_menu():    #muestra las opciones del MENU
    print("\nMENÚ:")
    print("1. Ingresar dinero a la cuenta")
    print("2. Extraer dinero de la cuenta")
    print("3. Mostrar Saldo")
    print("4. Gracias por operar con nuestro BANCO")

def ingresar_dinero(saldo):#solicita al usuario que ingrese un importe que lo suma al saldo actual y retorna el nuevo saldo
    cantidad=float(input("Ingrese el monto a depositar $: "))
    saldo+=cantidad
    print(f"Has ingresado $  {cantidad}. El nuevo saldo es $ {saldo}")
    return saldo

def extraer_dinero(saldo): #solicita al usuario el monto que va a extraer y 
    cantidad=float(input("Ingrese el importe a extraer $: "))
    if cantidad > saldo: #si la cantidad es mayor al saldo muestra el error de saldo insuficiente
        print("SALDO INSUFICIENTE")
    else:
        saldo -= cantidad # caso contrario si hay saldo va a restar la extraccion del ultimo saldo y lo devuelve actualizado
        print(f"Has extraido $ {cantidad}. El nuevo Saldo es de $: {saldo}.")
    return saldo
    
def mostrar_el_saldo(saldo): #muestra el saldo actual
    print(f"El saldo actual es $: {saldo}")

def main():                      #es el bucle principal del programa. Muestra el menu y solicita una opcion al usuario. 
    saldo=0.0                    #Segun la opcion ingresada, llama a la funcion correspondiente, si el usuario selecciona salir,
    while True:                  #rompe el bucle y termina el programa
        mostrar_menu()
        opcion=input("Seleccione una opción: ")
        if opcion=="1":
            saldo=ingresar_dinero(saldo)
        elif opcion=="2":
            saldo=extraer_dinero(saldo)
        elif opcion=="3":
            mostrar_el_saldo(saldo)
        elif opcion=="4":
            print("Gracias por operar con nuestro BANCO")
            break 
        else:
            print("Opcion No Valida.Por favor ingrese una opción valida")
if __name__=="__main__":
        main()
    '''         


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
        
'''El título es Aplicación de cajero automático Tres asteriscos y posteriormente vamos a definir la variable

de saldo inicial.

El valor de mil obviamente puede ser cualquier otro valor, el saldo inicial.

Posteriormente definimos la variable de salir con el valor inicial de falso.

Y posteriormente vamos a utilizar esta variable para poder iterar nuestro menú utilizando un ciclo while.

Agregamos la siguiente validación mientras la variable de salir no sea verdadera, entonces vamos a

estar iterando este menú y entonces agregamos también una cadena multilínea y agregamos nuestro menú.

Operaciones que puedes realizar en el sistema de cajero automático.

Entonces podemos consultar el saldo y hacer la primera opción.

Posteriormente podemos retirar, podemos retirar de nuestra cuenta y también podemos depositar dinero

a nuestra cuenta.

Y finalmente la opción cuatro es la opción de salir bien.

Así que con esto ya tenemos el menú y vamos a pedir.

Ahora el usuario que seleccione una opción va a proporcionar un valor numérico.

Por lo tanto, realizamos una conversión a un tipo entero y le pedimos escoge una opción dos puntos

espacio y empezamos a agregar las opciones de nuestro menú si la opción es igual al valor de uno, entonces

quiere decir que queremos consultar el saldo.

Aquí está mal escrito, tiene que ser Consultar saldo.

Lo corregimos y mandamos a imprimir.

Tu saldo actual es imprimimos el carácter de moneda, imprimimos el saldo y agregamos un formato de

dos dígitos y al final agregamos un salto de línea para que la siguiente vez que se muestre el menú

se agregue un salto de línea.

Así que esta es la opción uno.

Ahora, si agregamos la opción dos, la opción dos en este caso será la opción de retirar.

Sin embargo, antes de retirar, vamos a agregar una validación.

En primer lugar, le vamos a pedir al usuario que proporcione la cantidad a retirar.

Este va a ser un valor de tipo flotante, así que puede proporcionar valores de tipo flotante.

Le pedimos ingresa el monto a retirar dos puntos espacio y con esta variable de retiro vamos a agregar

la siguiente validación.

Si la variable de retiro es menor o igual que el saldo, entonces quiere decir que si podemos realizar

el retiro utilizando el operador compuesto para modificar la variable de saldo le vamos a restar el

valor que queremos retirar.

Recordemos que esto es equivalente a modificar la variable de saldo haciendo la resta de saldo menos

el valor que queremos retirar.

El valor que tenemos en la variable de retiro y posteriormente mandamos a imprimir tu nuevo saldo es

dos puntos y mandamos a imprimir la variable de saldo solamente dos dígitos flotantes.

Aquí me faltó al principio la f para que sea un f string y finalmente un salto de línea.

Bien, así que ya mandamos a imprimir tu nuevo saldo es el carácter de moneda.

Posteriormente la variable de saldo únicamente con dos dígitos de punto flotante y un salto de línea

al final.

Bien, esa es 1/1 de la validación.

En caso de que la variable de retiro el monto a retirar sea menor o igual que el saldo, entonces podemos

realizar la operación sin ningún problema, pero en caso contrario si el monto a retirar es mayor que

el saldo, entonces mandamos a imprimir.

No cuentas con el saldo suficiente.

El saldo actual es e imprimimos el saldo actual dando un formato de dos dígitos y también un salto de

línea.

Bien, así que con eso ya terminamos la opción dos para hacer un retiro.

Vamos a programar ahora la opción tres, que es la opción de depositar.

Así que agregamos un bloque más un bloque Elif y agregamos la nueva condición.

Si la opción es igual a tres, entonces vamos a pedir el depósito.

Definimos esta variable de depósito.

Vamos a convertir el valor a un tipo flotante y le pedimos al usuario ingresa el monto a depositar dos

puntos espacio y vamos a modificar la variable de saldo.

Le vamos a sumar el valor de la variable de depósito.

Recordemos que esto es equivalente a modificar la variable de saldo saldo más el depósito.

Bien, con esto ya hemos modificado el saldo y entonces ya estamos listos para mandar a imprimir el

mensaje.

Tu nuevo saldo es.

Ya hemos modificado este valor.

Mandamos a imprimir la variable de saldo, damos el formato y un salto de línea.

Bien, con esto ya tenemos la opción de depósito.

Y por último vamos a agregar la opción cuatro.

Recordemos que la opción cuatro es la opción de salir, así que mandamos a imprimir el mensaje Saliendo

del cajero automático.

Hasta pronto.

Y aquí lo más importante es cambiar el valor de la variable de salir a verdadero para que la siguiente

vez que se ejecute este ciclo, esta variable va a cambiar el valor a verdadero y al aplicarle el operador

NOT esta expresión cambia el valor a falso, termina de ejecutarse el ciclo while y termina de ejecutarse

nuestra aplicación.

También podemos agregar por último la opción else para mandar a imprimir el mensaje.

Opción inválida.

Selecciona otra opción y un salto de línea.

Recordemos que también terminando este ciclo while podemos agregar un bloque else.

Así que terminando este ciclo while podremos agregar un bloque else de manera opcional, por ejemplo

con el mensaje terminando la aplicación de cajero automático.

Como hemos comentado esto es opcional ya que se parece al mensaje anterior de saliendo del cajero automático.

Sin embargo, es para que sepan que también se puede agregar esta opción en caso de que así lo necesiten.

Cuando termina de ejecutarse este ciclo while.

Bien, prácticamente con esto ya tenemos todo nuestro código.

Vamos a comprobar.

Nos muestra el menú, Proporcionamos la opción uno de Consultar saldo.

El saldo actual es de mil.

Ahora vamos a hacer un retiro si queremos hacer un retiro mayor al saldo actual, por ejemplo, queremos

retirar 1500.

Podemos observar que nos muestra el mensaje.

Ya se ha aplicado la validación, no cuentas con el saldo suficiente.

Saldo actual es de mil.

Ahora vamos a hacer un retiro que sea exitoso.

Por ejemplo, queremos retirar solamente 200 y entonces el nuevo saldo es de 800.

Ahora vamos a hacer un depósito, vamos a sumar 500 y entonces el saldo anterior era de 800, sumamos

500.

Por lo tanto ahora el saldo actual es de 1300 y si volvemos a consultar el saldo podemos observar que

el saldo actual ya es de 1300, ya se ha modificado.

Y por último, si proporcionamos la opción cuatro, nos muestra el mensaje saliendo del cajero automático

y además también el bloque else del ciclo while.

Terminando la aplicación de cajero automático.

Así que con esto ya hemos programado por completo nuestra aplicación.

'''
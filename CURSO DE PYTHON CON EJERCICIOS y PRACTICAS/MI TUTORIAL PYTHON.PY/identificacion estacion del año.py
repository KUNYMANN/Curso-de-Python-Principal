'''se solicita proporcionar el valor de un mes.
En este caso va a ser un valor numérico entre uno y 12 y después de proporcionar este valor debemos
indicar la estación del año según lo siguiente.
Si se proporciona el valor de mes uno, dos o 12, la estación correspondiente es la estación de verano.
Obviamente es un cálculo aproximado ya que no corresponde exactamente el mes con la estación respectiva,
pero es para que podamos poner en práctica lo que hemos visto hasta el momento.
Así que si el mes es uno, dos o 12, la estación que tienen que mandar a imprimir es verano.
Posteriormente, si el mes es tres, cuatro o cinco, la estación es otoño.
Si el mes es 67U8, la estación que deben de mandar a imprimir es invierno y si el mes es nueve, diez
u 11, la estación que tienen que mandar a imprimir es primavera.
Cualquier otro valor tiene que mandar a imprimir el mensaje Estación desconocida.
Así que utilizando la sentencia if else, les pedimos resolver este ejercicio.'''

mes=int(input("Ingrese un numero para saber que mes es y a que estacion corresponde: "))
mes<=12
if mes==12 or mes==1 or mes==2:
   print('el mes elegido corresponde a la estacion VERANO')
elif mes ==3 or mes==4 or mes==5:
      print('el mes elegido corresponde a la estacion OTOÑO')
elif mes==6 or mes==7 or mes==8:
      print('el mes elegido corresponde a la estacion INVIERNO')
elif mes==9 or mes==10 or mes==11:
   print('el mes elegido corresponde a la estacion PRIMAVERA')
else:
   print("Estacion desconocida")
'''crear un programa para validar el usuario y password proporcionados por el usuario.
Van a crear dos constantes para definir los valores correctos y posteriormente van a comparar los valores
de usuario y password proporcionados por el usuario y verificar que sean válidos.
Se debe de solicitar el usuario y el password al usuario y si son iguales que los valores correctos
almacenados en las constantes de manera interna en nuestro programa, entonces debe de mandar a imprimir
verdadero.
Quiere decir que los valores son correctos, los valores de usuario y password, de lo contrario debe
de mandar a imprimir falso.
Así que en este caso ambos valores deben de ser correctos el valor de usuario y el valor de password
y vamos a ejecutar nuestro sistema para que vean exactamente lo que se les está solicitando.
En primer lugar, el título Sistema autenticación.
Posteriormente van a preguntar cuál es el usuario y de manera interna tenemos dos constantes almacenando
los valores correctos.
En este caso vamos a proporcionar los valores correctos, que son los valores de admin para el usuario
y el valor de password 123.
Si el usuario proporciona estos valores, entonces va a responder con verdadero datos correctos el valor
de true.'''


print("***SISTEMA DE AUTENTICACION***")
nombreUsuario=input("Ingrese su nombre de usuario: ")
clave=input("Ingrese su clave numeral de tres digitos: ")
usuario="Admin"
password='123'
verificacion=nombreUsuario.strip()==usuario and clave.strip()==password
print(f'Los datos ingresados son: {verificacion}')



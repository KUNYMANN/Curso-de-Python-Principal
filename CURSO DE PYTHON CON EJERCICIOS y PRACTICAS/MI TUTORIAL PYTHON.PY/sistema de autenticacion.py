'''realizar a continuación el siguiente sistema de autenticación.
Así que se les pide crear un sistema para validar los valores de usuario y password proporcionados.
Se deben definir dos constantes con los valores válidos de usuario y password.
Por otro lado, el sistema debe comparar los valores válidos contra los valores proporcionados.
Se deben de considerar cuatro casos.
El primer caso.
Si el usuario y password son válidos, entonces se debe de mandar a imprimir.
Bienvenido al sistema.
Por otro lado, si el usuario es inválido, entonces se debe de volver a solicitar el valor de usuario.
Por otro lado, si el password es el que es incorrecto, entonces se debe de pedir de nueva cuenta el
valor de password.
Y por último, si tanto el usuario y el password son inválidos, entonces se debe de indicar que debe
de corregir los dos valores.'''

nombre_usuario="KunyMann66"
clave="MaRiTa68"
usuario=input("Ingrese su nombre de usuario: ")
contraseña=input("Ingrese su contraseña: ")
if usuario==nombre_usuario and contraseña==clave:
    print("***Bienvenido al Sistema***")

elif usuario!=nombre_usuario and contraseña==clave:
    print("Error USUARIO, vuelva a ingresar")

elif usuario==nombre_usuario and contraseña!=clave:
    print("Error CONTRASEÑA, vuelva a ingresar")

else: 
    print("Los DATOS ingresados son inválidos")

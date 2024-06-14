# LOS TITULOS SE DENOMINAN "key"(clave) Y LOS DATOS SE DENOMINAN "value" (valor)
# LAS VARIABLES LLEVAN UN TITULO LA "KEY" QUE LE ASIGNAMOS, ESTAS SE DECLARAN Y LA VARIABLE PROPIAMNTE DICHA ES EL "VALOR", LO QUE SE PUEDE VARIAR, EL DATO QUE DEFINIMOS ASIGNARLE 
# O SEA UNA VARIABLE ESTA COMPUESTA POR UN TITULO Y UN DATO, Y SE EXPRESA DE ESTA MANERA...TITULO "KEY" =  DATO "VALUE"
# EJEMPLO: TITULO DE LA VARIABLE...COLOR = LA VARIABLE ES EL DATO QUE LE ASIGNEMOS... ROJO-VERDE-AZUL EL QUE FUERE

a=8             # a es la clave KEY y 8 es el VALOR
b=3
c= a+b  
print(c)
#EN EL PRINT SE COLOCA EL TITULO DE LA VARIABLE PARA QUE MUESTRE EL DATO DE LA VARIABLE
nombredelusuario="Kuny Mann"
print(nombredelusuario)
#EN ESTE CASO LA CONSOLA MOSTRARIA  Kuny Mann
nombre= 40+20
print(nombre)
#EN ESTE CASO LA CONSOLA MOSTRARIA  60

#ESTOS EJEMPLOS MUESTRAN LAS DOS FORMAS QUE SE PUEDE REPRESENTAR LAS VARIABLES PARA QUE EL PRINT NOS MUESTRE LO MISMO
numero=6
numero=6+3
print(numero)

numero=6
numero+=3
print(numero)

# INCLUSIVE SE PUEDEN COLOCAR NUMEROS NEGATIVOS
numero=-11
numero+=9
numero-=8
print(numero)

# EL TITULO DE NOMBRE EN ESTE CASO "+ NOMBRE +" SE PUEDE REEMPLAZAR POR LAS LLAVECITAS ENCERRANDO LA PALABRA NOMBRE {nombre}
nombre="Marita"
bienvenida="Hola " + nombre + " ¡Como estas!"
print(bienvenida)


# DEFINIMOS UNA VARIABLE
nombre= 7

# CONCATENAR UN CARACTER NUMERAL CON UN TEXTO, COLOCANDO f DELANTE DE LA VARIABLE DESIGNADA, AUTOMATICAMENTE TRANSFORMA AL / LOS CARACTERES EN TEXTO
#CONCATENAR CON +
bienvenida="Hola " + "¡Como estas!"

#CONCATENAR CON f STRINGS
bienvenida=f"Hola {nombre} ¡Como estas!"

print(bienvenida)

#borrar una Variable
nombre= 7
bienvenida=f"Hola {nombre} ¡Como estas!"
del nombre
print(bienvenida)

#OPERADORES DE PERTENENCIA (in / not in)
nombre= 7
bienvenida=f"Hola {nombre} ¡Como estas!"
print("kuny" in bienvenida)
print("kuny" not in bienvenida)

# EL TITULO DE UNA VARIABLE DE DOS O MAS PALABRAS NO LLEVAN ESPACIOS VACIOS....LAS VARIABLES SI (Ejemplo: tituladelavariable o titulo_de_la_variable)
# EXISTEN VARIAS FORMAS DE EXPRESARLO SEGUN EL PROGRAMA o lenguaje QUE USEMOS
# EJEMPLO titulo_honorifico_del_rey_de_irlanda   =    "Jack II de Cork" (asi se escribe en PYTHON y se llama Snak_case)
# EJEMPLO tituloHonorificoDelReyDeIrlanda  =   "Jack II de Cork" (asi se escribe en JAVASCRIPT y se llama CamelCase)








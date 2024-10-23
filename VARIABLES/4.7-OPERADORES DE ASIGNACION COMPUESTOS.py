'Los operadores de asignacion compuestos combinanuna operacion aritmetica con una asignacion, haciendo las operaciones mas consisas'
#Los operadores cvom'puestos pueden se: +=, -=, *=, /=, etc.
'sintaxis operador asignacion compuesto'
variable_OPERADOR="valor" #(definimor una variable, le agregamos el operador de asignacion compuesto y luego le damos un valor)
contador=5
contador+=7 #Esto significa "contador es igual a contador mas siete" contador=5+7 
print(f"el resulktado es {contador}") #contador es igual a 12

contador1=10
contador1*=3
print(f"el resulktado es {contador1}")
contador1/=5
print(f"el resulktado es {contador1}")

'SE VA UTILIZANDO EL VALOR DE ARRASTRE DE LA ULTIMA OPERACION'
num1=10
print(num1)#10
num1+=10 #aqui le pido que sume a la variable el valor que le asigno
print(num1)#20
num1-=6 #aqui le pido que reste a la variable el valor que le asigno
print(num1)#14
num1*=30 #aqui le pido que multiplique a la variable por el valor que le asigno
print(num1)#420
num1**=4 #aqui le pido que eleve a la variable al valor que le asigno
print(num1)#31116960000
num1//=100 #aqui le pido que divida a la variable por el valor que le asigno y me arroje el resultado entero sin decimales
print(num1)#311169600
num1/=10 #aqui le pido que divida a la variable por el valor que le asigno
print(f"{num1:.3F}") ##aqui le pido que me devuelva el resultado con un maximo de tres decimales 31116960.000
num1%=51#aqui le pido que me de el resto de la divicion por el valor que le asigno
print(num1)#24.0
"Utilizando los operadores compuestos pero reiniciando el valor de 'a' para que no attastre el resultado"
a,b=10,15
print(f"El valor inicial de a:{a} y el valor de b:{b}") #10 y 15
#operafdor compuesto de suma +=
a+=b # a=a+b
print(f"El operaedor de a+=b es:{a}")#25
#operador compuesto de resta
a=10 #aqui estamos reiniciando la variable "a"
a-=b # a=a-b
print(f"El operaedor de a-=b es:{a}")#-5
#operador compuesto multiplicacion
a=10 #aqui estamos reiniciando la variable "a"
a*=b # a=a*b
print(f"El operaedor de a*=b es:{a}")#150
#operador compuesto division
a=90 #aqui estamos reiniciando la variable "a" y le asignams un nuevo valor
a/=b # a=a*b
print(f"El operaedor de a/=b es:{a}")#6.0
#operador compuesto modulo (resto de una division)
a=87 #aqui estamos reiniciando la variable "a" y le asignams un nuevo valor
a*=b # a=a*b
print(f"El operaedor de a*=b es:{a}")#1305
#operador compuesto division exacta
a=65 #aqui estamos reiniciando la variable "a" y le asignams un nuevo valor
a//=b # a=a*b
print(f"El operaedor de a//=b es:{a}")#4
#operador compuesto exponenciacion
a=10 #aqui estamos reiniciando la variable "a"
b=3 #aqui estamos reiniciando la variable "b" y le asignams un nuevo valor solo para que el resultado no sea tan grande
a**=b # a=a*b
print(f"El operaedor de a**=b es:{a}")#1000
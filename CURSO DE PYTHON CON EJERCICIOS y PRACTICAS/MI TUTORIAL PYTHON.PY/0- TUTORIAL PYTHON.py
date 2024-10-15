#VARIABLES
# a y b hacen referencia al objeto que representa al entero 1
# Referencian a la misma dirección de memoria
'La función id() devuelve un identificador único del objeto que se le pasa como parámetro'
a = 1
b = 1
print(id(1))
4299329328
print(id(a))
4299329328
print(id(b))
4299329328
# b es asignado con el objeto que representa el entero 2
# a y b referencian a diferentes direcciones de memoria
# a mantiene la referencia al entero 1
b = 2
print(id(a))
4299329328
print(id(b))
4299329360
# a es asignada con el valor de b
# a y b referencian al mismo objeto y, por tanto,
# a la misma dirección de memoria
a = b
print(id(a))
4299329360
print(a)
2

#Asignar un valor a múltiples variables
' es hacer referencia al mismo objeto '
a=b=c=1 # el primer dato seguido del = es una variable y el ultimo dato despues del = es el valor de la variable
# o sea variable "a" = variable "b" = variable "c" = valor de las variables "1"
print(a) 
1
print(b)
1
print(c)
1
print(1)
1

#TIPOS DE DATOS

'''Python define tres tipos de datos numéricos básicos: enteros, números de punto flotante (simularía el conjunto de los números reales, 
pero ya veremos que no es así del todo) y los números complejos.'''

#numeros binarios (0 y 1)
'Los números en binario, se antepone 0b a una secuencia de dígitos en binario (0 y 1)'
diez = 10
print(diez)
10
diez_binario = 0b1010
print(diez_binario)
10
'Los números octales se crean anteponiendo 0o a una secuencia de dígitos octales (del 0 al 7)'
diez_octal = 0o12
print(diez_octal)
10
'Para crear un número entero en hexadecimal, hay que anteponer 0x a una secuencia de dígitos en hexadecimal (del 0 al 9 y de la A la F).'
diez_hex = 0xa
print(diez_hex)
10

#numeros flotantes
punto_flotante=1.1 + 2.2 #es un float
print(punto_flotante)
3.3000000000000003  # Representación aproximada de 3.3
print(f'{punto_flotante:.2f}')
3.30  # real mostrando únicamente 2 cifras decimales
un_real = 1.1  # El float literal debe incluir el carácter .
otro_real = 1/2  # El float tambien puede ser el resultado de una operacion ejemp. 1 dividido 2 
not_cient = 1.23E3  # El float se puede utilizar con notación científica (1230.0)

#numeros complejos
'''Los números complejos tienen una parte real y otra imaginaria
y cada una de ellas se representa como un float.'''
complejo = 1+2j
complejo.real
1.0
complejo.imag
2.0

#ARITMETICA
'''A todos los tipos numéricos se pueden aplicar las operaciones de la aritmética: suma, resta, producto, división
y se pueden mezclar los distintos tipos'''
suma=1 + 2.0
print(suma) #Entendemos que el tipo int es menor que el tipo float que a su vez es menor que el tipo complex.
3.0
suma_complejos=2+3j + 5.7 
print(suma_complejos) # (2.0 + 5.7 + 3j)
(7.7+3j)

#TIPO DE BOOLEANO
#En Python la clase que representa los valores booleanos es bool. 
# Esta clase solo se puede instanciar con dos valores/objetos: "True" para representar verdadero y "False" para representar falso.
'''Una particularidad del lenguaje es que cualquier objeto puede ser usado en un contexto donde se requiera comprobar si algo es verdadero o falso.
Por tanto, cualquier objeto se puede usar en la condición de un if o un while'''
#cualquier objeto es verdadero menos
'''Que implemente el método __bool__() y este devuelva False.
   Que impleménte el método __len__() y este devuelva 0.'''
#ademas es falso en estas instancias/objetos
'''None
   False
   El valor cero de cualquier tipo numérico: 0, 0.0, 0j, …
   Secuencias y colecciones vacías: '', (), [], {}, set(), range(0)'''

#TIPOS DE CADENAS DE CARACTERES
'Este tipo es conocido como string aunque su clase verdadera es str.'
'un string es una secuencia inmutable de caracteres en formato Unicode.'
'''Si en la cadena de caracteres se necesita usar una comilla simple, tienes dos opciones: usar comillas dobles para encerrar el string, 
o bien, usar comillas simples pero anteponer el carácter \ a la comilla simple del interior de la cadena. El caso contrario es similar.'''
hola = 'Hola "Pythonista"'
hola_2 = "Hola 'Pythonista'"
hola_3 = 'Hola \'Pythonista\''
print(hola) #Hola "Pythonista"
print(hola_2) #Hola 'Pythonista'
print(hola_3) #Hola 'Pythonista'
'''A diferencia de otros lenguajes, en Python no existe el tipo «carácter».
No obstante, se puede simular con un string de un solo carácter:'''
caracter_a = 'a'
print(caracter_a) #a



'''
class Persona:
    private: 
    int Numero_Telefono
    str Domicilio

    public:  
    int Dni
    str Nombre



Persona Santi,Kuny,Marita,Gorda

Santi.Dni='44496778'

print(Santi.Dni)'''


 
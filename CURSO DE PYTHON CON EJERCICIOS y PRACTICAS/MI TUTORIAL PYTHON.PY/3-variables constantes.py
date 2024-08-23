#TECNICA PARA MANEJAR VARIABLES Y CONSTANTES
'''las variables se llaman asi devido a que pueden variar sus datos o valores, esto quiere decir que 
las variables estan sujetas a constantes cambios'''
'hay otro tipos de datos que se llaman constantes, y se denominan asi porque su valor o dato jamas va a cambiar'
#Ejemplo:
#necesito una variable que contenga una cantidad de personas
cantidad_personas=100
#esta cantidad de personas en un contexto particular, puede cambiar sea que aumente o disminuya 
#o sea que va a estar cambiando constantemente
print(cantidad_personas) # imprime por consola 100
#que pasa si ingresan mas personas, como lo modifico, voy a llamar a la variable que ya habia creado
#en este caso 
cantidad_personas=150 # y voy a agregarle el nuevo valor
print(cantidad_personas) # imprime por consola 150
# que esta ocurriendo, se asigna un valor a cantidad_personas=100 y cuando lo modifique al valor
#tambien va a modificarlo por consola, esto nos muestra que las variables pueden cambiar sus valores o datos
'PARA EL CASO DE LAS CONSTANTESN ES MAS COMPLEJO Y NO ES PROPIO DE PYTHON'
#pero para la practica existe un metodo bastante comun que es colocar a la variable en MAYUSCULAS
'una variable en MAYUSCULAS hace referencia que va a ser una constante y que ese valor no deberia de ser modificado'
#si bien no es una regla del Lenguaje en si de Python, es una practica que entre programadores se conoce
#Ejemplo:
#tomemos el valor de PI este valor nunca va a cambiar entonces a esa variable la denomino en MAYUSCULAS
pi=3.14 #de esta manera colocandolo en minuscular yo puedo variar el valor asignado a pi
print(pi) # 3.14
"""pero sabemos que el valor de pi nunca va a cambiar, entonces para decirle a otro programador o alguien
que lea este codigo que su valor es una CONSTANTE, y LA ESCRIBO EN MAYUSCULAS""" 
#Esto es solo una practica que se utiliza en Python para identificar una variable con un valor constante y que no debe ser modificado
PI=3.141516
print(PI)


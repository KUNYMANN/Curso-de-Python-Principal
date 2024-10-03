#SUB-CADENAS 
'Una subcadena es una parte de una cadena principal, y hay varias maneras de extraer subcadenas en Python'
"Podemos extraer Subcadenas, buscarlas, reemplazarlas, entre otras operaciones"
'''Para extraer una subcadena podemos utilizar el concepto de "SLICING" o segmentacio, y este permite indicar el indice de inicio
y el indice final, sin incluir este ultmo caracter (recordemos es "hasta" NO "inclusive")
esto es para obtener una subcadena de una cadena original'''
#MANEJO DE SUB-CADENAS
cadena="Hola, Campeon de la vida!!"
sub_cadena=cadena[6:]
print(f"Aqui obtendremos la siguiente sub-cadena que corresponde a : {sub_cadena} ") #obtenemos la sub-cadena de la original en este caso "Campeon de la vida!!"
sub_sub_cadena=sub_cadena[0:7]
print(sub_sub_cadena)#obtenemos la sub_sub-cadena de la original en este caso "Campeon" que son los indices extraidos de la subcadena de la cadena original

print()

#BUSCAR SUB-CADENAS
'Para buscar subcadenas dentro de una cadena original urtilizamos el metodo find()'
texto="viva la vida?"
buscar_subcadena=texto.find("vi"),texto.find("vida")
print(buscar_subcadena)# (0, 8)
nueva=texto.find("V")
print(f"ya que el caracter solicitado no esta, va a arrojar un {nueva} siempre")#Python es sencible a MAYUSCULAS y minusculas, la busqueda debe hacerse  
                                                                                #exactamente igual a como esta escrito en la cadena original
print()

#REEMPLAZO DE SUB-CADENAS
'Utilizando el metodo .replace() reemplazamos una subcadena por otra dentro de una cadena principal'
original_cadena="Buenos Dias!!"  #no se reemplaza la cadena original, porque es inmutable, sino que se genera una nueva cadena u objeto
print(f"la cadena original es: {original_cadena}")
reemplazo_total=original_cadena.replace("Buenos","Hermosa").replace("Dias", "Tarde".upper()) #la nueva cadena va a llevar otro nombre de variable, con el nuevo valor/objeto reemplazado
print(f"la nueva cadena reemplazada es: {reemplazo_total}")#Hermosa TARDE!!
print(len(original_cadena))#13
print(len(reemplazo_total))#15

print()

#SEPARAR SUB-CADENAS
'Como extraer una subcadena de una cadena original con la funcion SPLIT(), este metodo permitre dividir una cadena en "una lista" de subcadenas basadas en un caracter separador'
"En caso de no haber un caracter separador Split() utiliza los espacios en blanco"
#Ejemplo
datos="Juan, 30, Mexico"
print(datos)#Juan, 30, Mexico
print(type(datos))#<class 'str'>
print(len(datos))#16
lista=datos.split(",") #con este metodo separamos en lista una cadena
print(lista)#['Juan', ' 30', ' Mexico']
print(lista[1:2])#[' 30']
print(len(lista))#3

print()

elementos="arena y sol, el mar azul"
print(elementos)#arena y sol, el mar azul
print(type(elementos))#<class 'str'>
print(len(elementos))#24
sub_elementos=elementos.split(",") #con este metodo separamos en lista una cadena
print(sub_elementos)#['arena y sol', ' el mar azul']
print(type(sub_elementos))#<class 'list'>
print(len(sub_elementos))#2
print(sub_elementos[0])
nombre="Santiago"
saludo="Hola Santiago "  +  "buen dia!!"
print(saludo)

#IMPRIMIR con un solo print
print("como estan") # linea 1                se puede pedir que imprima en dos lineas de esta manera
print("manga de genios") # linea 2           ejemplo print linea 1 y print linea 2 o simplemente 
print("como estan\nmanga de genios") #       colocando "n\"" el resultado es igual, lo va a imprimir en dos lineas con un solo print, 

#IMPRIMIR con un varios print en una misma linea
cancion_de_cuna="Arroro mi Niño"
artista_compositor=" de Joan Manuel Serrat " "El Catalan"
print(cancion_de_cuna + artista_compositor); print(saludo) #de esta manera con el ";" se puede colocar otra orden "print" 
                                                           #que lo va a imprimir en el renglon siguiente, no es aconcejable 

# IDENTAR significa dejar cuatro espacios con el espaciador o un tablulado desde el borde izquierdo 
a=0
for i in range(5): # los ":" significa que lo que sigue a continuacion pertenece al mismo bloque por eso aparece indentado
    a+=1
    print(a)
    
print("HOLA buen dia!!")
nombre=input("Como te llamas: \n")
edad=input("que edad tienes: \n")
nacionalidad=input("De que nacionalidad eres: \n")
print()
print("Hola " + ( nombre) + " tienes " + ( edad)+" años de edad y eres de nacionalidad " + ( nacionalidad))
print()


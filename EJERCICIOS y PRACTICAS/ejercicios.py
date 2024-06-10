nombre="Santiago"
saludo="Hola Santiago "  +  "buen dia!!"
print(saludo)

cancion_de_cuna="Arroro mi Niño"
artista_compositor=" de Joan Manuel Serrat " "El Catalan"
print(cancion_de_cuna + artista_compositor); print(saludo) #de esta manera con el ";" se puede colocar otra orden "print" que lo va a imprimir en el renglon siguiente

# IDENTAR significa dejar cuatro espacios con el espaciador o un tablulado desde el borde izquierdo 
a=0
for i in range(5): # los ":" significa que lo que sigue a continuacion pertenece al mismo bloque por eso aparece indentado
    a+=1
    print(a)
    
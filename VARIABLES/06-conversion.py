#TIPOS CONVERSIONES DE 
#De un string a un Entero
resultado=input("Ingresa tu edad:")
print(type(resultado))
numero=int(resultado) # el INT va a tomar la variable puesta entre parentesis 
                      #y a tratar de  transformarla en un numero entero
print(numero+2) 
#existen varios factores de conversion
str(22) #a pesar de ser un numero lo transformara a texto(string)
float("22.13") #lo transformara en un numero con decimales
bool("") #esta funcion va a tomar lo que coloquemos dentro () y lo va a transformar en true o false
bool("un string") #en su mayoria evaluan en true/verdadero 
#solo en 4 ocasiones evalua en false
bool("false")
bool(0)
bool("")
bool(None)

     
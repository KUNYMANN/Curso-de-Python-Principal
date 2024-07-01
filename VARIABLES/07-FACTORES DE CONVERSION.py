#TIPOS CONVERSIONES DE 
#De un string a un Entero
resultado=input("Ingresa tu edad: ")
print(type(resultado))
numero=int(resultado) # el INT va a tomar la variable puesta entre parentesis 
                      #y a tratar de  transformarla en un numero entero
print(numero+2) 
#existen varios factores de conversion
a=str(22) #a pesar de ser un numero lo transformara a texto(string)
b=float("22.13") #lo transformara en un numero con decimales
c=bool("") #esta funcion va a tomar lo que coloquemos dentro () y lo va a transformar en true o false
bool("un string") #en su mayoria evaluan en true/verdadero 

#solo en 4 ocasiones evalua en false
d=bool("false")
e=bool(0) #siempre va a evaluar en falso
f=bool("") #siempre va a evaluar en falso
g=bool(None) #siempre va a evaluar en falso

h=bin(10) #convertir un numero entero a binario
h1=int("0b1010",2) #convertir un numero binario a entero
i=hex(10) #convertir un numero entero en hexagecimal
i1=int("0xa",16)#convertir un numero hexagesimal en entero
j=abs(-8) #hallar el valor absoluto de un numero, siempre te va a dar un numero positivo
k=round(15.5) #sirve para redondear un numero float tanto hacia arriba 
k1=round(15.2) #como hacia abajo
l=len("Kunymann 7") #ver cuantos caracteres componen la cadena inclusive contando los espacion vacios 

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(h1)
print(i)
print(i1)
print(j)
print(k)
print(k1)
print(l)




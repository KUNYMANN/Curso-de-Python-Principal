#NUMEROS ENTEROS
num1=40
print(type(num1)) # int
print(num1) # 40
print(float(num1))# 40.0 este print(float) me esta convirtiendo a un (int) entero
                  # en un flotante (float) lo que seria un numero con decimales,
                  #  aunque despues de la coma solo exista un cero
'todo numero que tenga una coma para python es un numero float'
print(type(float(num1))) # ahora paso de ser un int a un float

#NUMEROS FLOAT
num2= 43.16
print(num2) # 43.16
print(type(num2)) #float
print(int(num2)) #43 este print(int) me esta convirtiendo a un flotante (float)
                  # en un (int) entero, tomando la parte entera solamente y eliminando la parte decimal, no esta redondeando,
                  # deja de existir la coma, por mas que despues de la misma existan numeros como el (.16)
print(type(int(num2))) #ahora paso de ser un float a un int
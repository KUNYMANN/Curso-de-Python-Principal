import math

radio=float(input("coloqe el valor del radio: "))
area=(math.pi*radio**2)
longitud=(2*math.pi*radio)

print("el valor del area es:" , area)                            
print(f"el valor del area es: {area}")
print(f"el valor del area es: {area:.2f}") #redondeo 2 decimales
print("el valor del area es: %.2f"% area) #redondeo 2 decimales

print("la longitud de la circunferencia es:" ,longitud)
print(f"la longitud de la circunferencia es: {longitud}")
print(f"la longitud de la circunferencia es: {longitud:.2f}") #redondeo 2 decimales
print("la longitud de la circunferencia es: %.2f" % longitud) #redondeo 2 decimales
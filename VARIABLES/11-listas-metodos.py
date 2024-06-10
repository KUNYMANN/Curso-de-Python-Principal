lenguajes=["Python","Ruby", "PHP","Javascript","Java"]
#como INSERTAR elementos
lenguajes.insert(3, "HTML")
lenguajes.insert(0,"Word")
print(lenguajes)
#como ELIMINAR elementos
lenguajes.remove("Ruby")
print(lenguajes)
#como PREGUNTAR si existe un elemento dentro de la lista
print("PHP"in lenguajes)#si esta dentro del listado dira True, si no esta dira False
print(len(lenguajes)) #acceder cuantos elementos contiene un listado
lenguajes.clear() #para limpiar el listado y que no contenga absolutamente nada
print(lenguajes)
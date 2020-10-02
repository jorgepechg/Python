#CICLO FOR

#Con FOR evitamos estar repitiendo el codigo para obtener variables de listas y diccionarios
#for recorre las listas y asigna el valor de cada varible de la lista a una sola variable que 
#especificamos al llamar a la función. Estructura: for nombreVariable in nombreLista
#De esta forma nosotros obtenemos todos los valores sin ir especificando la posicion de cada valor

nombre = "jorge"

for elemento in nombre:
    print(elemento)

person = {"name":"Marines","lastName":"Mendez","age":24}

for value in person:
    print(value) #me devuelve solo el nombre de las claves

for key, value in person.items():
    print(key, " ", value) #me devuelve el nombre de las claves y los valores





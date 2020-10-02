
#ARREGLOS O LISTAS

#Los valores que se encuentran dentro de un arreglo deben de ser del mismo tipo de dato
#El arreglo le asigna un identificador a cada valor
numbers = [1,2,3,4,5]
#          0 1 2 3 4  <-- identificadores (indice)
print(numbers[2])

colores = ["verde","morado","amarillo"]
#          0,       1,       2
print(colores[2])

#DICCIONARIOS O ARREGLOS ASOCIATIVOS

#Es una estructura de datos con caracteristicas especiales que nos permiten almacenar cualquier tipo de valor
#Nos permiten identificar cada elemento con una clave
#Hacemos uso de una clave y un valor.  "nombredelaClave":valor,

person = {"name":"Marines","lastName":"Mendez","age":24}
print(person.get("name"))

#FUNCIONES IMPORTANTES EN ARREGLOS

numbers = [1,2,3,4,5]
numbers.append(7)#Nos agrega un valor al final de la lista
print(numbers)

print(numbers.pop(0))#Nos devuelve un valor de acuerdo a su posición y lo retira de la lista
print(numbers)

numbers.insert(0,8)#agrega un valor, primero se define la posicion del indice
print(numbers)

numbers.remove(8)#remueve un elemento, pero sin devolvernos su valor
print(numbers)





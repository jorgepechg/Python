#FUNCIONES

#Estructura de una función
#palabraclave nombredelafuncion(parametro1, parametro2){
#             variable = parametro1 * parametro2
#             variable = variable * 7
#             return variable
# }

#Función con argumento ingresado en pantalla, la función se llama dentro la impresión
def saludar(nombre):
    return "Hola {} eres puto".format(nombre) #.format nos ayuda adar formato a la salida

print("Ingresa tu nombre: ") #se imprime solicitud para ingresar el argumento de la función
nombre = input() #en esta ocasion el valor del parametro(argumrnto) se le pide al usuario en pantalla 
print(saludar(nombre)) #llamada de la función dentro la impresión

#Función con argumentos ingresados en la llamada, la impresión se genera dentro de la función
def salarioporsemana(hrs, salariohr, prof):
    salario = hrs * salariohr
    salario = salario * 7
    return print("El salario de un", prof, "es", salario) #la función imprime directamente en pantalla

salarioporsemana(8, 284, "doctor") #los argumentos se ingresan en la llamada de la función



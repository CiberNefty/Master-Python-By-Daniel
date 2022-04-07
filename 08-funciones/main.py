"""
FUNCIONES:
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre
concreto que pueden reutilizarse invocando a la funcion 
tantas veces como sea posible.

def nameMyfuncion(parametros):
    # Bloque / conjunto de instrucciones

nameMyfuncion(mi_parametro)
nameMyfuncion(mi_parametro)
"""
# Ejemplo 1
print("####### EJEMPLO 1 ########")

# Definir funcion
def muestraNombres():
    print("Daniel")
    print("Paco")
    print("elsa")
    print("Thor")
    print("Nestro")
    print("Pipe")
    print("Felipe")
    print("\n")

# Invocar funcion
muestraNombres()
muestraNombres()
muestraNombres()
#--------------------
# EJjemplo 2: Parametros
# Un dato que le paso desde afuera hacia la funcion, para poder parametrizar 
print("####### EJEMPLO 2 ########")
"""
def mostrarTuNombre(nombre,edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
#mostrarTuNombre("Jose Peres")
#mostrarTuNombre("PAquito")
#mostrarTuNombre("Juanfran")
#mostrarTuNombre(nombre,9) # esta es un dato fijo
mostrarTuNombre(nombre,edad) 
"""
#---------------------
# Ejemplo 3
print("####### EJEMPLO 3 ########")
def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")
    for contador in range (11):
        operacion = numero *contador
        print(f"{numero} * {contador} = {operacion}")

    print("\n")

tabla(3)
tabla(7)
tabla(12)
# Ejemplo 3.1 
# sacando todas las tablas de multiplicar utilizandoo esta funcion
print("---------------------------------")
for ntabla in range (1,11):
    tabla(ntabla)
#-----------------------
# Ejemplo 4.
print("\n####### EJEMPLO 4 ########")
# Parametros opcionales
def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Daniel Vera",3232)
#--------------------------
# Ejemplo 5. return o devolver datos
print("\n####### EJEMPLO 5 ########")
def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

print(saludame("VIctor"))
#-------------------------
# Ejemplo 6. 
# Generar una calculadora en un string
print("\n####### EJEMPLO 6 ########")

def calculadora(num1, num2, basicas = False):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    division = num1 / num2

    cadena = ""
    if basicas != False:
        cadena += "Suma: "+str(suma)
        cadena += "\n"
        cadena += "Resta: "+str(resta)
    else:
        cadena += "\n"
        cadena += "Multiplicacion: "+str(multi)
        cadena += "\n"
        cadena += "Division: "+str(division)    

    return cadena

print(calculadora(56,5,True))
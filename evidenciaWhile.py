#Programa que muestre al usuario al sig menu

print("Bienvenido, oprima la opcion que desea")
print("operaciones: [1]suma,[2]resta,[3]multitplicacion,[4]division.[5]salir")
eleccion = int(input("Selecciona una de las opciones anteriores: "))
if eleccion == 1:
    #suma
    n1 = int(input("introduce el primer numero: "))
    n2 = int(input("introduce el segundo numero: "))
    print(f"{n1} + {n2} = {n1 + n2}")
    espacio = input()
elif eleccion == 2:
    #resta
    n1 = int(input("Introduce el primer numero: "))
    n2 = int(input("Introduce el segundo numero: "))
    print(f"{n1} - {n2} = {n1 - n2}")
    espacio = input()
elif eleccion == 3:
    #multiplicacion
    n1 = int(input("Introduce el primer numero: "))
    n2 = int(input("Introduce el segundo numero: "))
    print(f"{n1} * {n2} = {n1 * n2}")
    espacio = input()

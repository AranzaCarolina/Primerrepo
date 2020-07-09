#Menu Ciclico

while True:
    print("operaciones: [1]suma, [2]resta, [3]multitplicacion, [4]division, [5]salir")
    eleccion = input("Selecciona una de las opciones anteriores: ")

    if eleccion == "1" or eleccion == "2" or eleccion == "3" or eleccion == "4":
        n1 = int(input("introduce el primer numero: "))
        n2 = int(input("introduce el segundo numero: "))
    if eleccion == "1":
        #suma
        print(f"{n1} + {n2} = {n1 + n2}")
    elif eleccion == "2":
     #resta
     print(f"{n1} - {n2} = {n1 - n2}")
    elif eleccion == "3":
     #multiplicacion
     print(f"{n1} * {n2} = {n1 * n2}")
    elif eleccion == "4":
     #division
     print(f"{n1} / {n2} = {n1 / n2}")
    elif eleccion == "5":
        print ("Adios")
        break
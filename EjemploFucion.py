#programa que pida al usuarioun texto y un numero entero.
#Imprimir el texto repetido las veces indicado por el numero
#Nota: hacer el prgrama usando una funcion
#
#ingresa un texto: hola
#ingresa un num: 4
#salida:
#hola
#hola
#hola
#hola
#

#Declarar funcion
def repetir(texto, numero):
    texto += '\n'
    print(texto*numero)

#escribir el codigo para usar la funcion
t = input("ingresa un texto: ")
n = int(input("ingresa un numero: "))

repetir(t,n)


#Escribir un programa que pida al usuario 2 numeros enteros
#y calcular la suma desde el numero 1 hasta el numero 2
#imprimir el resultado de la suma

print("bienvenido")
num1 = int(input("dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))

suma = 0 

for n in range(num1,num2+1):
    suma+=n
print(f'la suma es {suma}')


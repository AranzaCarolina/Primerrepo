def calcularSuma(numini,numfin):
    suma = 0
    for num in range(numini,numfin+1):
        suma += num
    return suma

def calcularSuma2(numini,numfin):
    suma = 0
    for num in range(numini,numfin+1):
        suma += num 
    print(f"la suma es {suma}")


#Probar la funcion
print(f"la suma es {calcularSuma(1,10)}")
calcularSuma2(10,100)

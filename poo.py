class MaquiVending:
    totalMaquinas=0 #atributo de clase(una para todos los objetos)
    dueño = "empresax" #atributo de clase 

    def __int__(self,empresa,tipo="combo",tipoMoneda="moneda/billete",empresa):
        self.tipo = tipo
        self.tipoMoneda = tipoMoneda
        self.empresa = empresa

maqFacpya = MaquiVending("combo","moneda/billete","facpya")
bancoAcme = Bank(45121,"conocida")

print(maqFacpya.tipo )


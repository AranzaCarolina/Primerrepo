class PlazaComercial:

    def __int__(self,nombre,municipio):
        self.__nombre = nombre
        self.__muncipio = municipio

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nuevoNombre):
        self.__nombre = nuevoNombre

    @property
    def municipio(self):
        return self.__muncipio

    @municipio.setter
    def municipio(self,nuevoMunicipio):
        self.__muncipio = nuevoMunicipio

    def imprimirInfo(self):
        print(f"Plaza:{self.__nombre},Mun:{self.__muncipio}")

plazaGalerias = PlazaComercial("Galerias Mty","Escobedo")
plazaGalerias.municipio = "mty" #municipio de la plaza
print(plazaGalerias.nombre()) #Nombre de la plaza
plazaGalerias.imprimirInfo()
#¿que hago si me equivoque con el municipio?, usar el getters y el setters




textField = JTextField(20) #Caja de texto 
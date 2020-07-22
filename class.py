class PlazaComercial:
    
    def __init__(self,nombre,municipio):
        self.__nombre = nombre
        self.__municipio = municipio
 
    @property    
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevoNombre):
        self.__nombre = nuevoNombre
 
    @property
    def municipio(self):
        return self.__municipio
    
    @municipio.setter
    def municipio(self,nuevoMunicipio):
        self.__municipio = nuevoMunicipio
 
    def imprimirInfo(self):
        print(f"Plaza:{self.__nombre},Mun:{self.__municipio}")
 
    @classmethod
    def creaPlaza(cls):
        return cls(None,None)
 
    @staticmethod
    def saludo():
        print("hola desde mi clase: PlazaComercial")
 
otraplaza = PlazaComercial("nueva","san pedro")
 
nuevaPlaza = PlazaComercial.creaPlaza()
 
nuevaPlaza.nombre = "nuevo sur"
nuevaPlaza.municipio = "gpe"
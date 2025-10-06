class SocioNegocio:
    def __init__(self,run,nombre,apellido,direccion,fono,correo):
        self.__run =run
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__fono = fono
        self.__correo = correo
    
    def getRun(self):
        return self.__run
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDireccion(self):
        return self.__direccion
    
    def getFono(self):
        return self.__fono
    
    def getCorreo(self):
        return self.__correo

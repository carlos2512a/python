from DTO.socioNegocio import SocioNegocio 
class Cliente(SocioNegocio):
    def __init__(self, run,nombre,apellido, direccion, fono, correo,codigo ,tipo,montoCredito,deuda):
        super().__init__(run,nombre, apellido,direccion,fono,correo)
        self.__codigo = codigo
        self.__tipo = tipo
        self.__montoCredito = montoCredito
        self.__deuda = deuda
    
    def __str__(self):
        return f"Cliente de run:{self.getRun()}"
    
    def getCodigo(self):
        return self.__codigo
    
    def getTipo(self):
        return self.__tipo 
    
    def getmontoCredito(self):
        return self.__montoCredito
    
    def getDeuda(self):
        return self.__deuda

carlos = Cliente(12314,"Carlos","Apellido","Puente Alto",87987897,"carlos@carlos",1,1,600000,60000)
print(carlos)

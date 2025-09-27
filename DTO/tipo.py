import pymysql 

class Tipo:
    def __init__(self,codigo,nombre):
        self.con = pymysql.connect(codigo=codigo,nombre=nombre)
        self.cursor = self .con.cursor()
        
    def __str__(self,sql):
        self.cursor.execute(sql)
        return self.cursor
    
    def desconectar(self):
        self.con.close()
        
    def commit(self):
        self.con.commit()
        
    def rollback(self):
        self.con.rollback()

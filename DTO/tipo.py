import pymysql
class Tipo: 
    def __init__(self, id, nombre):
        self.con = pymysql.connect(id=id , nombre=id)
        self.cursor = self.con.cursor() 

    def __str__(self):
        return F"Cliente de run:{self.con}"

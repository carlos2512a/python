from DAO.conexion import Conexion
import os
from dotenv import load_dotenv
from DTO.cliente import Cliente

load_dotenv()
host = os.getenv("HOST")
passwd = os.getenv("PASS")
user = os.getenv("USER")
db = os.getenv("DB")



def agregar(c:Cliente):
    try:
        con = Conexion(host,user,passwd,db)
        sql =f"insert into cliente set cli_run='{c.getRun()}',cli_nombre='{c.getNombre()}',cli_apellido='{c.getApellido()}',cli_direccion='{c.getDireccion()}',cli_fono={c.getFono()},cli_correo='{c.getCorreo()}',cli_monto_credito={c.getmontoCredito()},cli_deuda={c.getDeuda()},TIPO_ID={c.getTipo()}"
        con.ejecutarQuery(sql)
        con.commit()
        con.desconectar()
    
    except Exception as e:
        print(e)

    


def mostrarParcial(cant):
    datos=""
    try:
        con = Conexion(host,user,passwd,db)
        sql ="select * from cliente"
        cursor = con.ejecutarQuery(sql)
        datos = cursor.fetchmany(size=cant)
        con.desconectar()
    except Exception as e:
        print(e)
    return datos

def mostrarTodos():
    datos=""
    try:
        con = Conexion(host,user,passwd,db)
        sql ="select * from cliente"
        cursor = con.ejecutarQuery(sql)
        datos = cursor.fetchall()
        con.desconectar()
    except Exception as e:
        print(e)
    return datos

def mostrarParticular(id):
    dato = "Problema con mostrar cliente..."
    try:
        con = Conexion(host,user,passwd,db)
        sql ="select * from cliente where cli_id='{}'".format(id)
        cursor = con.ejecutarQuery(sql)
        datos = cursor.fetchone()
        con.desconectar()
    except Exception as e:
        print(e)
        return datos
    

def editar(c:Cliente):
    try:
        con = Conexion(host,user,passwd,db)
        sql =f"update cliente set cli_run= '{c.getRun()}',cli_nombre='{c.getNombre()}',cli_apellido='{c.getApellido()}',cli_direccion='{c.getApellido()}',cli_fono={c.getFono()},cli_correo='{c.getCorreo()}',cli_id={c.getId()},TIPO_ID={c.getTipo()},cli_monto_credito='{c.getmontoCredito()},cli_deuda={c.getDeuda()}"
        con.ejecutarQuery(sql)
        con.commit
        con.desconectar()
    except Exception as e:
        print(e)
    
def eliminar(c:Cliente):
    try:
        con = Conexion(host,user,passwd,db)
        sql =f"delete from cliente where cli_id= {c.getId()};"
        con.ejecutarQuery(sql)
        con.commit
        con.desconectar()
    except Exception as e:
        print(e)

carlos = Cliente(12314,"Javier","Jaramillo","Puente Alto",87987897,"carlos@carlos",0,1,600000,60000)
agregar(carlos)


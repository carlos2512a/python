#Vamos a crear un diccionario donde cada clave va ser el rut y el valor va ser otro diccionario


alumnos={
    '12345678-9':{
        'nombre':'juan',
        'edad':20,
        'carrera':'Ingieneria'
    },
    '98765432-1':{
        'nombre':'Carlos',
        'edad':30,
        'carrera':'Ingieneria'
    }
}

#Acceder a un alumno especifico
print(alumnos['12345678-9']['nombre'])#Juan

#Recorrer diccionario
 
for rut,datos in alumnos.items():
    print(f'Rut:{rut}')
    print(f'Nombre:{datos['nombre']}')
    print(f'edad{datos['edad']}')
    print(f'carrera{datos['carrera']}\n')



#crear un programa que:
# permita agregar 2 alumnos desde el teclado(input)
# Guarde los datos en un diccionario
#Imprima todos los alumnos

alumnos={}
#repetir 2 veces para ingresar 2  veces 
for i in range(2):
 print(f'\ Registro del primer alumno{i+1}')
 rut=input('ingrese el rut del alumno:')
 nombre=input('Ingrese nombre')
 edad=int(input('Ingrese su edad:'))
 carrera=input('Ingrese la carrera:')
 
 #Guardar datos en el diccionario
 alumnos[rut]={
     'nombre':nombre,
     'edad':edad,
     'carrera':carrera,
 }
 #Mostrar todos los datos del alumno
 
for i, (rut, datos) in enumerate(alumnos.items()):
    print(f'alumno{i}')
    print(f'rut:{rut}')
    print(f'nombre:{datos['nombre']}')
    print(f'edad{datos['edad']}')
    print(f'carrera{datos['carrera']}\n')



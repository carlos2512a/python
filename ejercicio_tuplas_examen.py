#ejercicios tuplas
#crear una tuplas que se llame datos personales e ingrese  sus 2 nombres y sus apellidos 
# e imprima me llamo (nombre),(nombre2), y mi apellidos son(apellido),(apellido2)

datos_personales=()

datos_personales=('carlos','humerto','villanueva','martinez')

nombre,nombre2,apellido,apellido2=datos_personales
print(f'Me llamo{nombre} {nombre2} y mi apellidos son {apellido} {apellido2}')

#2
datos_personales=('carlos','humberto','villanueva','martinez')
print(datos_personales)#imprime tupla completa
print(datos_personales[1])
#DESEMPAQUETAR TUPLA
nombre,nombre2,apellido,apellido2=datos_personales

nombre1=datos_personales[0]
nombre2=datos_personales[1]
apellido=datos_personales[2]
apellido2=datos_personales[3]



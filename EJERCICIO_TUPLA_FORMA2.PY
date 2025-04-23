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

#crea una tupla que se llame cordenadas "x" "y" y "z"
#desempaquete la tupla impreme las cordenadas X es .--- y es--- y z es---

cordenadas=()
cordenadas=('x','y','z')
x,y,z=cordenadas
print(f'la cordenada x es{x} la cordenada y es {y} la cordenada z es {z}')

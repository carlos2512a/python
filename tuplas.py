#Tuplas Ordenadas y no Modificables
colores=('rojo','azul','verde')
print(colores[1]) #azul
mi_tupla=('Python',3.10,True)
print(mi_tupla[0])#Python

producto=('Teclado',2500,'electronica')

#Acceso por indice
nombre=producto[0]
precio=producto[1]

print(f'{nombre} cuesta $ {precio}')

#recorres tupla con for
colores=('rojo','azul','verde')
for color in colores:
    print(color)
    
#Desempaquetar tupla
persona=('pedro',25,'chile')
nombre,edad,pais=persona
print(f'{nombre} tiene{edad} es{pais}')
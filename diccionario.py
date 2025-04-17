#diccionario
# Un diccionario
persona={'nombre':'ana','edad':30}
print(persona['nombre'])#Ana
print(persona)
persona={
    'nombre':'ana',
    'edad':30,
    'ciudad':'santiago'
}
#Clave o variables:nombre,edad,ciudad
#valores:Ana,30,santiago

#Acceder a datos

print(persona['nombre'])#Ana
print(persona['ciudad'])#Santiago

#Crear diccionario desde 0

producto= {}# diccionario vacio

producto['nombre']='Mouse'
producto['precio']=12000
producto['STOCK']=25

print(producto)

for clave in producto:
    print(clave,'->',producto[clave])

#Modificar agregar y eliminar datos
producto['stock']=30 #modificar
producto['categoria']='periferico' #Agregar
del producto['precio']#eliminar
print('--------------')
print(producto)
producto.remove('stock')
print(producto)
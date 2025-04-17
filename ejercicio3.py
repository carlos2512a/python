#ejercicio 3
#while y diccionario de datos
#diccionario productos
#usuario debe agregaR PRODUCTOS (while)
#cuando el ususario termine de agrefar productos escruiba 'salir y salga'
#utiliza for para mostrar los productos

productos={}

while True:
    nombre=input('Ingrese el nombre del producto (o "salir" para terminar)')
    if nombre=='salir':
        break
    precio=int(input('Precio:'))
    stock=int(input('stock:'))
    
    productos[nombre]={
        'precio':precio,
        'stock':stock
}

print('Lista de productos')
for  nombre,datos in productos.items():
    print(f'el producto{nombre} cuesta ${datos[precio]} y quedan {datos['stock']} unidades')
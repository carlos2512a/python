#Ejercicios 2
#crea una tupla de un alumno que contenga nombre , edad y carrera
#Imprime un mensaje con estos datos

Alumno=('carlos',18,'informatico')
nombre,edad,carrera=Alumno
print(f'{nombre} tiene {edad} es  {carrera}')

#lista de tuplas

ventas=[
    ('auto', 2000.000,'2025-04-12'),
    ('computador', 50.000,'2025-03-12'),
    ('celular', 80.000,'2025-04-12')]

#Recorres e imprimir ventas

for producto, precio, fecha in ventas:
    print(f'producto {producto},precio {precio},fecha{fecha}' )

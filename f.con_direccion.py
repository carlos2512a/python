nombre=input('¿Cual es tu nombre?')
apellido=input('¿Cual es tu apellido?')
edad=int(input('¿Cual es tu edad?' ))
edad_amigo=30
direccion=input('¿Cual es tu direccion? ')
numero_direccion=int(input('¿Numero de direccion? '))
suma=edad+edad_amigo
#print(nombre,apellido,direccion,numero_direccion,suma)

#f-strings
print(f'nombre Completo:{nombre} {apellido}')
print(f'Direccion y numero completo:{direccion} {numero_direccion}')
print(f'suma de edades:{suma}')

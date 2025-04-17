#crea una lista vacia que se llame nombres
#luego permite que el ususario ingresar nombres en un bucle hasta que escriba 'fin'

#luego agrega a cada nombre ala lista eh imprimelos(opcional enumerados)usando el bucle for

nombres=[]

while True:
    nombre=input('Ingrese el nombre o escriba ''fin''para salir ')
    if nombre== 'fin':
     break
    nombres.append(nombre)
    
print('lista de nombres')

for i ,nombre in enumerate(nombres,start=1):
    print(f'{i}-.{nombre}')
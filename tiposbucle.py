#while repite mientra la condicion sea verdadera
contador=1

while contador <=5:
    print(f'numero:{contador}')# o print ('numero:',contador)
    contador+=1 #contador=contador+1
    
#for recorre una secuencia
print('----------------------------------------------------')
for numero in range(1,6):
    print(f'Numero:{numero}')
    
#ejercicio
#ingrese un numero que imprima desde uno hasta el numero que dio el ususario

limite=int(input('INGRESE EL NUMERO'))
contador=1

while contador <=limite:
    print(contador)
    contador += 1 #contador = contador +1
    
    
#Bucle infinito

while True:
    nombre=input('escribe tu nombre')
    print(f'Hola {nombre} ')    
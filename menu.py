#Menu con while True
while True:
    print('\n Menu:')
    print('1-.Saludar')
    print('2-.Pregunta edad')
    print('3-. Salir')

    opcion=input('Elige una opcion 1/2/3:')

    if opcion == '1':
        print('Holaaaaaa!!')
    elif opcion =='2':
        edad=int(input('¿Cual es tu edad?'))
        print(f'Tienes {edad} años')
    elif opcion == '3':
           print('Hasta luego') 
           break
    else:
     print('Opcion no valido,intente de nuevo')
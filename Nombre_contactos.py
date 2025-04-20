contactos={}

while True:
    nombre=input('Ingresa un nombre("salir" o terminar)')
    if nombre =='salir':
        break
    telefono=input(f'Ingresa el numero telefono{nombre}:')
    edad=input(f'ingrese la edad {nombre}')
    contactos[nombre]={
        'Telefono':telefono,
        'edad':edad
    }
    
    print("\n Lista de contacto")
    for nombre,datos in contactos.items():
        print(f"{nombre}: telefono: {datos['Telefono']} edad: {datos['edad']}")

        
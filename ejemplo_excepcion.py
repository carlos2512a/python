#usuario ingrese los datos 
#y muestre el resultado de la division del primero por el segundo 

while True:
    try:
        num1= int(input ('Ingrese el primero numero: '))
        num2= int(input ('Ingrese el primero numero: '))
        
        resultado = num1/num2
        print (f' El resultado de la division es: {resultado} ')
        break
    except ValueError:
        print('Error: Numero no valido')
    except ValueError:
        print('Error: Numero no se puede dividir por cero')
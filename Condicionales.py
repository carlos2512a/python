#condicionales
#permite que tu programa toma decisiones

edad=20

if edad >=18:
    print('Eres mayor de edad')

#IF/ELIF/ELSE

edad=int(input('¿Cual es tu edad? '))

if edad<18:
    print('Eres menor de edad')
elif edad==18:
    print('Justo tienes 18')
else:
    print('Eres menor de edad')
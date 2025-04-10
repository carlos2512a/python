#Ejercicio con listas
# 1-pedir al ususario que ingrese 3 comidas
# 2 -Guardar en una lista
# 3 Imprima una por una

#crear una lista
# Paso 1: crear una lista
comidas=[]

# Paso 2 :Ingresar las 3 comidas

for i in range(4):
    comida=input(f'Ingrese su comida favorita N°{i+1}:  ')
    comidas.append(comida)
    
#PASO 3: Mostra comida 1*1

print('\n Tus comidas favoritas son:')
for comida in comidas:
    print(f'- {comida}')
    
comidas.append(comida)

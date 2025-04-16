#Solicito nombre completo e ingrese valores de forma numerica
# Ejemplo ingrese su nombre completo de acuerdo a su peticion
nombre=[] 

print('Registro de apellidos y nombres')
print('Ingrese nombre completo')


for i in range(4):
    entrada=input(f'Ingrese sus datos uno a uno{i+1} :')
    nombre.append(entrada)
    
    
print('Tus datos son:')
for nombre in nombre:
     print('-'+ nombre)
  



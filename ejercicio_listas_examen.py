#es crear una lista vacia que se llame compras
#pide al ususario que ingrese
compras=[]
while True:
    producto=input('INGRESE EL PRODUCTO O INGRESE UN "fin" para terminar')
    if producto =='fin': #if producto.lower()=='fin'
        break
    compras.append(producto)
    print('Lista de procutos ingresados')
    #for i , producto in enumerate (compras,start=1):
        #print(f'{i}.{producto}')
        
contador=1
for producto in compras:
    print(f'{contador}.{producto}')
    contador+=1
#listas

frutas=['Manzana','Pera','Mango']
#indice parte en 0 y cada valor recibe el numero en elemento

#acceder a los elementos

print(frutas)
print(frutas[0]) #manzana
print(frutas[2]) #mango
      
#modificar elemento lista
frutas[1]='Kiwi'
print(frutas)  #manzana,kiwi,mango
      
#metodos utiles para modificar
frutas.append('uva') #agregar
print(frutas) #['manzana','kiwi','mango','uva']

frutas.remove('Manzana') #eliminar
print(frutas) #['kiwi','Pera','uva']

print(len(frutas)) #Cantidad  de elementos
frutas.sort()#ordenar alfabeticamente
print(frutas)
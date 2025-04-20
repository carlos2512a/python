#while y diccionario de datos
#Diccionarion de nombre, edad 
#Usuario debe agragar nombre (While)
#Cuando el ususario termine de agregar los datos escriba 'Salir'o salga para terminar'
#Utiliza el for para mostrar los productos

personas = {}

while True:
    nombre = input("Ingresa un nombre (o escribe 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    edad = input(f"Ingresa la edad de {nombre}: ")
    personas[nombre] = int(edad)

print("\nDatos ingresados:")
for nombre, edad in personas.items():
    print(f"{nombre} tiene {edad} años.")

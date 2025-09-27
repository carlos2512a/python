class Libro:
    def __init__(self,isbn,titulo,autor,pagina,año,formato):
       self.isbn=isbn
       self.titulo=titulo
       self.autor=autor
       self.pagina=pagina
       self.año=año
       self.formato=formato

    def identificacion(self):
        print("-----------------------")
        print("El Isbn es",self.isbn)
       
        print("El Titulo es",self.titulo)
       
        print("El Autor es",self.autor)
       
        print("El Pagina es ",self.pagina)
       
        print("El Año creado es",self.año)
        
        print("El Formato es ",self.formato)
        
    def cambiar_titulo(self,nuevo_titulo:str):
        self.titulo= nuevo_titulo
        
L1= Libro("244-2751-62-4","Overview","George Orwell","328","1949","Novela")
L2= Libro("234-4444-52-3","Cien Años De Soledad","Gabriel Garcia","417","1987","Novela Magico")
L3= Libro("123-1234-12-1","Overview","George Orwell","328","1949","Novela")

libros=[L1,L2,L3]

L1.cambiar_titulo("mujercita")

for libro in libros:
    libro.identificacion()
    
    
    

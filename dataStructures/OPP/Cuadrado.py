class Cuadrado:
    def __init__(self, lado):
        self.lado=lado

    def area(self):
        print("El area es: ",self.lado*self.lado)
    
    def perimetro(self):
        print("El perimetro es: ",self.lado*4)

cuadrado=float(input("Escribe el valor del lado: "))
cuadrado1=Cuadrado(1) #Se crea el objeto cuadrado 1 de la clase cuadrado 
cuadrado1.area()
cuadrado1.perimetro()

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho=ancho
        self.alto=alto

    def area(self):
        area=self.alto*self.ancho
        return area
    
    def perimetro(self):
        perimetro=(self.alto*2)+(self.ancho*2)
        return perimetro
    
rectangulo1=Rectangulo(4,2)
area=rectangulo1.area()
perimetro=rectangulo1.perimetro()
print("El area es: ",area)
print("El perimetro es: ",perimetro)

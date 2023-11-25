class Triangulo:
    def __init__(self, base, altura, lado):
        self.base=base
        self.altura=altura
        self.lado=lado

    def area(self): 
        print("El area es: ",self.base*((self.radio*self.altura)/2) )
    
    def perimetro(self):
        print("El perimetro es: ", 2*self.lado+self.base)

triangulo1=Triangulo(3,5)
area=triangulo1.area()
perimetro=triangulo1.perimetro()
print("El area es: ",area)
print("El perimetro es: ",perimetro)

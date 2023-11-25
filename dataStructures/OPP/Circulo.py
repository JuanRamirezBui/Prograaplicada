class Circulo:
    pi=3.14
    
 

    def __init__(self, radio):
        self.radio=radio

    def circunferencia(self):
        return 2*self.pi*self.radio

    def area(self):
        return self.pi*(self.radio**2) 
    
    def perimetro(self):
        return 2*self.pi*self.radio

circunferencia_circulo=Circulo(12)
print(circunferencia_circulo.circunferencia())
area_circulo=Circulo(5)
print(area_circulo.area())
perimetro_circulo=Circulo(5)
print(perimetro_circulo.perimetro())

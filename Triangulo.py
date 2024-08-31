from Figura import Figura

class Triangulo(Figura):

    def __init__(self, lado=0,altura=0):
        super().__init__(lado,altura)

    def areaTriangulo(self):
        return (self.lado*self.altura)/2
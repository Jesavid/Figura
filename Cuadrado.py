from Figura import Figura

class Cuadrado(Figura):

    def __init__(self, lado=0):
        super().__init__(lado)

    def areaCuadrado(self):
        return self.lado*self.lado

    def perimetroCuadrado(self):
        return 4*self.lado
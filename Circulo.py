from Figura import Figura

class Circulo(Figura):

    def __init__(self, radio=0, pi=3.14159):
        super().__init__(radio, pi)

    def areaCirculo(self):
        return self.pi*self.radio*self.radio
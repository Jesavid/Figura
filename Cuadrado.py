from Figura import Figura

class Cuadrado(Figura):

    def __init__(self, lado):
        super().__init__(lado)

    def areaCuadrado(self):
        return self.lado^2
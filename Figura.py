# Establecer una figura lado con los atributos de lado, apotema, y radio


class Figura:
    def __init__(self, lado=0, apotema=0, radio=0):
        self.lado = lado
        self.apotema = apotema,
        self. radio = radio


    # Definicion de getters an setters
    def set_lado(self, lado):
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_apotema(self, apotema):
        self.apotema = apotema

    def get_apotema(self):
        return self.apotema

    def set_radio(self, radio):
        self.radio = radio

    def get_radio(self):
        return self.radio

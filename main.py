from Cuadrado import Cuadrado
from Circulo import Circulo
def main():
    cuadrado = Cuadrado()
    circulo = Circulo()

    print("1. Cuadrado")
    print("2. Circulo")
    print("3. Triángulo")
    seleccion = int(input("¿Que desea hacer? "))

    if (seleccion == 1):
        lado = int(input("El lado del cuadrado es: "))
        cuadrado.set_lado(lado)
        print(f"El área del cuadrado es: {cuadrado.areaCuadrado()}")
        print(f"El perimetro del cuadrado es: {cuadrado.perimetroCuadrado()}")

    elif (seleccion == 2):
        radio = int(input("El radio del ciruclo es: "))
        circulo.set_radio(radio)
        print(f"El área del circulo es: {circulo.areaCirculo()}")




if __name__ == '__main__':
    main()
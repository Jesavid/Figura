from Cuadrado import Cuadrado
from Circulo import Circulo
from Triangulo import Triangulo
def main():
    cuadrado = Cuadrado()
    circulo = Circulo()
    triangulo = Triangulo()

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

    elif (seleccion == 3):
        base = int(input("La base del triangulo es: "))
        triangulo.set_lado(base)
        altura = int(input("La altura del triangulo es: "))
        triangulo.set_altura(altura)
        print(f'El area del triángulo es: {triangulo.areaTriangulo()}')




if __name__ == '__main__':
    main()
from Cuadrado import Cuadrado

def main():
    cuadrado = Cuadrado()

    lado = int(input("El lado del cuadrado es: "))
    cuadrado.set_lado(lado)
    print(cuadrado.areaCuadrado())
    print(cuadrado.perimetroCuadrado())

if __name__ == '__main__':
    main()
def main():
    lado1 = int(input("Ingresa la medida del lado 1: "))
    lado2 = int(input("Ingresa la medida del lado 2: "))
    lado3 = int(input("Ingresa la medida del lado 3: "))
    #Escribe aquí tu código...

    if lado1 == lado2 and lado2 == lado3 :
        print("Es un triangulo equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3 :
        print("Es un triangulo isosceles")
    else:
        print("Es un triangulo escaleno")


if __name__=='__main__':
    main()


def main():
    edad = int(input("Ingresa tu edad: "))
    #Aquí empieza tu programa...

    if edad >= 18 :
        print("Cumples con los requisitos")
    elif edad <= 17 :
        print("No cumples con los requisitos")
    else :
        print("respuesta incorrecta")

    identificaion = str(input("Tiene identificacion oficial s/n?: "))
    if identificaion == "s" :
        print("Cumples con los requisitos")
    elif identificaion == "n" :
        print("No cumples con los requisitos")
    else:
        print("respuesta incorrecta")

if __name__ == '__main__':
    main()

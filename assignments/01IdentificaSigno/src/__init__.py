# You can safely ignore this file
def main():
    numero = int(input("Dame un número: "))
    if numero >= 1 :
        print("Es positivo")
    elif numero <= -1 :
        print("Es negativo")
    else:
        print("Es cero")
    

if __name__ == '__main__':
    main()

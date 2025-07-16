def ingresar_producto(productos):
    while True:
        codigo = input("Ingrese el código del producto (ej. P001): ")
        if codigo in productos:
            print(" Ese código ya existe. Ingrese un código único.")
        else:
            break

    nombre = input("Ingrese el nombre del producto: ")

    while True:
        categoria = input("Ingrese la categoría (Hombre/Mujer/Niño): ")
        if categoria in ["Hombre", "Mujer", "Niño"]:
            break
        else:
            print(" Categoría inválida. Intente con Hombre, Mujer o Niño.")

    while True:
        talla = input("Ingrese la talla (S, M, L, XL): ")
        if talla in ["S", "M", "L", "XL"]:
            break
        else:
            print(" Talla inválida. Intente con S, M, L o XL.")

    while True:
        try:
            precio = float(input("Ingrese el precio unitario (Q): "))
            if precio > 0:
                break
            else:
                print(" El precio debe ser mayor que Q0.00")
        except ValueError:
            print(" Ingrese un número válido.")

    while True:
        try:
            cantidad = int(input("ingrese cantidad de producto en stock "))
            if cantidad > 0:
                break
            else:
                print ("deve ingresar un numero entero positivo")

        except ValueError:
            print("")

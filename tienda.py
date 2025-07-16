def ingresar_producto(productos):
    while True:
        codigo = input("Ingrese el código del producto (ej. P001): ").strip().upper()
        if codigo in productos:
            print(" Ese código ya existe. Ingrese un código único.")
        else:
            break

    nombre = input("Ingrese el nombre del producto: ").strip()

    while True:
        categoria = input("Ingrese la categoría (Hombre/Mujer/Niño): ").strip().capitalize()
        if categoria in ["Hombre", "Mujer", "Niño"]:
            break
        else:
            print(" Categoría inválida. Intente con Hombre, Mujer o Niño.")

